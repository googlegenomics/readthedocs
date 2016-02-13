Tute Genomics Annotation
========================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/annotate_variants/tute_annotation.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

.. toctree::
   :maxdepth: 2

.. include:: /includes/tute_data.rst

To make use of this upon your own data:

(1) First, load your data into Google Genomics and export your variants to BigQuery.  See `Load Genomic Variants`_ for more detail as to how to do this.
(2) Copy and modify one of the queries in `Tute's documentation`_ so that it will perform a `JOIN <https://cloud.google.com/bigquery/query-reference#joins>`_ command against your table.
(3) Run the revised query with BigQuery to join the Tute table with your variants and materialize the result to a new table.  Notice in the screenshot below the destination table and 'Allow Large Results' is checked.

.. image:: TuteAnnotation.png


