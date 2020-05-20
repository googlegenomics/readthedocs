.. BigQuery documentation links

.. _Standard SQL Query Syntax: https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax
.. _Legacy SQL Migration Guide: https://cloud.google.com/bigquery/docs/reference/standard-sql/migrating-from-legacy-sql
.. _Legacy SQL FLATTEN: https://cloud.google.com/bigquery/docs/reference/standard-sql/migrating-from-legacy-sql#removing_repetition_with_flatten
.. _JOIN: https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#join_types
.. _Query Plan Explanation: https://cloud.google.com/bigquery/query-plan-explanation
.. _WITH clause: https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#with-clause
.. _SAFE_CAST: https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#casting
.. _REGEXP_REPLACE: https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#regexp_replace
.. _CASE function: https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#conditional-expressions
.. _ARRAY: https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#array-type
.. _STRUCT: https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#struct-type
.. _UNNEST: https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#unnest
.. _User Defined Functions: https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions

+--------------------------------------------------------------------------------------------------------------+
| Note: Google Genomics is now Cloud Life Sciences.                                                            |
| The Google Genomics Cookbook on Read the Docs is not actively                                                |
| maintained and may contain incorrect or outdated information.                                                |
| The cookbook is only available for historical reference. For                                                 |
| the most up to date documentation, view the official Cloud                                                   |
| Life Sciences documentation at https://cloud.google.com/life-sciences.                                       |
|                                                                                                              |
| Also note that much of the Genomics v1 API surface has been                                                  |
| superseded by `Variant Transforms <https://cloud.google.com/life-sciences/docs/how-tos/variant-transforms>`_ |
| and `htsget <https://cloud.google.com/life-sciences/docs/how-tos/reading-data-htsget>`_.                     |
+--------------------------------------------------------------------------------------------------------------+

Analyze variants using Google BigQuery
======================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/analyze_variants/analyze_variants_with_bigquery.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

The purpose of this code lab is to help you:

* learn how to use the Google BigQuery query tool
* learn valuable BigQuery SQL syntax
* become familiar with the variants table created by a Google Genomics variant export

BigQuery can use thousands of machines in parallel to process your queries.
This means you can use it to interact with genomic data in an ad-hoc fashion:
Queries that on traditional systems take hours to run (as batch jobs) can
instead be processed in seconds with BigQuery.

This code lab focuses on genomic variant data that has been exported from Google
Genomics to BigQuery. The dataset used is from the public
`Illumina Platinum Genomes project data`_ (6 samples). You may run the same
queries against other datasets exported from Google Genomics, including:

* the `1000 Genomes project data`_
* your own data which you can `load into Google BigQuery <https://cloud.google.com/genomics/v1/load-variants>`_

All output below is for queries against the Platinum Genomes.

Here are some of the questions you'll answer in this code lab about the variant data:

* How many records are in the variants table
* How many variant calls are in the variants table
* How many variants are called for each sample
* How many samples are in the variants table
* How many variants are there per chromosome
* How many high-quality variants per-sample

Here are some of the technical skills you will learn:

* How to get an overview of the data in your table
* How are non-variant segments represented in the variants table
* How are variant calls represented in the variants table
* How are variant call quality filters represented in the variants table
* How to handle hierarchical fields in variants data
* How to count distinct records
* How to group records
* How to write user-defined functions

BigQuery Web Interface
----------------------

So long as you have created a Google Cloud project, then you will immediately
be able to access the BigQuery web interface. Just go to
`http://bigquery.cloud.google.com <http://bigquery.cloud.google.com>`_.

On the left-hand side of the browser window you should see your Cloud project
name displayed like:

   .. image:: analyze_variants_with_bigquery/My_Project_left_hand_nav.png
      :width: 250 px

If you have multiple projects, be sure that the one you want the queries of
this code lab to be billed against is selected. If it is not, then click on the
down-arrow icon, select "Switch to Project" and then select the correct
project.

Add the Genomics public data project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You could immediately start composing queries against any BigQuery data you
have access to, including public datasets. But first let's add a nice
usability shortcut for accessing the Genomics public data.

On the left-hand side of the browser window:

1. Click on the down-arrow icon that is next to your project name
2. Select "Switch to Project"
3. Select "Display Project"
4. Enter "genomics-public-data" in the Add Project dialog
5. Click "OK"

On the left-hand side, you should now see a list of public genomics datasets:

   .. image:: analyze_variants_with_bigquery/My_Project_with_genomics_public_data.png
      :width: 250 px

Table Overview
--------------

Before issuing any queries against the data, let's take a look at some meta
information about the variants table and get familiar with it.

Table schema
~~~~~~~~~~~~

On the left-hand side of the browser window, you should see a list of
BigQuery datasets. Opening "Google Genomics Public Data (genomics-public-data)"
you should see ``platinum_genomes``. Opening ``platinum_genomes``
you should see the ``variants`` table.

Selecting the ``variants`` table from the drop-down, you should now see the
table schema in the right-hand pane:

   .. image:: analyze_variants_with_bigquery/variants_table_schema.png
      :width: 95%

