Data Analysis Codelab
=====================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/analyze_variants/data_analysis_codelab.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

There are a collection of analyses upon variants documented in codelab `Data Analysis using Google Genomics`_.

In this codelab, you will use `Google Genomics`_, `Google BigQuery`_, `Apache Spark`_, and `R`_ to explore the :doc:`/use_cases/discover_public_data/1000_genomes` dataset. Specifically, you will:

* run a principal component analysis (either from scratch or using pre-computed results)
* use BigQuery to explore population variation
* zoom in to specific genome regions, including using the Genomics API to look all the way down to raw reads
* run a GWAS over the variants within BRCA1
* visualize and annotate results using various R packages, including `Bioconductor`_

To make use of this upon your own data:

(1) First, load your data into Google Genomics and export your variants to BigQuery.  See :doc:`/use_cases/load_data/index` for more detail as to how to do this.
(2) Update the BigQuery table name, variant set id, and read group set in the example to match those of your data.


