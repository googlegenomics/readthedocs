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

Run iPython Notebooks on Compute Engine
=======================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/run_familiar_tools/datalab.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

`Google Cloud Datalab`_ is built on Jupyter (formerly IPython) and enables analysis of your data in `Google BigQuery`_, `Google Compute Engine`_, `Google Cloud Storage`_, and `Google Genomics`_ using Python, SQL, and JavaScript (for BigQuery user-defined functions).

Read Example Notebooks
----------------------

There are several example notebooks for genomics use cases upon public data such as the :doc:`/use_cases/discover_public_data/platinum_genomes`, :doc:`/use_cases/discover_public_data/1000_genomes`, and :doc:`/use_cases/discover_public_data/isb_cgc_data`.  You can read them on github:

* `Exploring Genomic Data <https://github.com/googledatalab/datalab/blob/master/dev/notebooks/Exploring%20Genomics%20Data.ipynb>`_
* `Explore the 1000 Genomes Sample Information <https://github.com/googlegenomics/datalab-examples/blob/master/datalab/genomics/Explore%201000%20Genomes%20Samples.ipynb>`_
* `Genome-wide association study <https://github.com/googlegenomics/datalab-examples/blob/master/datalab/genomics/Genome-wide%20association%20study%20(GWAS).ipynb>`_
* `Getting started with the Google Genomics API <https://github.com/googlegenomics/datalab-examples/blob/master/datalab/genomics/Getting%20started%20with%20the%20Genomics%20API.ipynb>`_
* And find more sample notebooks in:

  * `https://github.com/googlegenomics/datalab-examples <https://github.com/googlegenomics/datalab-examples>`_
  * `https://github.com/GoogleCloudPlatform/datalab <https://github.com/GoogleCloudPlatform/datalab/blob/master/content/datalab/Readme.ipynb>`_
  * `https://github.com/isb-cgc/examples-Python <https://github.com/isb-cgc/examples-Python>`_
  * `https://github.com/googlegenomics/linkage-disequilibrium <https://github.com/googlegenomics/linkage-disequilibrium/tree/master/datalab>`_

Run Notebooks
-------------
To run the examples yourself:

1. Launch your own Cloud Datalab instance `in the cloud <https://cloud.google.com/datalab/getting-started>`_ or `run it locally <https://github.com/GoogleCloudPlatform/datalab#using-datalab-and-getting-started>`_.
2. Work through the introductory notebooks that are pre-installed on Cloud Datalab.
3. Run ``git clone https://github.com/googlegenomics/datalab-examples.git`` on your local file system to download the notebooks.
4. Import the genomics notebooks into your Cloud Datalab instance by navigating to the notebook list page and uploading them.

If you are running in the cloud, be sure to shut down Cloud Datalab when you are no longer using it. Shut down instructions and other tips are `here <https://cloud.google.com/datalab/getting-started>`__.
