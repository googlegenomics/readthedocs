ClinVar Annotations
===================

Annotations from `ClinVar`_ were loaded into Google Genomics for use in sample annotation pipelines.  This data reflects the state of `ClinVar`_ at a particular point in time.

Each of the annotation sets listed below was imported into the API from the source files. The source files are also mirrored in Google Cloud Storage.

Provenance
----------
`ClinVar`_ (downloaded 2/5/2015 10:18AM PST):

* ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz
* ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/disease_names

Data
----
* Google Cloud Storage folder `gs://genomics-public-data/clinvar/ <https://console.developers.google.com/storage/browser/genomics-public-data/clinvar/>`_
* Google Genomics `annotation sets <https://developers.google.com/apis-explorer/?#p/genomics/v1beta2/genomics.annotationSets.search?_h=11&resource=%257B%250A++%2522datasetIds%2522%253A+%250A++%255B%252210673227266162962312%2522%250A++%255D%250A%257D&>`_

Caveats
----

A number of ClinVar entries were omitted during ingestion due to data incompatibility with the Google Genomics API.

* 14737 were aligned to NCBI36, which the Google Genomics API does not currently support.
* 5952 did not specify a reference assembly.
* 1324 were labeled as insertions but did not specify the inserted bases.
* 220 were labeled as SNPs, but did not specify an alternate base.
* 148 were larger than 100MBp.
