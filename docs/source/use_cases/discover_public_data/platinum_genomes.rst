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

Illumina Platinum Genomes
===========================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/platinum_genomes.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

This dataset comprises the `6 member CEPH pedigree 1463 <http://www.ebi.ac.uk/ena/data/view/PRJEB3381>`_.  See http://www.illumina.com/platinumgenomes/ for full details.

Google Cloud Platform data locations
------------------------------------

* Google Cloud Storage folder `gs://genomics-public-data/platinum-genomes <https://console.cloud.google.com/storage/genomics-public-data/platinum-genomes/>`_
* Google Genomics Dataset ID `3049512673186936334 <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.datasets.get?datasetId=3049512673186936334>`_

  * `ReadGroupSet IDs <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.readgroupsets.search?fields=readGroupSets(id%252Cname)&_h=5&resource=%257B%250A++%2522datasetIds%2522%253A+%250A++%255B%25223049512673186936334%2522%250A++%255D%250A%257D&>`_
  * `Variant Reference Bounds <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.variantsets.get?variantSetId=3049512673186936334&_h=2&>`_

* Google BigQuery Dataset ID `genomics-public-data:platinum_genomes <https://bigquery.cloud.google.com/table/genomics-public-data:platinum_genomes.variants>`_

Beacon
------
You can find a `Global Alliance for Genomics and Health Beacon`_ at http://webdev.dnastack.com/p/beacon/platinum?chromosome=1&coordinate=10177&allele=AC

Provenance
----------

* The source files for this data include:
   * All of the BAM files listed at `the EBI FTP site <ftp://ftp.sra.ebi.ac.uk/vol1/ERA172/ERA172924/bam>`_.
   * All of the VCF files were listed at `the Illumina FTP site <ftp://ussd-ftp.illumina.com/>`_ prior to the IlluminaPlatinumGenomes_v6.0 release but they have since been taken down.
* These files were copied to Google Cloud Storage, uploaded to Google Genomics, and the variants were exported to Google BigQuery.