The key fields of the variants table that will be frequently referenced
in this code lab are:

  reference_name
    The reference on which this variant occurs (such as "chr20" or "X").

  start
    The position at which this variant occurs (0-based). This corresponds to
    the first base of the string of reference bases.

  end
    The end position (0-based) of this variant. This corresponds to the
    first base after the last base in the reference allele. So, the length
    of the reference allele is (``end`` - ``start``).

  reference_bases
    The reference bases for this variant.

  alternate_bases
    The bases that appear instead of the reference bases.

and

  call
    The variant calls for this particular variant.

The first set of fields are what makes a ``variants`` record unique.

The ``call`` field contains a list of the calls for the ``variants`` record.
The ``call`` field is an ARRAY (aka REPEATED) field and is a STRUCT
(it contains NESTED fields)
ARRAY and STRUCT fields are discussed further
:ref:`below <array-and-struct-fields>`.

The fixed members of the call field are:

  call.call_set_id
    Unique identifier generated by Google Genomics to identify a callset.

  call.call_set_name
    Identifier supplied on input to Google Genomics for a callset.
    This is also typically known as the sample identifier.

  call.genotype
    Array field containing the numeric genotype encodings for this call.
    Values:

    * -1: no call
    *  0: reference
    *  1: first alternate_bases value
    *  2: second alternate_bases value
    *  ...
    *  n: nth alternate_bases value

  call.genotype_likelihood
    Array field containing the likelihood value for each corresponding
    genotype.

More details about other fields can be found at
`Understanding the BigQuery Variants Table Schema`_.

   +------------------------------------------------------------------------+
   | Data note: 0-based positioning                                         |
   +========================================================================+
   | Note that both the start field and end fields in the variant table are |
   | 0-based. This is consistent with the GA4GH API (which Google Genomics  |
   | implements), but differs from the VCF specification in which the start |
   | column is 1-based and the end column is 0-based.                       |
   +------------------------------------------------------------------------+

How was this table created?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The data in the Platinum Genomes variants table was created by:

1. Copying VCFs into Google Cloud Storage
2. Importing the VCFs into Google Genomics
3. Exporting the variants to Google BigQuery

More on the process can be found
`here <https://cloud.google.com/genomics/v1/load-variants>`__ on
`cloud.google.com/genomics <https://cloud.google.com/genomics>`_.

More on the Google Genomics variant representation can be found
`here <https://cloud.google.com/genomics/reference/rest/v1/variants>`__
`cloud.google.com/genomics <https://cloud.google.com/genomics>`_.

More on the origin of the data can be found
`here <http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/platinum_genomes.html>`_ on
`googlegenomics.readthedocs.org <http://googlegenomics.readthedocs.org>`_.

.. _array-and-struct-fields:

ARRAY and STRUCT fields
^^^^^^^^^^^^^^^^^^^^^^^

BigQuery supports fields of type `ARRAY`_ for lists of values
and fields of type `STRUCT`_ for hierarchical values.
These field types are useful for representing rich data
without duplication.

   +-------------------------------------------------------------------------+
   | Legacy SQL Nomenclature                                                 |
   +=========================================================================+
   | Prior to supporting the SQL 2011 standard, BigQuery used its own SQL    |
   | variant, now called "Legacy SQL". In Legacy SQL ARRAY and STRUCT        |
   | fields were referred to as "REPEATED" and "NESTED" fields respectively. |
   |                                                                         |
   | For more information, see the `Legacy SQL Migration Guide`_.            |
   +-------------------------------------------------------------------------+

Two of the ``variants`` fields noted above, the ``alternate_bases`` and the
``call`` field, are ARRAY fields. ARRAY fields are a feature of BigQuery
that allow for embedding multiple values of the same type into the same
field (similar to a list).

The ``alternate_bases`` field is a simple ARRAY field in that it allows
for multiple scalar STRING values.  For example:

   .. image:: analyze_variants_with_bigquery/array_fields_example.png
      :width: 85%

.. When RTD uses Sphinx 4.x, use the table below instead of the image above.
   Until then, using a proper table triggers
   https://github.com/sphinx-doc/sphinx/issues/1871

   +----------------+----------+----------+-----------------+
   + reference_name | start    | end      | alternate_bases |
   +================+==========+==========+=================+
   | chr4           | 6214126  | 6214135  | - A             |
   |                |          |          | - AACAC         |
   +----------------+----------+----------+-----------------+
   | chr9           | 16011409 | 16011412 | - C             |
   |                |          |          | - CT            |
   +----------------+----------+----------+-----------------+

The ``call`` field is a complex ARRAY field in that contains STRUCTs.
The Platinum Genomes ``call`` field contains 13 fields of its own, such as
``call_set_name``, ``genotype``, and ``FILTER``.
Some fields, such as ``genotype`` and ``FILTER``, are themselves ARRAY
fields. We will see examples of working with these fields below.

.. _variants-vs-non-variants:

Variants vs. non-variants
^^^^^^^^^^^^^^^^^^^^^^^^^

