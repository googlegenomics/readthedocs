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

Run Bioconductor on Compute Engine
==================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/run_familiar_tools/bioconductor.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

.. include:: /includes/bioconductor_deployment_sidebar.rst

Bioconductor maintains Docker containers with R, Bioconductor packages, and RStudio Server all ready to go!  Its a great way to set up your R environment quickly and start working.  The instructions to deploy it to Google Compute Engine are below but if you want to learn more about these containers, see http://www.bioconductor.org/help/docker/.

1. Click on `click-to-deploy Bioconductor`_ to navigate to the launcher page on the Cloud Platform Console.

  1. Optional: change the *Machine type* if you would like to deploy a machine with more CPU cores or RAM.
  2. Optional: change the *Data disk size (GB)* if you would like to use a larger persistent disk for your own files.
  3. Optional: change *Docker image* if you would like to run a container with additional Bioconductor packages preinstalled.

2. Click on the *Deploy Bioconductor* button.
3. Follow the post-deployment instructions to log into RStudioServer via your browser!

If you want to deploy a different docker container, such as the one from :doc:`/workshops/bioc-2015` or from https://github.com/isb-cgc/examples-R:

1. In field *Docker Image* choose item ``custom``.
2. Click on *More* to display the additional form fields.
3. In field *Custom docker image* paste in the docker image path, such as ``gcr.io/bioc_2015/devel_sequencing`` or ``b.gcr.io/isb-cgc-public-docker-images/r-examples``.

Change your virtual machine type (number of cores, amount of memory)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. First, make sure results from your current R session are saved to the data disk (underneath ``/home/rstudio/data``) or another location outside of the container.
2. Follow these instructions to stop, resize, and start your VM: https://cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance

"Stop" or "Delete" your virtual machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: /includes/c2d_deployment_teardown.rst

