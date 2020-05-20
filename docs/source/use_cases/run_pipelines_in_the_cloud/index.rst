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

==========================================
Run workflows and common tasks in parallel
==========================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/run_pipelines_in_the_cloud/index.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

Researchers today have the ability to generate an incredible amount of biological data. Once you have this data, the next step is to refine it and analyze it for meaning. Whether you are developing your own algorithms or running common tools and workflows, you now have a large number of software packages to help you out.

Here we make a few recommendations for what technologies to consider. Your technology choice should be based on your own needs and experience. There is no “one size fits all” solution.

dsub
----

If your experience and preferred approach is to write Python (or Ruby or Perl) and orchestrate execution with a little bit of shell scripting, or you need to run some off the shelf command-line tools, then dsub may be the right answer for you. dsub is targeted towards computational biologists who often have experience with submitting tasks to a job scheduler (such as Grid Engine, Slurm, or LSF) after developing and testing algorithms on their workstation or laptop.

dsub source and getting started instructions can be found at:

*  https://github.com/googlegenomics/dsub

There you can find examples of running dsub for:

* `Custom scripts <https://github.com/googlegenomics/dsub/tree/master/examples/custom_scripts>`_
* `Decompressing files <https://github.com/googlegenomics/dsub/tree/master/examples/decompress>`_
* `Generating reports with FastQC <https://github.com/googlegenomics/dsub/tree/master/examples/fastqc>`_
* `Indexing BAMS with samtools <https://github.com/googlegenomics/dsub/tree/master/examples/samtools>`_

WDL and Cromwell
----------------

The Broad Institute has developed the Workflow Definition Language (WDL) and an associated runner called Cromwell. Together these have allowed the Broad to build, run at scale, and publish its best practices pipelines. If you want to run the Broad’s published GATK workflows or are interested in using the same technology stack, take a look at WDL and Cromwell.

The WDL specification and examples can be found at:

* https://github.com/broadinstitute/wdl

Cromwell source and documentation can be found at:

* https://github.com/broadinstitute/cromwell

Instructions for getting started with the GATK on Google Cloud can be found at:

* https://cloud.google.com/genomics/gatk

Grid Engine (or similar job scheduler)
--------------------------------------

Many computational biologists have experience running tasks on compute clusters using a job manager such as `Grid Engine`_ or `Slurm`_. If you have existing tools that assume such an environment, then you can create a similar cluster on Google Cloud using Elasticluster.

Elasticluster documentation can be found at:

*  https://elasticluster.readthedocs.org

For setup instructions, see:

.. toctree::
   :maxdepth: 1

   /use_cases/setup_gridengine_cluster_on_compute_engine/index

You can find examples of using Grid Engine for tasks such as:

.. toctree::
   :maxdepth: 1

   /use_cases/run_samtools_over_many_files/index
   /use_cases/compress_or_decompress_many_files/index

Apache Beam and Google Cloud Dataflow
----------------------

If you want to develop brand new pipelines with the most sophisticated and scalable data processing infrastructure, then Apache Beam and Google Cloud Dataflow may be the right choice for you. Dataflow is a fully managed runner for Apache Beam.

More on Apache Beam can be found at:

* https://beam.apache.org

More on Google Cloud Dataflow can be found at:

* https://cloud.google.com/dataflow

Genomics Pipelines API
----------------------

To run tasks on Google Cloud, dsub uses the `Google Genomics Pipelines API`_. For most usage, dsub is the recommended interface. The Pipelines API is best suited to developers wanting to build new job management tools (like dsub) or workflow systems (like Cromwell).

For a more detailed overview, see:

.. toctree::
   :maxdepth: 1

   /use_cases/run_pipelines_in_the_cloud/pipelines_api

For examples of calling the API from Python, see:

* `pipelines-api-examples`_

