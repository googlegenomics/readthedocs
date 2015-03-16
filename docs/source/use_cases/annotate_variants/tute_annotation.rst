Annotate Variants with Tute Genomics
====================================

.. toctree::
   :maxdepth: 2

Tute Genomics has made available to the community annotations for all hg19 SNPs as a BigQuery table.

See `Tute's documentation`_ for more details about the annotation databases included and sample queries upon public data.

.. _Tute's documentation: https://docs.google.com/document/d/1_Kryc4qAqw1NRezaqDJ1tXUSCbxEkKK4SSi_kZuyHtU/pub

To make use of this upon your own data:

(1) :doc:`../load_data/index`
(2) Use the BigQuery JOIN command to join the Tute table with your variants and materialize the result to a new table.

TODO: actual example with bq tool



