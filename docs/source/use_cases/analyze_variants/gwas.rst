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

Genome-Wide Association Study (GWAS)
====================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/analyze_variants/gwas.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

`Google BigQuery`_ can be used to perform a GWAS.  Here are several examples:

* Chi-squared tests on :doc:`/use_cases/discover_public_data/1000_genomes` dataset with members of EAS super population as case and control all other populations:

  * iPythonNotebook `Genome-wide association study (GWAS).ipynb <https://github.com/googlegenomics/datalab-examples/blob/master/datalab/genomics/Genome-wide%20association%20study%20(GWAS).ipynb>`_
  * SQL `gwas-pattern-chi-squared-test.sql <https://github.com/googlegenomics/bigquery-examples/blob/master/1000genomes/sql/gwas-pattern-chi-squared-test.sql>`_

* Two-proportion Z test on :doc:`/use_cases/discover_public_data/1000_genomes` dataset with members of EAS super population as case and control all other populations:

  * SQL `gwas-pattern-two-proportion-z-test.sql <https://github.com/googlegenomics/bigquery-examples/blob/master/1000genomes/sql/gwas-pattern-two-proportion-z-test.sql>`_

* Chi-squared test on :doc:`/use_cases/discover_public_data/1000_genomes` dataset with case and control determined by clustering from a PCA:

  * R package vignette `AllModalitiesDemo.md <https://github.com/googlegenomics/codelabs/blob/master/R/1000Genomes-BRCA1-analysis/AllModalitiesDemo.md>`__
  * written as a codelab `AllModalitiesDemo.md <https://github.com/googlegenomics/bioconductor-workshop-r/blob/master/inst/doc/AllModalitiesDemo.md>`__

To run this on your own data:

(1) First, load your data into Google Genomics and export your variants to BigQuery.  See `Load Genomic Variants`_ for more detail as to how to do this.
(2) For data with non-variant segments (e.g, `gVCF` or `Complete Genomics`_ data), reshape the data into multi-sample variants format via :doc:`/use_cases/load_data/multi_sample_variants`

