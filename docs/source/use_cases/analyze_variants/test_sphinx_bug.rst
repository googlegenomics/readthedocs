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