The Platinum Genomes data is gVCF_ data, meaning there are records in the
variants table for non-variant segments (also known as "reference calls").
Having the reference calls in the variants table, following the
`gVCF conventions`_, "makes it straightforward to distinguish variant,
reference and no-call states for any site of interest".

   +--------------------------------------------------------------+
   | Other variant sources, besides VCFs, can contain non-variant |
   | segments, including `Complete Genomics`_ masterVar files.    |
   +--------------------------------------------------------------+

In a ``variants`` table exported from Google Genomics, the non-variant segments
are commonly represented in one of the following ways (the representation
depends on the variant caller that generated the source data):

* With a zero-length ``alternate_bases`` value, or
* With the text string ``<NON_REF>`` as an ``alternate_bases`` value, or
* With the text string ``<*>`` as an ``alternate_bases`` value

For example:

   +----------------+-------+------+-----------------+-------------------+
   | reference_name | start |  end | reference_bases | *alternate_bases* |
   +================+=======+======+=================+===================+
   |              1 |  1000 | 1010 |               A |                   |
   +----------------+-------+------+-----------------+-------------------+

or

   +----------------+-------+------+-----------------+-------------------+
   | reference_name | start |  end | reference_bases | *alternate_bases* |
   +================+=======+======+=================+===================+
   |              1 |  1000 | 1010 |               A | - *<NON_REF>*     |
   +----------------+-------+------+-----------------+-------------------+

In this example we have a reference block of 10 bases on chromosome 1,
starting at position 1000. The reference base at position 1000 is an "A"
(the reference bases at the other positions of this block are not represented).

In the first case, the ``alternate_bases`` ARRAY field contains no values;
it is an ARRAY of length 0.
In the second case, the ``alternate_bases`` ARRAY field is length 1 containing
the literal text string ``<NON_REF>``.

   +--------------------------------------------------------------+
   | See the `VCF specification`_ for further discussion of       |
   | representing non-variant positions in the genome.            |
   +--------------------------------------------------------------+

The Platinum Genomes data represents non-variant segments with a NULL
``alternate_bases`` value, however the queries in this code lab are designed to
accommodate each of the above representations.

Table summary data
~~~~~~~~~~~~~~~~~~

Click on the "Details" button in the right hand pane of the browser window.
This will display information like:

   .. image:: analyze_variants_with_bigquery/variants_table_details.png
      :width: 75%

You can immediately see the size of this table at 46.5 GB and over 261 million
rows.

Click on the "Preview" button and you see a preview of a few records in the
table like:

   .. image:: analyze_variants_with_bigquery/variants_table_preview.png
      :width: 95%

Queries
-------
Now that you have an overview of data in the table, we will start issuing
queries and progressively add more query techniques and explanations of
the ``variants`` table data.

We will include many documentation references when introducing new concepts,
but you may find it useful to open and reference the
`Standard SQL Query Syntax`_.

How many records are in the variants table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You saw in the previous section how many variant records are in the table,
but to get your feet wet with queries, let's verify that summary data:

::

   #standardSQL
   SELECT
     COUNT(1) AS number_of_records
   FROM
     `genomics-public-data.platinum_genomes.variants`

You should see the same result as "Number of Rows" above: ``261,285,806``.

How many variant calls are in the variants table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each record in the ``variants`` table is a genomic position that is a variant
or non-variant segment, and each record has within it an ARRAY field,
which is a list of ``calls``. Each call includes the ``call_set_name``
(typically the genomic "sample id"), along with values like the genotype,
quality fields, read depth, and other fields typically found in a VCF or
`Complete Genomics`_ masterVar file.

Let's now get a summary of total number of calls across all samples.
As noted, the ``call`` field is an ARRAY field, with multiple calls
embedded in each ``variants`` record.
We *cannot* just change what we count above to count the ``call`` field:

::

   #standardSQL
   SELECT
     COUNT(call) AS number_of_calls
   FROM
     `genomics-public-data.platinum_genomes.variants`

returns the ``number_of_calls`` as 261,285,806. **Notice that this is the
same as the number of variant records. This query did NOT count the
array elements, just the number of arrays.**

We have a few choices then on how we properly count the calls.

One way is to count the total number of calls by querying over the
``variants`` records and sum the lengths of each ``call`` ARRAY.

::

   #standardSQL
   SELECT
     SUM(ARRAY_LENGTH(call)) AS number_of_records
   FROM
     `genomics-public-data.platinum_genomes.variants`

Another way is to `JOIN`_ the ``variants`` record with the ``variants.call``
field. This is similar to the `Legacy SQL FLATTEN`_ technique, which
effectively expands each call record to be a top level result joined with
its parent ``variants`` record fields.

::

   #standardSQL
   SELECT
     COUNT(call) AS number_of_calls
   FROM
     `genomics-public-data.platinum_genomes.variants` v, v.call

Note the use of the comma (,) operator, which is a short-hand notation
for ``JOIN``. Also note that the join to the ``call`` field
makes an implicit `UNNEST`_ call on the ``call`` field.

   +------------------------------------------------------------------------+
   | Code tip: UNNEST                                                       |
   +========================================================================+
   | The `UNNEST`_ function provides a mechanism to query over an ARRAY     |
   | field as though it is a table. UNNEST returns one record for each      |
   | element of an ARRAY.                                                   |
   +------------------------------------------------------------------------+

