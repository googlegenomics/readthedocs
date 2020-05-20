.. |suggested_client_id_name| replace:: ``Genomics Tools``
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

Run Picard and GATK tools on Cloud-Resident Genomic Data
========================================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/run_picard_and_gatk/index.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

Introduction
------------

`Picard`_/`GATK`_ tools are command line utilities for genomic sequencing data processing that typically take BAM and other files as input and produce modified BAM files.

These tools are frequently chained together into pipelines to perform step-by-step processing of the sequencing data all the way from unaligned sequencer output to variant calls (e.g. see `Broad best practices <https://www.broadinstitute.org/gatk/guide/best-practices>`_).

=====

We are teaching these tools to take cloud based datasets as a possible input. The foundation for cloud data access is now in HTSJDK library and we have converted a number of Picard tools.

If your dataset is loaded into a cloud provider supporting `GA4GH`_ API (e.g. `Google Genomics`_) or you use one of the available datasets from :doc:`/use_cases/discover_public_data/index`, you will be able to run a Picard tool against it, reading data directly from the cloud.

=====

**New**: see `the video version <https://www.youtube.com/playlist?list=PLYKy4VbxNln5j89ESpYBVUkeFDbmQwxYG>`__ of this tutorial.

Below is a step by step guide on how to build Picard tools with GA4GH support, set-up access to genomics data in the cloud and run the tools.

By the end of this tutorial you will be able run a Picard tool, giving it a URL identifying a genomic dataset in the cloud and see the output of processing the data directly from the cloud.

We also have detailed description of changes to HTSJDK and Picard to help you write your own cloud-aware client on top of HTSDK or help us convert more Picard tools.

Set up access to genomics data in Google Cloud
-------------------------------------------------

We will assume you are starting from a completely blank slate so please skip the steps that are redundant for you.

If you are already using Google Genomics API and have a project set up for this you can skip this section and go directly to `Build Picard tools with GA4GH support`_.

.. include:: /includes/genomics_tools_setup.rst

.. _Build Picard tools with GA4GH support:

Build Picard tools with GA4GH support
-------------------------------------
You will need `Maven <https://maven.apache.org/install.html>`_ and `Ant <http://ant.apache.org/manual/install.html>`_ build tools installed on your machine.

1. Fetch `Picard`_, `HTSJDK`_ and `gatk-tools-java`_ projects required for building Picard with GA4GH support.

.. code-block:: shell

  $ git clone https://github.com/broadinstitute/picard.git
  $ cd picard
  $ git clone https://github.com/samtools/htsjdk
  $ cd ..
  $ git clone https://github.com/googlegenomics/gatk-tools-java

2. Build gatk-tools-java and copy the resulting JAR into Picard library folder:

.. code-block:: shell

  $ cd gatk-tools-java
  $ mvn compile package
  $ mkdir ../picard/lib/gatk-tools-java
  $ cp target/gatk-tools-java*minimized.jar ../picard/lib/gatk-tools-java/

3. Build Picard version with GA4GH support:

.. code-block:: shell

  // Assuming you are still in gatk-tools-java directory
  $ cd ../picard
  $ ant -lib lib/ant package-commands-ga4gh

4. Make sure you put **client_secrets.json** file in the parent folder just above Picard.
You should end up with the following directory structure:

.. code-block:: shell

  your_client_folder \
    client_secrets.json
    gatk-tools-java \
    picard \
      htsjdk \


Run Picard tools with an input from the cloud
---------------------------------------------

You can now run ViewSam tool that prints the contents of the supplied INPUT

.. code-block:: shell

  $ cd picard
  $ java \
     -jar dist/picard.jar ViewSam \
     INPUT=https://www.googleapis.com/genomics/v1beta2/readgroupsets/CK256frpGBD44IWHwLP22R4/ \
     GA4GH_CLIENT_SECRETS=../client_secrets.json

This command uses an older, slower REST based API. To run using GRPC API implementation (which is much faster) use the following command that utilizes ALPN jars that come with gatk-tools-java and enables GRPC support:

.. code-block:: shell

  java \
   -Xbootclasspath/p:../gatk-tools-java/lib/alpn-boot-8.1.3.v20150130.jar \
   -Dga4gh.using_grpc=true \
   -jar dist/picard.jar ViewSam \
   INPUT=https://www.googleapis.com/genomics/v1beta2/readgroupsets/CK256frpGBD44IWHwLP22R4/ \
   GA4GH_CLIENT_SECRETS=../client_secrets.json

