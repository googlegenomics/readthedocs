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

=============
Pipelines API
=============

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/run_pipelines_in_the_cloud/pipelines_api.html
==========================================

__ RenderedVersion_

.. comment: end: goto-read-the-docs

Do you have a task that you need to run independently over dozens,
hundreds, or thousands of files in Google Cloud Storage? The
`Google Genomics Pipelines API`_ provides an easy way to launch
and monitor tasks running in the cloud.

  +---------------------------------------------------------------------+
  | Alpha                                                               |
  +---------------------------------------------------------------------+
  | This is an Alpha release of Google Genomics API. This feature might |
  | be changed in backward-incompatible ways and is not recommended for |
  | production use. It is not subject to any SLA or deprecation policy. |
  +---------------------------------------------------------------------+

Overview
--------

A "pipeline" in its simplest form is a task consisting of:

  * Path(s) of input files to read from Cloud Storage
  * Path(s) of output files/directories to write to Cloud Storage
  * A Docker_ image to run
  * A command to run in the Docker image
  * Cloud resources to use (number of CPUs, amount of memory, disk size and type)

The Pipelines API will:

  #. Create a Compute Engine virtual machine
  #. Download the Docker image
  #. Download the input files
  #. Run a new Docker container with the specified image and command
  #. Upload the output files
  #. Destroy the Compute Engine virtual machine

Log files are uploaded periodically to Cloud Storage.

Alternatives
------------

For many cases, the Pipelines API has an advantage over fixed clusters
in that Compute Engine resources (virtual machines and disks) are
allocated only for the lifetime of the running pipeline, and are then
destroyed.

However many existing scripts assume a fixed cluster (such as a shared
disk).  If you want to create a fixed cluster, see
:doc:`/use_cases/setup_gridengine_cluster_on_compute_engine/index`

Getting started examples
------------------------

We have a github repository with several pipelines-api-examples_ to
help you get started.

See the `README <https://github.com/googlegenomics/pipelines-api-examples/>`_
at the top of the repository for prerequisites. Existing
examples include:

  * `Compress or decompress files <https://github.com/googlegenomics/pipelines-api-examples/blob/master/compress>`_
  * `Run FastQC over a list of BAM or FASTQ files <https://github.com/googlegenomics/pipelines-api-examples/blob/master/fastqc>`_
  * `Use samtools to create a BAM index file <https://github.com/googlegenomics/pipelines-api-examples/blob/master/samtools>`_
  * `Use a custom script in Cloud Storage to update a VCF header <https://github.com/googlegenomics/pipelines-api-examples/blob/master/set_vcf_sample_id>`_
  * `Use Bioconductor to count overlaps in a BAM file <https://github.com/googlegenomics/pipelines-api-examples/blob/master/bioconductor>`_

Beyond Files
------------

Note that the Pipelines API is not only for working with files.
If you have tools that access data in `Google Genomics`_,
`Google BigQuery`_, or any other Google Cloud API, they can be
run using the Pipelines API.

When running a pipeline, simply include the appropriate
`OAuth 2.0 Scope <https://developers.google.com/identity/protocols/googlescopes>`_
for the Compute Engine `ServiceAccount <https://cloud.google.com/genomics/reference/rest/v1alpha2/pipelines/run#ServiceAccount>`_.

