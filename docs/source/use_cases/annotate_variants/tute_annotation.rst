Annotate Variants with Tute Genomics
====================================

.. toctree::
   :maxdepth: 2

.. include:: /includes/tute_data.rst

To make use of this upon your own data:

(1) First, load your data into Google Genomics and export your variants to BigQuery.  See :doc:`../load_data/index` for more detail as to how to do this.
(2) Use the BigQuery `JOIN <https://cloud.google.com/bigquery/query-reference#joins>`_ command to join the Tute table with your variants and materialize the result to a new table.  Notice in the screenshot below the destination table and 'Allow Large Results' is unchecked.

.. image:: TuteAnnotation.png


