Personal Genome Project Data
============================

.. toctree::
   :maxdepth: 3

.. contents::

.. include:: ../../pgp-data.rst

Google Genomics PGP Dataset
---------------------------

Google Genomics variant set id for dataset ``pgp_20150205``: `9170389916365079788 <https://developers.google.com/apis-explorer/#p/genomics/v1beta2/genomics.datasets.get?datasetId=9170389916365079788>`_

This variant set contains the Complete Genomics datasets from:

* `gs://pgp-harvard-data-public/**/masterVar*bz2 <https://console.developers.google.com/storage/pgp-harvard-data-public>`_
* a few additional PGP Complete Genomics genomes
* and one PGP variants-only Illumina genome

BigQuery PGP Tables
-------------------

Variant set ``pgp_20150205`` was exported to BigQuery tables:

 (1) `google.com:biggene:pgp_20150205.variants <https://bigquery.cloud.google.com/table/google.com:biggene:pgp_20150205.variants>`_
 (2) `google.com:biggene:pgp_20150205.variants_cgi_only <https://bigquery.cloud.google.com/table/google.com:biggene:pgp_20150205.variants_cgi_only>`_ where the export excluded the single variants-only Illumina genome


