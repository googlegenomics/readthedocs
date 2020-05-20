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

Linkage Disequilibrium Datasets
===============================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/linkage_disequilibrium/public_ld_datasets.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

Linkage disequilibrium was run separately for each `super population and sub population <http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/integrated_call_samples_v3.20130502.ALL.panel>`_ within :doc:`/use_cases/discover_public_data/1000_genomes` phase 3 variants using the method defined in Box 1 of:

| `Linkage disequilibrium - understanding the evolutionary past and mapping the medical future <http://www.nature.com/nrg/journal/v9/n6/full/nrg2361.html>`_
| Slatkin, Montgomery
| Nature Reviews Genetics, Volume 9, Issue 6, 477 - 485
| DOI: http://dx.doi.org/10.1038/nrg2361
|

LD was computed for all pairs of variants within a window of 1,000,000 bp (1 megabase) and all pairs with absolute allelic correation of 0.4 are retained.   See :doc:`/use_cases/linkage_disequilibrium/compute_linkage_disequilibrium` for more detail.

The `output files <https://console.cloud.google.com/storage/browser/genomics-public-data/linkage-disequilibrium/1000-genomes-phase-3/ldCutoff0.4_window1MB/>`_ were split by chromosome with `output columns <https://github.com/googlegenomics/linkage-disequilibrium#linkage-disequilibrium-calculation-pipeline>`_ indicating the identity of each pair of values and the resulting LD value. The output files have also been `loaded into BigQuery <https://bigquery.cloud.google.com/dataset/genomics-public-data:linkage_disequilibrium_1000G_phase_3?pli=1>`_ with the same columns. Examples of using BigQuery to analyze LD are `available as Datalab notebooks <https://github.com/googlegenomics/linkage-disequilibrium/tree/master/datalab>`_.

Google Cloud Platform data locations
------------------------------------

* Google Cloud Storage folder `gs://genomics-public-data/linkage-disequilibrium <https://console.cloud.google.com/storage/browser/genomics-public-data/linkage-disequilibrium/1000-genomes-phase-3/ldCutoff0.4_window1MB/>`_
* Google BigQuery Dataset ID `genomics-public-data:linkage_disequilibrium_1000G_phase_3 <https://bigquery.cloud.google.com/dataset/genomics-public-data:linkage_disequilibrium_1000G_phase_3>`_