The previous query is equivalent to:

::

   #standardSQL
   SELECT
     COUNT(call) AS number_of_calls
   FROM
     `genomics-public-data.platinum_genomes.variants` v
   JOIN
      UNNEST(v.call)

The final example for counting calls extends the previous example to
demonstrate accessing one of the ``call`` fields.
Each ``call`` must have a single ``call_set_name`` and so to count them:

::

   #standardSQL
   SELECT
     COUNT(call.call_set_name) AS number_of_calls
   FROM
     `genomics-public-data.platinum_genomes.variants` v, v.call call

For each of these queries, you should get a result of ``309,551,691``,
which means that there is an average of ``1.2`` calls per variant record
in this dataset.

   +-----------------------------------------------------------------------+
   | Which query is "better"?                                              |
   +=======================================================================+
   | BigQuery pricing is based on the amount of data examined. Query       |
   | performance also improves when we can reduce the amount of data       |
   | examined. BigQuery provides empirical data which can be viewed in the |
   | web UI; always check the "Query complete (Ns elapsed, M B processed)" |
   | displayed. You may make use of the `Query Plan Explanation`_ to       |
   | optimize your queries.                                                |
   +-----------------------------------------------------------------------+

How many variants and non-variant segments are in the table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As discussed above, the Platinum Genomes data is `gVCF`_ data, and so the
variants table contains both real variants as well as non-variant segments.

Let's now run a query that filters out the non-variant segments:

::

   #standardSQL
   SELECT
     COUNT(1) AS number_of_real_variants
   FROM
     `genomics-public-data.platinum_genomes.variants` v
   WHERE
     EXISTS (SELECT 1
               FROM UNNEST(v.alternate_bases) AS alt
             WHERE
               alt NOT IN ("<NON_REF>", "<*>"))

When you issue this command, you'll observe that the number of variants
(including no-calls of variants) is ``10,982,549``. So the vast majority
of records are reference calls, which is to be expected.

What's the logic of this query? How did it filter out non-variant segments?

As noted :ref:`above <variants-vs-non-variants>`, there are (at least)
three different conventions for designating a variant record as a non-variant
segment. The WHERE clause here includes ``variant`` records where the
``alternate_bases`` field contains a value that is a true alternate
sequence (it is NOT one of the special marker values).

In the above query, for each record in the ``variants`` table, we
issue a subquery over the ``alternate_bases`` field of that
``variants`` record, returning the value 1 for each
``alternate_bases`` that is not ``<NON_REF>`` or ``<*>``.

If the subquery returns any records, the corresponding ``variants``
record is counted.

Let's turn the previous query around and get a count of the reference segments:

::

   #standardSQL
   SELECT
     COUNT(1) AS number_of_non_variants
   FROM
     `genomics-public-data.platinum_genomes.variants` v
   WHERE
     NOT EXISTS (SELECT 1
                   FROM UNNEST(v.alternate_bases) AS alt
                 WHERE
                   alt NOT IN ("<NON_REF>", "<*>"))

This command will return a count of ``250,303,257`` non-variant records.
This is good since:

::

   250,303,257 + 10,982,549 = 261,285,806 

The above WHERE clause is a literal negation of the previous query, but the
double negation (NOT EXIST ... NOT IN ...) can be a little difficult to follow.
A more direct form of this query is:

::

   #standardSQL
   SELECT
     COUNT(1) AS number_of_non_variants
   FROM
     `genomics-public-data.platinum_genomes.variants` v
   WHERE
     ARRAY_LENGTH(v.alternate_bases) = 0
     OR EXISTS (SELECT 1
                 FROM UNNEST(v.alternate_bases) AS alt
               WHERE
                 alt IN ("<NON_REF>", "<*>"))

This query directly counts the variant records which either:

  * Have an alternate_bases array length of 0, or
  * Contain an alternate_bases value of ``<NON_REF>`` or ``<*>``

This directly maps to the description of the non-variant segment representation
noted :ref:`above <variants-vs-non-variants>`. But note that there is a
subtle difference between this query and the previous that can produce
different results depending on your data.

In many datasets, ``variants`` records will be *either* variants or non-variant
segments; such records will either contain ``alternate_bases`` values
consisting only of genomic sequences *OR* will contain a single ``<NON_REF>``
or ``<*>`` value.

It is however very possible for a variant caller to produce a variant record
in a VCF with an ALT column value of ``T,<NON_REF>``. Of the previous two
queries, the first will *exclude* such records from the result, while the
second will *include* them.

What this difference makes clear is that the notion of a particular ``variants``
record being a binary "variant" *or* "non-variant" segment is dataset-
specific. One will typically want to look at more specific criteria
(the actual genotype calls of specific variants) during analysis. This is
discussed further below.

How many variants does each sample have called?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've now had a quick look at the top-level records in the ``variants`` table.
Next let's look at the child records, namely the individual samples that have
had calls made against the variants.

