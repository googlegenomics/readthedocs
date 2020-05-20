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

* Google Cloud Storage folder `gs://pgp-harvard-data-public <https://console.cloud.google.com/storage/pgp-harvard-data-public>`_
* Google Genomics Dataset ID `9170389916365079788 <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.datasets.get?datasetId=9170389916365079788>`_
* Google BigQuery Dataset IDs
   * `google.com:biggene:pgp_20150205.genome_calls <https://bigquery.cloud.google.com/table/google.com:biggene:pgp_20150205.genome_calls>`_

Provenance
----------

Google Genomics variant set for dataset ``pgp_20150205``: `9170389916365079788 <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.datasets.get?datasetId=9170389916365079788>`_ contains:

* the Complete Genomics datasets from `gs://pgp-harvard-data-public/**/masterVar*bz2 <https://console.cloud.google.com/storage/pgp-harvard-data-public>`_

Appendix
--------

Google is hosting a copy of the `PGP`_ Harvard data in Google Cloud Storage.
All of the data is in this bucket: ``gs://pgp-harvard-data-public``

If you wish to browse the data you will need to
`install gsutil <https://cloud.google.com/storage/docs/gsutil_install>`_.

Once installed, you can run the ``ls`` command on the pgp bucket::

  $ gsutil ls gs://pgp-harvard-data-public
  gs://pgp-harvard-data-public/cgi_disk_20130601_00C68/
  gs://pgp-harvard-data-public/hu011C57/
  gs://pgp-harvard-data-public/hu016B28/
  ....lots more....

The sub folders are `PGP`_ IDs, so if we ``ls`` a specific one::

  $ gsutil ls gs://pgp-harvard-data-public/hu011C57/
  gs://pgp-harvard-data-public/hu011C57/GS000018120-DID/

And then keep diving down through the structure, you can end up here::

  $ gsutil ls gs://pgp-harvard-data-public/hu011C57/GS000018120-DID/GS000015172-ASM/GS01669-DNA_B05/ASM/
  gs://pgp-harvard-data-public/hu011C57/GS000018120-DID/GS000015172-ASM/GS01669-DNA_B05/ASM/dbSNPAnnotated-GS000015172-ASM.tsv.bz2
  gs://pgp-harvard-data-public/hu011C57/GS000018120-DID/GS000015172-ASM/GS01669-DNA_B05/ASM/gene-GS000015172-ASM.tsv.bz2
  ... and more ...


Your genome data is located at:
gs://pgp-harvard-data-public/{YOUR_PGP_ID}

If you do not see the data you are looking for, you should contact
`PGP`_ directly through `your web profile <https://my.pgp-hms.org/message/new>`_.

