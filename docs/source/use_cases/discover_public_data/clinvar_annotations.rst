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

ClinVar Annotations
===================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/clinvar_annotations.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

Annotations from `ClinVar`_ were loaded into Google Genomics for use in sample annotation pipelines.  This data reflects the state of `ClinVar`_ at a particular point in time.

Google Cloud Platform data locations
------------------------------------

* Google Cloud Storage folder `gs://genomics-public-data/clinvar/ <https://console.cloud.google.com/storage/browser/genomics-public-data/clinvar/>`_
* Google Genomics `annotation sets <https://developers.google.com/apis-explorer/?#p/genomics/v1/genomics.annotationsets.search?_h=3&resource=%257B%250A++%2522datasetIds%2522%253A+%250A++%255B%25222259180486797191426%2522%250A++%255D%250A%257D&>`_

Provenance
----------

Each of the annotation sets listed below was imported into the API from the source files. The source files are also mirrored in Google Cloud Storage.

`ClinVar`_ (downloaded 2/5/2015 10:18AM PST):

* ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz
* ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/disease_names

Caveats
-------

A number of ClinVar entries were omitted during ingestion due to data incompatibility with the Google Genomics API.

* 14737 were aligned to NCBI36, which the Google Genomics API does not currently support.
* 5952 did not specify a reference assembly.
* 1324 were labeled as insertions but did not specify the inserted bases.
* 220 were labeled as SNPs, but did not specify an alternate base.
* 148 were larger than 100MBp.
