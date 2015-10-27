Run iPython Notebooks on Google Compute Engine
===============================================

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

The https://github.com/googlegenomics/datalab-examples repository contains example notebooks for genomics use cases upon public data such as the :doc:`/use_cases/discover_public_data/platinum_genomes` and :doc:`/use_cases/discover_public_data/1000_genomes`.

You can read them on github:

* `Exploring Genomic Data <https://github.com/GoogleCloudPlatform/datalab/blob/master/content/datalab/samples/Exploring%20Genomics%20Data.ipynb>`_
* `Explore the 1000 Genomes Sample Information <datalab/genomics/Explore%201000%20Genomes%20Samples.ipynb>`_
* `Genome-wide association study <datalab/genomics/Genome-wide%20association%20study%20(GWAS).ipynb>`_
* `Getting started with the Google Genomics API <datalab/genomics/Getting%20started%20with%20the%20Genomics%20API.ipynb>`_

To run the examples yourself:

1. Launch your own Cloud Datalab instance: https://cloud.google.com/datalab/
2. Work through the introductory notebooks first that are pre-installed on Cloud Datalab.
3. Run ``git clone https://github.com/googlegenomics/datalab-examples.git`` on your local file system to download the notebooks.
4. Import the genomics notebooks into your Cloud Datalab instance by navigating to the notebook list page and uploading them one at a time.

Be sure to shut down Cloud Datalab when you are no longer using it.  Shut down instructions and other tips are `here <https://cloud.google.com/datalab/getting-started>`_.