Each variant in the ``variants`` table will have zero or more
``call.call_set_name`` values. A given ``call.call_set_name`` will appear
in multiple ``variants`` records.

To count the number of ``variants`` records in which each ``callset`` appears:

::

   #standardSQL
   SELECT
     call.call_set_name AS call_set_name,
     COUNT(call.call_set_name) AS call_count_for_call_set
   FROM
     `genomics-public-data.platinum_genomes.variants` v, v.call
   GROUP BY
     call_set_name
   ORDER BY
     call_set_name

You should observe that there are 6 records returned.
Each ``call_set_name`` corresponds to an individual who was sequenced.

   .. image:: analyze_variants_with_bigquery/call_count_for_call_set.png
      :width: 60%
      :align: center

But humans don't typically have 50 million variants. Let's filter out
the reference segments and and just look at the "real" variant records:

::

   #standardSQL
   SELECT
     call.call_set_name AS call_set_name,
     COUNT(call.call_set_name) AS call_count_for_call_set
   FROM
     `genomics-public-data.platinum_genomes.variants` v, v.call
   WHERE
     EXISTS (SELECT 1
               FROM UNNEST(v.alternate_bases) AS alt
             WHERE
               alt NOT IN ("<NON_REF>", "<*>"))
   GROUP BY
     call_set_name
   ORDER BY
     call_set_name

Returns:

   .. image:: analyze_variants_with_bigquery/count_true_variants_per_callset.png
      :width: 60%
      :align: center

5 million variants for a human is on the right scale, but there is one
additional filter that we have missed applying to our results.

Filter "true variants" by genotype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Variants loaded into the Platinum Genomes ``variants`` table include no-calls.
A no-call is represented by a ``genotype`` value of -1. These cannot be
legitimately called "true variants" for individuals, so let's filter them out.
Many tools filter such calls if at least one of the genotypes is -1, and so
we will do the same here.

We can be even more concrete with our variant queries by only including
calls with genotypes greater than zero. If a call includes only genotypes
that are no-calls (-1) or reference (0), then they are not true variants.

The following query adds the additional filtering by genotype:

::

   #standardSQL
   SELECT
     call.call_set_name AS call_set_name,
     COUNT(call.call_set_name) AS call_count_for_call_set
   FROM
     `genomics-public-data.platinum_genomes.variants` v, v.call
   WHERE
     EXISTS (SELECT 1
               FROM UNNEST(v.alternate_bases) AS alt
             WHERE
               alt NOT IN ("<NON_REF>", "<*>"))
     AND EXISTS (SELECT 1 FROM UNNEST(call.genotype) AS gt WHERE gt > 0)
     AND NOT EXISTS (SELECT 1 FROM UNNEST(call.genotype) AS gt WHERE gt < 0)
   GROUP BY
     call_set_name
   ORDER BY
     call_set_name

Returns:

   .. image:: analyze_variants_with_bigquery/count_true_variants_per_callset_2.png
      :width: 60%
      :align: center

Is the non-variant segment filter actually needed here?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The above query filtered out:

* non-variant segments
* calls for which all ``genotype`` values are 0 and/or -1

There is some redundancy in this filter. All ``call.genotype`` values for
non-variant segments in this dataset are either 0, or -1.
Thus the above query could safely be rewritten without the filter on
``alternate_bases``.

::

   #standardSQL
   SELECT
     call.call_set_name AS call_set_name,
     COUNT(call.call_set_name) AS call_count_for_call_set
   FROM
     `genomics-public-data.platinum_genomes.variants` v, v.call
   WHERE
     EXISTS (SELECT 1 FROM UNNEST(call.genotype) AS gt WHERE gt > 0)
     AND NOT EXISTS (SELECT 1 FROM UNNEST(call.genotype) AS gt WHERE gt < 0)
   GROUP BY
     call_set_name
   ORDER BY
     call_set_name

The previous form of this query may be preferred as it
makes the semantic intent of more clear (only query over
"true variant" records).

However as queries become larger and more complicated, removing
well-known redundancies can make your queries more readable and can also
make them less expensive. BigQuery costs are based on the number of bytes
processed. The second form of the query does not need to examine the
``alternate_bases`` column.

How many samples are in the variants table?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the previous few queries, we observed that there are 6 distinct
``call_set_name`` values in the ``variants`` table as each query returned 6
rows. But what if we were interested in specifically returning that count?

One way to do this is to take our existing query and treat it like a table
over which we can query. In this example, we take the previous queries and
first collapse it down to the minimum results needed - just the list of
call set names:

::

   #standardSQL
   SELECT call.call_set_name
   FROM `genomics-public-data.platinum_genomes.variants` v, v.call
   GROUP BY call.call_set_name)

then we compose a query using the SQL `WITH clause`_.

::

   #standardSQL
   WITH call_sets AS (
     SELECT call.call_set_name
     FROM `genomics-public-data.platinum_genomes.variants` v, v.call
     GROUP BY call.call_set_name)

   SELECT
     COUNT(1) AS number_of_callsets
   FROM
     call_sets

