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

TCGA Cancer Genomics Data in the Cloud
======================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/isb_cgc_data.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

Use the power of BigQuery to analyze the wealth of data created by `The Cancer Genome Atlas <http://cancergenome.nih.gov/>`_ (TCGA) project!

The Institute for Systems Biology (ISB) has created and made public a dataset based on the open-access TCGA data including somatic mutation calls, clinical data, mRNA and miRNA expression, DNA methylation and protein expression from 33 different tumor types. It's part of their `Cancer Genomics Cloud`_, funded by the National Cancer Institute. They've also created public github repositories  so you can try out sample queries and analyses in R or `Google Cloud Datalab`_.

 * `documentation <http://isb-cancer-genomics-cloud.readthedocs.org/>`__
 * `examples in R <https://github.com/isb-cgc/examples-R>`_
 * `examples in Python <https://github.com/isb-cgc/examples-Python>`_

Google Cloud Platform data locations
------------------------------------

* Google BigQuery Dataset IDs: 
   + `isb-cgc:TCGA_bioclin_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_bioclin_v0>`_
   + `isb-cgc:TCGA_hg19_data_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_hg19_data_v0>`_
   + `isb-cgc:TCGA_hg38_data_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_hg38_data_v0>`_

