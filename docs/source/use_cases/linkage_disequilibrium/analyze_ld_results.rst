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

Analyze Linkage Disequilibrium Results
======================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/linkage_disequilibrium/analyze_ld_results.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

.. toctree::
   :maxdepth: 2

There are several examples of interacting with LD results stored in BigQuery using Datalab in GitHub. The examples are all part of the `linkage disequilibrium project <https://github.com/googlegenomics/linkage-disequilibrium/tree/master/datalab>`_.

* Exploring `summary statistics of LD data <https://github.com/googlegenomics/linkage-disequilibrium/blob/master/datalab/Exploring_Linkage_Disequilibrium_Data.ipynb>`_.
* `Visualizing LD patterns <https://github.com/googlegenomics/linkage-disequilibrium/blob/master/datalab/Visualizing_Regional_LD.ipynb>`_ in specific genomic regions.
* Examining the rate of `LD decay <https://github.com/googlegenomics/linkage-disequilibrium/blob/master/datalab/LD_decay.ipynb>`_ as a function of distance.
* Selecting "tag variants" and visualizing `tag variant distributions <https://github.com/googlegenomics/linkage-disequilibrium/blob/master/datalab/Tag_variant_identification.ipynb>`_.