This composition query pattern is frequently useful and is shown here as
an example.

Composition turns out to be unnecessary for this particular query.
We can get the count of distinct ``call_set_name`` values an easier way:

::

   #standardSQL
   SELECT
     COUNT(DISTINCT call.call_set_name) AS number_of_callsets
   FROM
     `genomics-public-data.platinum_genomes.variants` v,  v.call

How many variants are there per chromosome
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've had a look at the number of variants per callset. What if we want
to look at the number of variants per chromosome. Given our experience
with ``GROUP BY`` and ``COUNT`` from the previous section, this should
be fairly straight-forward. We just need to apply these same tools to
the ``reference_name`` field.

It turns out that there are some wrinkles to contend with.  
The query that we want is:

  - Return all ``variants`` records in which there is

    - at least one call with

      - at least one genotype greater than 0

  - Group the variant records by chromosome and count each group

The first wrinkle is that we need to look into an ARRAY (genotype)
within an ARRAY (call) while keeping execution context of the query
at the ``variants`` record level. We are not interested in producing
a per-call or per-genotype result. We are interested in producing
a per-variant result.

We saw above how to "look into" an ARRAY record, without changing the query
context, we can use the `UNNEST`_ function in an EXISTS subquery in our
WHERE clause:

::

   #standardSQL
   SELECT
     reference_name,
     COUNT(reference_name) AS number_of_variant_records
   FROM
     `genomics-public-data.platinum_genomes.variants` v
   WHERE
     EXISTS (SELECT 1
               FROM UNNEST(v.call) AS call
             WHERE EXISTS (SELECT 1
                             FROM UNNEST(call.genotype) AS gt
                           WHERE gt > 0))
   GROUP BY
     reference_name
   ORDER BY
     reference_name

Returns:

   .. image:: analyze_variants_with_bigquery/true_variants_by_chromosome_1.png
      :width: 60%
      :align: center

The above encodes very explicitly our needed logic. We can make this a
bit more concise by turning the EXISTS clause into a JOIN of the ``call``
field with the ``call.genotype`` field:

::

   #standardSQL
   SELECT
     reference_name,
     COUNT(reference_name) AS number_of_variant_records
   FROM
     `genomics-public-data.platinum_genomes.variants` v
   WHERE
     EXISTS (SELECT 1
               FROM UNNEST(v.call) AS call, UNNEST(call.genotype) AS gt
             WHERE gt > 0)
   GROUP BY
     reference_name
   ORDER BY
     reference_name


The above is good and the results are correct, but let's work on improving
our output. Our second wrinkle arises as we'd like to sort the output in
chromosome-numeric order but the field we are sorting on is a STRING and
the values contain the prefix "chr".

Let's walk through a few steps to demonstrate some BigQuery technique.

To sort numerically, we should first trim out the "chr" from the
``reference_name`` field:

::

   #standardSQL
   SELECT
     REGEXP_REPLACE(reference_name, '^chr', '') AS chromosome,
     COUNT(reference_name) AS number_of_variant_records
   FROM
     `genomics-public-data.platinum_genomes.variants` v
   WHERE
     EXISTS (SELECT 1
               FROM UNNEST(v.call) AS call, UNNEST(call.genotype) AS gt
             WHERE gt > 0)
   GROUP BY
     chromosome
   ORDER BY
     chromosome

What did we do here? First we used the `REGEXP_REPLACE`_
function to replace the leading "chr" string with an with an empty string
(and gave the result a column alias of ``chromosome``).
Then we changed the ``GROUP BY`` and ``ORDER BY`` to use the computed
``chromosome`` field. But the ordering isn't quite what we wanted:

   .. image:: analyze_variants_with_bigquery/true_variants_by_chromosome_remove_chr.png
      :width: 60%
      :align: center

The order is still string rather than numeric ordering. Let's try to
cast the column to an integer:

::

   #standardSQL
   SELECT
     CAST(REGEXP_REPLACE(reference_name, '^chr', '') AS INT64) AS chromosome,
     COUNT(reference_name) AS number_of_variant_records
   FROM
     `genomics-public-data.platinum_genomes.variants` v
   WHERE
     EXISTS (SELECT 1
               FROM UNNEST(v.call) AS call, UNNEST(call.genotype) AS gt
             WHERE gt > 0)
   GROUP BY
     chromosome
   ORDER BY
     chromosome

Unfortunately this generates an error:

   +------------------------------+
   | Error: Bad int64 value: X    |
   +------------------------------+

Not all chromosome names are numeric, namely X, Y, and M.
This makes it challenging to order as desired.
Let's approach this slightly differently and use
string sorting. To get the desired order, we will prepend a "0" to
chromosomes 1-9:

::

   #standardSQL
   SELECT
     CASE
       WHEN SAFE_CAST(REGEXP_REPLACE(reference_name, '^chr', '') AS INT64) < 10
         THEN CONCAT('0', REGEXP_REPLACE(reference_name, '^chr', ''))
         ELSE REGEXP_REPLACE(reference_name, '^chr', '')
     END AS chromosome,
     COUNT(reference_name) AS number_of_variant_records
   FROM
     `genomics-public-data.platinum_genomes.variants` v
   WHERE
     EXISTS (SELECT 1
               FROM UNNEST(v.call) AS call, UNNEST(call.genotype) AS gt
             WHERE gt > 0)
   GROUP BY
     chromosome
   ORDER BY
     chromosome