For Java 7 (as opposed to 8) use *alpn-boot-7.1.3.v20150130.jar*.

We use a test readset here from `genomics-test-data <https://console.cloud.google.com/project/genomics-test-data/storage/browser/gatk-tools-java/>`_ project.

Specifying a genomics region to use from the readset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The INPUT urls are of the form **https://<GA4GH provider>/readgroupsets/<readgroupset id>[/sequence][/start-end]**.

For example:

.. code-block:: shell

  java -jar dist/picard.jar ViewSam \
  INPUT=https://www.googleapis.com/genomics/v1beta2/readgroupsets\
  /CMvnhpKTFhD3he72j4KZuyc/chr17/41196311-41207499 \
  GA4GH_CLIENT_SECRETS=../client_secrets.json


Timing the reading speed from the cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can run `gatk-tools-java/src/main/scripts/example.sh <https://github.com/googlegenomics/gatk-tools-java/blob/master/src/main/scripts/example.sh>`_ with and without "grpc" command line parameter to see the difference in reading speed. The timing statistics are dumped to the terminal.
We benchmarked **x11** speed improvements with GRPC compared to REST, giving **~12,000 reads/second**.

The tests were done on `Platinum Genomes NA12877_S1.bam dataset <https://console.cloud.google.com/storage/browser/genomics-public-data/platinum-genomes/bam/?_ga=1.197206447.160385476.1431305548>`_, please see the `detailed writeup of the test procedure and results <https://docs.google.com/document/d/1Br7RMSbAChNpG6pi2teujf-YthczF-rAM1afSgDoCgQ/edit#>`_ if you want to repeat the test.

We therefore recommend running GRPC variants of command line.

Other Picard tools you can run
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can run MarkDuplicates or MarkDuplicatesWithMateCigar tools like this:

.. code-block:: shell

  java \
    -Xbootclasspath/p:../gatk-tools-java/lib/alpn-boot-8.1.3.v20150130.jar \
    -Dga4gh.using_grpc=true \
    -jar dist/picard.jar MarkDuplicates \
    INPUT=https://www.googleapis.com/genomics/v1beta2/readgroupsets/CK256frpGBD44IWHwLP22R4/ \
    OUTPUT=output.bam \
    METRICS_FILE=output.metrics \
    GA4GH_CLIENT_SECRETS=../client_secrets.json

Figuring out a url for your dataset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the examples above we have been using urls of the form https://www.googleapis.com/genomics/v1beta2/readgroupsets/XXX where XXX is the id of the readset.

How do you find an ID of the readset from the  :doc:`/use_cases/discover_public_data/index` set or from your own project ?

We will do it step by step using the command line API client.

* Lets say we want to use `Platinum Genomes NA12877_S1.bam readgroupset <https://console.cloud.google.com/storage/browser/genomics-public-data/platinum-genomes/bam/?_ga=1.197206447.160385476.1431305548>`_ from :doc:`/use_cases/discover_public_data/1000_genomes` project.

* The `documentation <https://cloud.google.com/genomics/data/1000-genomes?hl=en>`_ page states that the dataset id for this set of files is **10473108253681171589**.

* To list readgroupsets under this dataset:

.. code-block:: shell

     $ gcloud alpha genomics readgroupsets list 10473108253681171589 --limit 10
     ID                      NAME     REFERENCE_SET_ID
     CMvnhpKTFhDq9e2Yy9G-Bg  HG02573  EOSt9JOVhp3jkwE
     CMvnhpKTFhCEmf_d_o_JCQ  HG03894  EOSt9JOVhp3jkwE
     ...

* Note the **NAME** column - it will correspond to the file name. The **ID** column is the ID of the readgroupset we are looking for.


Now lets suppose we are not looking for one of the readgroupsets form the genomics public data but instead want to use one from our own project.
In this case we need to figure out the *dataset id* for our files first, before we can use "readgroupsets list" command to list the individual readgroupsets.

* Lets say we want to figure out which dataset ids are present under `genomics test data <https://console.cloud.google.com/project/genomics-test-data/storage/browser>`_ project.

* First we need to set the project id for subsequent commands to be our project using

.. code-block:: shell

	$ gcloud config set project genomics-test-data

* Now we can issue this command:

.. code-block:: shell

     $ gcloud alpha genomics datasets list --limit 10

* The output will list dataset(s) present in the project together with their ids and we can then use the "readgroupsets list" command to get the id of the readgroupset under one of the datasets.

