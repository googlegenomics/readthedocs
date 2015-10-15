.. _FROM clause: https://cloud.google.com/bigquery/query-reference#from
.. _WHERE clause: https://cloud.google.com/bigquery/query-reference#where
.. _HAVING clause: https://cloud.google.com/bigquery/query-reference#having
.. _REGEXP_REPLACE: https://cloud.google.com/bigquery/query-reference#regularexpressionfunctions
.. _CASE function: https://cloud.google.com/bigquery/query-reference#otherfunctions
.. _GROUP_CONCAT function: https://cloud.google.com/bigquery/query-reference#aggfunctions
.. _COUNT function: https://cloud.google.com/bigquery/query-reference#aggfunctions
.. _WITHIN keyword: https://cloud.google.com/bigquery/query-reference#scopedaggregation

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

The purpose of this lab is to help you:

* learn how to use the Google BigQuery query tool
* learn valuable BigQuery SQL syntax
* become familiar with the variants table created by a Google Genomics variant export

BigQuery uses thousands of machines in parallel to process your queries.
This means you can use it to interact with genomic data in an ad-hoc fashion.
Queries that on traditional systems take hours to run (as batch jobs) can
instead be processed in seconds with BigQuery.

This lab focuses on genomic variant data that has been exported from Google
Genomics to BigQuery. The dataset used is from the public
`Illumina Platinum Genomes project data`_ (17 samples). You may run the same
queries against other datasets exported from Google Genomics, including the
`1000 Genomes project data`_.
All output below is for queries against the Platinum Genomes.

Here are some of the questions you'll answer in this lab about the variant data:

* How many records are in the variants table
* How many variant calls are in the variants table
* How many variants are called for each sample
* How many non-variants are called for each sample
* How many samples are in the variants table
* How many variants are there per chromosome
* How many high-quality variants per-sample

Here are some of the technical skills you will learn:

* How to get an overview of the data in your table
* How are non-variant segments represented in the variants table
* How are variant calls represented in the variants table
* How are variant call quality filters represented in the variants table
* How to handle nested fields in variants data
* How to count distinct records
* How to group records
* How to construct queries using subqueries

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
this lab to be billed against is selected. If it is not, then click on the
down-arrow icon, select "Switch to Project" and then select the correct
project.

Add the Genomics public data project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We could immediately start composing queries against any BigQuery data you
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
BigQuery datasets. Select the ``genomics-public-data:platinum_genomes``.
Click on the ``variants`` table, which should appear in the drop-down.

When you have selected the table from the drop-down, you should now see the
table schema in the right-hand pane:

   .. image:: analyze_variants_with_bigquery/variants_table_schema.png
      :width: 95%

The key fields of the variants table that will be frequently referenced
in this lab are:

  reference_name
    The reference on which this variant occurs. (such as "chr20" or "X")
  
  start
    The position at which this variant occurs (0-based). This corresponds to
    the first base of the string of reference bases.
  
  end
    The end position (0-based) of this variant. This corresponds to the
    first base after the last base in the reference allele. So, the length
    of the reference allele is (end - start).
  
  reference_bases
    The reference bases for this variant. They start at the given position.
  
  alternate_bases
    The bases that appear instead of the reference bases.

and

  call
    The variant calls for this particular variant.

The first set of fields are what makes a ``variant`` record unique.

The ``call`` field contains a list of the calls for the ``variant`` record.
The ``call`` field is a REPEATED field which contains NESTED fields
(REPEATED and NESTED fields are discussed further
:ref:`below <repeated-and-nested-fields>`).

The fixed NESTED fields of the call field are:

  call.call_set_id
    Unique identifier generated by Google Genomics to identify a callset.

  call.call_set_name
    Unique identifier supplied on input to Google Genomics for a callset.
    This is also typically known as the sample identifier.

  genotype
    Repeated field containing the numeric genotype encodings for this call.
    Values:

    * -1: no call
    *  0: reference
    *  1: first alternate_bases value
    *  2: second alternate_bases value
    *  ...
    *  n: nth alternate_bases value

  genotype_likelihood
    Repeated field containing the likelihood value for each corresponding
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
`here <https://cloud.google.com/genomics/v1/load-variants>`_ on
`cloud.google.com/genomics <https://cloud.google.com/genomics>`_.

More on the Google Genomics variant representation can be found
`here <https://cloud.google.com/genomics/reference/rest/v1/variants>`_
`cloud.google.com/genomics <https://cloud.google.com/genomics>`_.

More on the origin of the data can be found
`here <http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/platinum_genomes.html>`_ on
`googlegenomics.readthedocs.org <http://googlegenomics.readthedocs.org>`_.

.. _repeated-and-nested-fields:

REPEATED and NESTED fields
^^^^^^^^^^^^^^^^^^^^^^^^^^

BigQuery supports REPEATED fields for lists of values and NESTED fields for
hierarchical values. These field types are useful for representing rich data
without duplication.

Two of the fields noted above, the ``alternate_bases`` and the ``call``
field, are REPEATED fields.  REPEATED fields are a feature of BigQuery
that allow for embedding multiple values of the same type into the same
field (similar to a list). 