This looks better:

   .. image:: analyze_variants_with_bigquery/true_variants_by_chromome_pad_with_0.png
      :width: 60%
      :align: center

What did we do? We used the highly flexible `CASE function`_ to prepend a
"0" to all chromosomes numbered less than 10, and only removed the "chr"
from the remaining ``reference_name`` values.

Also notice the use of the `SAFE_CAST`_ function. This will return NULL
for X, Y, and M instead of raising an error.

As a final improvement on the output of the above query, let's display the
``reference_name`` unchanged while still getting the sort ordering we want.
All we need to do is move our ``CASE`` clause to the ``ORDER BY``:

::

   #standardSQL
   SELECT
     reference_name,
     COUNT(reference_name) AS number_of_variant_records
   FROM
     `genomics-public-data.platinum_genomes.variants` v
   WHERE
     EXISTS (SELECT 1
               FROM UNNEST(v.call) AS call, UNNEST(call.genotype) AS gt
             WHERE gt > 0)
   GROUP BY
     reference_name
   ORDER BY
     CASE
       WHEN SAFE_CAST(REGEXP_REPLACE(reference_name, '^chr', '') AS INT64) < 10
         THEN CONCAT('0', REGEXP_REPLACE(reference_name, '^chr', ''))
         ELSE REGEXP_REPLACE(reference_name, '^chr', '')
     END

Result:

   .. image:: analyze_variants_with_bigquery/true_variants_by_chromome_final.png
      :width: 60%
      :align: center

User Defined Functions
~~~~~~~~~~~~~~~~~~~~~~

We were able to embed some fairly interesting logic into our query with
the CASE statement. But doing so made the query more verbose. As you build
more complex queries, keeping the queries concise becomes more and more
important to make it easier to ensure their logic is correct.

Let's use one last bit of BigQuery technique to improve on our query:
`User Defined Functions`_. UDFs can be defined as SQL expressions or
as JavaScript.

In our first example, we will simply move the ``CASE`` logic from our previous
query into a function:

::

   #standardSQL
   CREATE TEMPORARY FUNCTION SortableChromosome(reference_name STRING)
     RETURNS STRING AS (
     -- Remove the leading "chr" (if any) in the reference_name
     -- If the chromosome is 1 - 9, prepend a "0" since
     -- "2" sorts after "10", but "02" sorts before "10".
     CASE
       WHEN SAFE_CAST(REGEXP_REPLACE(reference_name, '^chr', '') AS INT64) < 10
         THEN CONCAT('0', REGEXP_REPLACE(reference_name, '^chr', ''))
         ELSE REGEXP_REPLACE(reference_name, '^chr', '')
     END
   );

   SELECT
     reference_name,
     COUNT(reference_name) AS number_of_variant_records
   FROM
     `genomics-public-data.platinum_genomes.variants` v
   WHERE
     EXISTS (SELECT 1
               FROM UNNEST(v.call) AS call, UNNEST(call.genotype) AS gt
             WHERE gt > 0)
   GROUP BY
     reference_name
   ORDER BY SortableChromosome(reference_name)

In the second example, we use a function defined in JavaScript:

::

   #standardSQL
   CREATE TEMPORARY FUNCTION SortableChromosome(reference_name STRING)
     RETURNS STRING LANGUAGE js AS """
     // Remove the leading "chr" (if any) in the reference_name
     var chr = reference_name.replace(/^chr/, '');
     
     // If the chromosome is 1 - 9, prepend a "0" since
     // "2" sorts after "10", but "02" sorts before "10".
     if (chr.length == 1 && '123456789'.indexOf(chr) >= 0) {
       return '0' + chr;
     }
     
     return chr;
   """;
   
   SELECT
     reference_name,
     COUNT(reference_name) AS number_of_variant_records
   FROM
     `genomics-public-data.platinum_genomes.variants` v
   WHERE
     EXISTS (SELECT 1
               FROM UNNEST(v.call) AS call, UNNEST(call.genotype) AS gt
             WHERE gt > 0)
   GROUP BY
     reference_name
   ORDER BY SortableChromosome(reference_name)

Each of these two queries returns the same as our previous query, but the
logic of the query is more concise.

How many high-quality variants per-sample
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `VCF specification`_ describes the ``FILTER`` field which can be used
to label variant calls of different qualities. Let's take a look at the
per-call ``FILTER`` values for the Platinum Genomes dataset:

::

   #standardSQL
   SELECT
     call_filter,
     COUNT(call_filter) AS number_of_calls
   FROM
     `genomics-public-data.platinum_genomes.variants` v,
     v.call,
     UNNEST(call.FILTER) AS call_filter
   GROUP BY
     call_filter
   ORDER BY
     number_of_calls

Returns:

   .. image:: analyze_variants_with_bigquery/FILTER_count.png
      :width: 60%
      :align: center

