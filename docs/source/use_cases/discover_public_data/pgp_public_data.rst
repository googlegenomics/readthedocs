Personal Genome Project Data
============================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/pgp_public_data.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

This dataset comprises roughly 180 Complete Genomics genomes.  See the `Personal Genome Project`_ and the publication for full details:

|  `A public resource facilitating clinical use of genomes <http://www.ncbi.nlm.nih.gov/pubmed/22797899>`_
|  Ball MP1, Thakuria JV, Zaranek AW, Clegg T, Rosenbaum AM, Wu X, Angrist M, Bhak J, Bobe J, Callow MJ, Cano C, Chou MF, Chung WK, Douglas SM, Estep PW, Gore A, Hulick P, Labarga A, Lee JH, Lunshof JE, Kim BC, Kim JI, Li Z, Murray MF, Nilsen GB, Peters BA, Raman AM, Rienhoff HY, Robasky K, Wheeler MT, Vandewege W, Vorhaus DB, Yang JL, Yang L, Aach J, Ashley EA, Drmanac R, Kim SJ, Li JB, Peshkin L, Seidman CE, Seo JS, Zhang K, Rehm HL, Church GM.
|  Published: July 24, 2012
|  DOI: 10.1073/pnas.1201904109
|

Google Cloud Platform data locations
------------------------------------

* Google Cloud Storage folder `gs://pgp-harvard-data-public <https://console.developers.google.com/storage/pgp-harvard-data-public>`_
* Google Genomics Dataset ID `9170389916365079788 <https://developers.google.com/apis-explorer/#p/genomics/v1beta2/genomics.datasets.get?datasetId=9170389916365079788>`_
* Google BigQuery Dataset IDs
   * `google.com:biggene:pgp_20150205.variants <https://bigquery.cloud.google.com/table/google.com:biggene:pgp_20150205.variants>`_
   * `google.com:biggene:pgp_20150205.variants_cgi_only <https://bigquery.cloud.google.com/table/google.com:biggene:pgp_20150205.variants_cgi_only>`_ where the export excluded the single variants-only Illumina genome

Provenance
----------

Google Genomics variant set for dataset ``pgp_20150205``: `9170389916365079788 <https://developers.google.com/apis-explorer/#p/genomics/v1beta2/genomics.datasets.get?datasetId=9170389916365079788>`_ contains:

* the Complete Genomics datasets from `gs://pgp-harvard-data-public/**/masterVar*bz2 <https://console.developers.google.com/storage/pgp-harvard-data-public>`_
* a few additional `PGP`_ Complete Genomics genomes
* and one `PGP`_ variants-only Illumina genome

Appendix
--------
.. include:: /pgp-data.rst