The ``alternate_bases`` field is a simple REPEATED field in that it allows
for multiple scalar STRING values. Examples:

   +----------------+----------+----------+-----------------+
   + reference_name | start    | end      | alternate_bases |
   +================+==========+==========+=================+
   | chr4           | 6214126  | 6214135  | - A             |
   |                |          |          | - AACAC         |
   +----------------+----------+----------+-----------------+
   | chr9           | 16011409 | 16011412 | - C             |
   |                |          |          | - CT            |
   +----------------+----------+----------+-----------------+

The ``call`` field is a complex REPEATED field in that it contains
NESTED fields (making it a hierarchical field).
The ``call`` field contains 14 nested fields, such as ``call_set_name``,
``genotype``, and ``FILTER``. Some fields, such as ``genotype`` and
``FILTER``, are themselves REPEATED fields. We will see examples of
working with these fields below.

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
are commonly represented in one of two ways (the representation depends on
the variant caller that generated the source data):

* With a NULL ``alternate_bases`` value, or
* With the text string '<NON_REF>' as the ``alternate_bases`` value

For example:

   +----------------+-------+------+-----------------+-------------------+
   | reference_name | start |  end | reference_bases | *alternate_bases* |
   +================+=======+======+=================+===================+
   |              1 |  1000 | 1010 |               A |       *<NON_REF>* |
   +----------------+-------+------+-----------------+-------------------+

or

   +----------------+-------+------+-----------------+-------------------+
   | reference_name | start |  end | reference_bases | *alternate_bases* |
   +================+=======+======+=================+===================+
   |              1 |  1000 | 1010 |               A |          *[NULL]* |
   +----------------+-------+------+-----------------+-------------------+

In this example we have a reference block of 10 bases on chromosome 1,
starting at position 1000. The reference base at position 1000 is an "A"
(the reference bases at the other positions of this block are not represented).

The Platinum Genomes data represents non-variant segments with a NULL
``alternate_bases`` value, however the queries in this lab are designed to
accommodate either representation.

Table summary data
~~~~~~~~~~~~~~~~~~

Click on the "Details" button on the right hand side of the browser window.
This will display information like:

   .. image:: analyze_variants_with_bigquery/variants_table_info.png
      :width: 95%

You can immediately see the size of this table at 103 GB and over 688 million
rows, and you see a preview of a few records in the table.

Queries
-------
Now that you have an overview of data in the table, we will start issuing
queries and progressively add more query techniques and explanations of
the ``variant`` table data.

We will include many documentation references when introducing new concepts,
but you may find it useful to open the `Google BigQuery query reference`_.

How many records are in the variants table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You saw in the previous section how many variant records are in the table,
but to get your feet wet with queries, let's verify that summary data:

::

   SELECT COUNT(1) AS number_of_records
   FROM [genomics-public-data:platinum_genomes.variants]

You should see the same result as "Number of Rows" above: ``688,167,235``.

   +-----------------------------------------------------------------------+
   | Code tip: COUNT(1) vs. COUNT(*) vs. COUNT(<field>)                    |
   +=======================================================================+
   | When counting records in a BigQuery table, you will want to take care |
   | when selecting whether to use the syntax "``COUNT(1)``",              |
   | "``COUNT(*)``" or "``COUNT(<field>)``".                               |
   |                                                                       |
   | Be aware that ``COUNT(NULL)`` returns ``0``. If you use the syntax    |
   | ``COUNT(<field>)``, then this can be a problem if that field contains |
   | ``NULL`` values that you wish to count.                               |
   |                                                                       |
   | When counting top-level non-repeated fields, ``COUNT(*)`` or          |
   | ``COUNT(1)`` is typically a better choice than ``COUNT(<field>)``     |
   | since ``COUNT(<field>)`` will return ``0`` for ``NULL`` values.       |
   |                                                                       |
   | When counting REPEATED fields, use ``COUNT(<field>)``. If you want to |
   | count ``NULL`` values in a repeated field, use                        |
   | ``COUNT(IFNULL(<field>, ''))``.                                       |
   +-----------------------------------------------------------------------+

How many variant calls are in the variants table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each record in the ``variant`` table is a genomic position that is a variant
or non-variant segment, and each record has within it a "repeated field",
which is list of ``calls``. Each call includes the ``call_set_name``
(typically the genomic "sample id"), along with values like the genotype,
quality fields, read depth, and other fields typically found in a VCF or
`Complete Genomics`_ masterVar file.

Let's now get a summary of total number of calls. As noted, the ``call``
field is a REPEATED field, with multiple calls embedded in each ``variant``
record. We cannot count the instances of the call field directly:

::

   SELECT COUNT(call) AS number_of_calls
   FROM [genomics-public-data:platinum_genomes.variants]

returns:

::

   Error: Field call is not a leaf field.

We have a few choices then on how we count the calls. To directly count
the instances of the ``call`` field, we are going to instruct BigQuery
to `flatten <https://cloud.google.com/bigquery/docs/data#nested>`_ the
table as it processes it (removing one level of nesting). This tells
BigQuery to treat each ``call`` as though it were a top-level record.