Calls with multiple FILTER values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The values for the ``number_of_calls`` seem high based on the total number
of calls. Let's sum up all of the FILTER values:

::

   #standardSQL
   SELECT
     COUNT(call_filter) AS number_of_filters
   FROM
     `genomics-public-data.platinum_genomes.variants` v,
     v.call,
     call.FILTER AS call_filter

The returned result is ``327,580,807``, which is higher than the total
number of calls we computed earlier (``309,551,691``). So what is going
on here? Is our query faulty?

No. The ``FILTER`` field is an ARRAY field within each ``call`` field,
so some ``call`` fields have multiple ``FILTER`` values. Let's concatenate
the FILTER field values while looking at a few variant calls.

::

   #standardSQL
   SELECT
     reference_name,
     start,
     `end`,
     reference_bases,
     call.call_set_name AS call_set_name,
     (SELECT STRING_AGG(call_filter) FROM UNNEST(call.FILTER) AS call_filter) AS filters,
     ARRAY_LENGTH(call.FILTER) AS filter_count
   FROM
     `genomics-public-data.platinum_genomes.variants` v, v.call
   WHERE
     ARRAY_LENGTH(call.FILTER) > 1
   ORDER BY
     filter_count DESC, reference_name, start, `end`, reference_bases, call_set_name
   LIMIT
     10

Returns:

   .. image:: analyze_variants_with_bigquery/calls_with_multiple_FILTER_values.png
      :width: 95%
      :align: center

So we can see that some variant calls of low quality will fail to pass
multiple filters.

FILTERing for high quality variant records
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the count of ``FILTER`` values above, we can see that the vast majority
of variant calls have been marked with the ``PASS`` label, indicating that
they are high quality calls that have passed all variant calling filters.

When analyzing variants, you will often want to filter out lower quality
variants. It is expected that if the ``FILTER`` field contains the value
``PASS``, it will contain no other values. Let's verify that by adding one
new condition to the WHERE clause of the previous query:

::

   #standardSQL
   SELECT
     reference_name,
     start,
     `end`,
     reference_bases,
     call.call_set_name AS call_set_name,
     (SELECT STRING_AGG(call_filter) FROM UNNEST(call.FILTER) AS call_filter) AS filters,
     ARRAY_LENGTH(call.FILTER) AS filter_count
   FROM
     `genomics-public-data.platinum_genomes.variants` v, v.call
   WHERE
     EXISTS (SELECT 1 FROM UNNEST(call.FILTER) AS call_filter WHERE call_filter = 'PASS')
     AND ARRAY_LENGTH(call.FILTER) > 1
   ORDER BY
     filter_count DESC, reference_name, start, `end`, reference_bases, call_set_name
   LIMIT
     10

The result is:

   +------------------------------+
   | Query returned zero records. |
   +------------------------------+

This query omitted any call that did not contain a ``PASS`` value for
``FILTER``, and only returned calls for which there was more than 1
``FILTER`` value.

Count high quality calls for samples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All high quality calls for each sample
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following counts all calls (variants and non-variants) for each call set
omitting any call with a non-`PASS` filter.

::

   #standardSQL
   SELECT
     call.call_set_name AS call_set_name,
     COUNT(1) AS number_of_calls
   FROM
     `genomics-public-data.platinum_genomes.variants` v, v.call
   WHERE
     NOT EXISTS (SELECT 1 FROM UNNEST(call.FILTER) AS call_filter WHERE call_filter != 'PASS')
   GROUP BY
     call_set_name
   ORDER BY
     call_set_name

Returns:

   .. image:: analyze_variants_with_bigquery/count_high_quality_calls_per_sample.png
      :width: 60%
      :align: center

All high quality true variant calls for each sample
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following counts all calls (variants and non-variants) for each call set
omitting any call with a non-`PASS` filter and including only calls with at
least one true variant (genotype > 0).

::

   #standardSQL
   SELECT
     call.call_set_name AS call_set_name,
     COUNT(1) AS number_of_calls
   FROM
     `genomics-public-data.platinum_genomes.variants` v, v.call
   WHERE
     NOT EXISTS (SELECT 1 FROM UNNEST(call.FILTER) AS call_filter WHERE call_filter != 'PASS')
     AND EXISTS (SELECT 1 FROM UNNEST(call.genotype) as gt WHERE gt > 0)
   GROUP BY
     call_set_name
   ORDER BY
     call_set_name

Returns:
   .. image:: analyze_variants_with_bigquery/count_high_quality_variant_calls.png
      :width: 60%
      :align: center

Where to go next
----------------

The Google Genomics team and the community have contributed many data
analysis examples and tools that build on the concepts you have learned here.

To find more sample queries and methods of accessing a ``variants`` table
in BigQuery see:

* https://github.com/googlegenomics/getting-started-bigquery
* https://github.com/googlegenomics/bigquery-examples
* https://github.com/googlegenomics/codelabs
* :doc:`/use_cases/discover_public_data/tute_genomics_public_data`
* :doc:`/use_cases/analyze_variants/index`

