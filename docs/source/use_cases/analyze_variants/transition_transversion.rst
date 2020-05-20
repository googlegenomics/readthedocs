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

Transition/Transversion Ratio
=============================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/analyze_variants/transition_transversion.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

There are several transition/transversion ratio examples in GitHub:

* Ti/Tv by Genomic Window `query <https://github.com/googlegenomics/codelabs/blob/master/R/PlatinumGenomes-QC/sql/ti-tv-ratio.sql>`__ and `plot <https://github.com/googlegenomics/codelabs/blob/master/R/PlatinumGenomes-QC/Variant-Level-QC.md#titv-by-genomic-window>`__.
* Ti/Tv by Alternate Allele Counts `query <https://github.com/googlegenomics/codelabs/blob/master/R/PlatinumGenomes-QC/sql/ti-tv-by-alternate-allele-count.sql>`__ and `plot <https://github.com/googlegenomics/codelabs/blob/master/R/PlatinumGenomes-QC/Variant-Level-QC.md#titv-by-alternate-allele-counts>`__.
* Ti/Tv for an entire cohort `query <https://github.com/googlegenomics/bigquery-examples/blob/master/1000genomes/sql/ti-tv-ratio.sql>`__.
* A `comparison <https://github.com/googlegenomics/bigquery-examples/tree/master/1000genomes/data-stories/reproducing-vcfstats>`__ of vcfstats Ti/Tv results to results from BigQuery.