::

   SELECT COUNT(1) AS number_of_calls
   FROM (FLATTEN([genomics-public-data:platinum_genomes.variants], call))

or we can use the knowledge that each call field must have a single
``call_set_name``:

::

   SELECT COUNT(call.call_set_name) AS number_of_calls
   FROM [genomics-public-data:platinum_genomes.variants]

For both of these queries, you should get a result of ``887,457,596``,
which means that there is an average of ``1.3`` calls per variant record
in this dataset.

   +-----------------------------------------------------------------------+
   | Code tip: Don't FLATTEN on call                                       |
   +=======================================================================+
   | Explicit flattening of the ``call`` field significantly expands the   |
   | number of records for BigQuery to process, and is typically           |
   | unnecessary. A better pattern that is often effective is to use one   |
   | (inner) query to reduce the data set and an outer query to aggregate  |
   | over the inner query results. An example will be shown                |
   | :ref:`below <inner-outer-query-example>`).                            |
   +-----------------------------------------------------------------------+

How many variants and non-variant segments are in the table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As discussed above, the Platinum Genomes data is `gVCF`_ data, and so the
variants table contains both real variants as well as non-variant segments.

Let's now run a query that filters out the non-variant segments:

::

   SELECT COUNT(1) AS number_of_real_variants
   FROM [genomics-public-data:platinum_genomes.variants]
   OMIT RECORD IF
     EVERY(alternate_bases == '<NON_REF>') OR
     EVERY(alternate_bases IS NULL)

When you issue this command, you'll observe that the number of variants
(including no-calls of variants) is ``12,379,576``. So the vast majority
of records are reference calls, which is to be expected.

   +-----------------------------------------------------------------------+
   | Code tip: OMIT IF                                                     |
   +=======================================================================+
   | BigQuery provides three different filtering clauses for queries:      |
   |                                                                       |
   | - WHERE                                                               |
   | - OMIT IF                                                             |
   | - HAVING                                                              |
   |                                                                       |
   | The HAVING clause can be applied to aggregate fields of a query.      |
   | HAVING will be discussed in more detail below.                        |
   |                                                                       |
   | For filtering prior to aggregation, BigQuery's WHERE is analogous to  |
   | the traditional SQL "WHERE" clause applied to records. OMIT IF        |
   | provides additional functionality not provided by WHERE.              |
   | According to the the Query Reference:                                 |
   |                                                                       |
   |   `whereas the WHERE clause filters only the entire top-level`        |
   |   `record, the OMIT IF clause can exclude an individual element`      |
   |   `in a repeated field`                                               |
   |                                                                       |
   | This ability to filter on individual elements in a repeated field is  |
   | critical for working with records in the ``variants`` table as it     |
   | contains 11 repeated fields.                                          |
   +-----------------------------------------------------------------------+

Let's turn the previous query around and get a count of the reference segments:

::

   SELECT COUNT(1) AS number_of_non_variants
   FROM [genomics-public-data:platinum_genomes.variants]
   OMIT RECORD IF NOT
     (EVERY(alternate_bases IS NULL) OR
      EVERY(alternate_bases == '<NON_REF>'))

This command will return a count of ``675,787,659`` non-variant records.
This is good since:

::

   675,787,659 + 12,379,576 = 688,167,235

How many variants does each sample have called?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've now had a quick look at the top-level records in the ``variants`` table.
Next let's look at the child records, namely the individual samples that have
had calls made against the variants.

Each variant in the ``variants`` table will have one or more
``call.call_set_name`` values. A given ``call.call_set_name`` will appear
in multiple ``variant`` records.

To count the number of ``variant`` records in which each ``callset`` appears:

::

   SELECT call.call_set_name AS call_set_name,
          COUNT(call.call_set_name) AS call_count_for_call_set
   FROM [genomics-public-data:platinum_genomes.variants]
   GROUP BY call_set_name
   ORDER BY call_set_name

You should observe that there are 17 records returned.
Each ``call_set_name`` corresponds to an individual who was sequenced.

   .. image:: analyze_variants_with_bigquery/call_count_for_call_set.png
      :width: 60%
      :align: center

But humans don't typically have 50 million variants. Recall that the
``variants`` table contains reference calls as well, so let's filter
those out and just look at the non-reference segments, the "real"
variant records:

::

   SELECT call.call_set_name AS call_set_name,
          COUNT(call.call_set_name) AS call_count_for_call_set
   FROM [genomics-public-data:platinum_genomes.variants]
   OMIT RECORD IF
     EVERY(alternate_bases == '<NON_REF>') OR
     EVERY(alternate_bases IS NULL)
   GROUP BY call_set_name
   ORDER BY call_set_name

Returns:

   .. image:: analyze_variants_with_bigquery/count_true_variants_per_callset.png
      :width: 60%
      :align: center

5 million variants for a human is on the right scale, but there is one
additional filter that we missed applying to our results.

.. _inner-outer-query-example:

Filter "true variants" by genotype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Variants that were loaded into this table include "no-calls" with a
``genotype`` field value of ``-1``. These cannot be legitimately called
"true variants", so let's filter them out too.
