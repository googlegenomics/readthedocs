.. _gzip: http://www.gzip.org/
.. _bzip2: http://www.bzip.org/

.. |br| raw:: html

   <br />

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
Compress/Decompress files in Cloud Storage
==========================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/compress_or_decompress_many_files/index.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

Suppose you have thousands of VCFs, which you have stored *compressed* in
Google Cloud Storage, and you need to perform some operation on them in
their *decompressed* state.

A few examples:

* You want to run some check or update on all of the headers
* You want to import them into Google Genomics

Or suppose you have thousands of VCFs, and you did not compress them when
originally copying them to Google Cloud Storage, but these VCFs can now be
compressed and archived.

The ``compress`` tool available in the `Grid Computing Tools github repo`_
can be used for any of these situations if your compression scheme is
either `gzip`_ or `bzip2`_.

--------
Overview
--------

.. include:: /includes/grid-computing-tools-overview.rst

-------------------------------
Workstation directory structure
-------------------------------

.. include:: /includes/grid-computing-tools-workstation-directory-structure.rst

-------------------
Running the samples
-------------------
The quickest way to get familiar with the ``compress`` tool is by trying one
or more of the samples. Samples are provided for the following uses:

* Download bzip2-compressed files from Cloud Storage, decompress them, and upload the results into Cloud Storage
* Download decompressed files from Cloud Storage, compress them with bzip2, and upload the results into Cloud Storage
* Download gzip-compressed files from Cloud Storage, decompress them, and upload the results into Cloud Storage
* Download decompressed files from Cloud Storage, compress them with gzip, and upload the results into Cloud Storage

The samples provided here each list just 6 files to work on, and the
instructions below demonstrate spreading the processing over 3 worker instances.

1. .. include:: /includes/grid-computing-tools-steps-create-cluster.rst

2. .. include:: /includes/grid-computing-tools-steps-download-grid-computing-repo.rst

3. **Upload the** ``src`` **and** ``samples`` **directories to the Grid Engine master instance:**

  .. code-block:: shell

    cd grid-computing-tools

    elasticluster sftp gridengine << 'EOF'
    mkdir src
    mkdir src/common
    mkdir src/compress
    put src/common/* src/common/
    put src/compress/* src/compress/
    mkdir samples
    mkdir samples/compress
    put samples/compress/* samples/compress/
    EOF

4. .. include:: /includes/grid-computing-tools-steps-ssh-to-master.rst

5. **Set up the configuration files for the samples**

   The syntax for running each of the samples is the same:

   .. code-block:: shell

     ./src/compress/launch_compress.sh [config_file]

   The ``config_file`` lists two sets of key parameters:

   * What operation to perform
   * What are the source and destination locations

   |br|
   The operation to perform is controlled by the following:

   * COMPRESS_OPERATION: ``compress`` or ``decompress``
   * COMPRESS_TYPE: ``bzip2`` or ``gzip``
   * COMPRESS_EXTENSION: Typically ``.bz2`` or ``.gz``

   |br|
   The locations are determined by:

   * INPUT_LIST_FILE: file containing a list of GCS paths to the input files to process
   * OUTPUT_PATH: GCS path indicating where to upload the output files
   * OUTPUT_LOG_PATH: (optional) GCS path indicating where to upload log files

   |br|
   To use the samples, you must update the ``OUTPUT_PATH`` and
   ``OUTPUT_LOG_PATH`` to contain a valid GCS bucket name.
   Each of the sample config files sets a placeholder
   for the ``OUTPUT_PATH`` and ``OUTPUT_LOG_PATH`` such as:

   .. code-block:: shell

     export OUTPUT_PATH=gs://MY_BUCKET/output_path/compress_bzip2
     export OUTPUT_LOG_PATH=gs://MY_BUCKET/log_path/compress_bzip2

   You can do this manually with the editor of your choice or you can
   change all of the ``config`` files at once with the command:

   .. code-block:: shell

     sed --in-place -e 's#MY_BUCKET#your_bucket#' samples/compress/*_config.sh

   Where ``your_bucket`` should be replaced with the name of a GCS bucket in
   your Cloud project to which you have write access.

   |br|
6. **Run the sample:**

   You can run all of the samples, or just those that model your particular
   use-case.

   * Compress a list of files using bzip2 [ Estimated time to complete: 35 minutes ]

   .. code-block:: shell

     ./src/compress/launch_compress.sh ./samples/compress/bzip2_compress_config.sh

   * Decompress a list of files using bzip2 [ Estimated time to complete: 4 minutes ]

   .. code-block:: shell

     ./src/compress/launch_compress.sh ./samples/compress/bzip2_decompress_config.sh

   * Compress a list of files using gzip [ Estimated time to complete: 15 minutes ]

   .. code-block:: shell

     ./src/compress/launch_compress.sh ./samples/compress/gzip_compress_config.sh

   * Decompress a list of files using gzip [ Estimated time to complete: 5 minutes ]

   .. code-block:: shell

     ./src/compress/launch_compress.sh ./samples/compress/gzip_decompress_config.sh

   When successfully launched, Grid Engine should emit a message such as:

   .. code-block:: shell

     Your job-array 1.1-6:1 ("compress") has been submitted

   This message tells you that the submitted job is a `gridengine array job`_.
   The above message indicates that the job id is **1** and that the tasks are
   numbered **1** through **6**.
   The name of the job, **compress**, is also indicated.

   |br|
7. .. include:: /includes/grid-computing-tools-steps-monitoring-job-status.rst

   |br|
8. .. include:: /includes/grid-computing-tools-steps-check-logging.rst

   |br|
9. .. include:: /includes/grid-computing-tools-steps-viewing-results.rst

   |br|
10. .. include:: /includes/grid-computing-tools-steps-viewing-log-files.rst

11. .. include:: /includes/grid-computing-tools-steps-delete-cluster.rst

--------------------
Running your own job
--------------------
To run your own job to compress/decompress a list of files requires the following:

.. include:: /includes/grid-computing-tools-run-your-own-overview.rst

1. **Create an** ``input list file``

   If all of your input files appear in a single directory, then the
   easiest way to generate a file list is with `gsutil`_. For example:

   .. code-block:: shell

     gsutil ls gs://MY_BUCKET/PATH/*.vcf.bz2 > ${WS_ROOT}/my_jobs/compressed_vcf_list_file.txt

2. **Create a** ``job config file``

   The easiest way to create a job config file is to base it off the
   appropriate sample and update

     * INPUT_LIST_FILE
     * OUTPUT_PATH
     * OUTPUT_LOG_PATH

   Save the job config file to ``${WS_ROOT}/my_jobs/``.

   |br|
3. .. include:: /includes/grid-computing-tools-steps-sizing-disks.rst

4. **Upload input list file, config file, and** ``grid-computing-tools`` **source to the gridengine cluster master**

  .. code-block:: shell

    elasticluster sftp gridengine << EOF
    put ../my_jobs/*
    mkdir src
    mkdir src/common
    mkdir src/compress
    put src/common/* src/common/
    put src/compress/* src/compress/
    EOF

5. .. include:: /includes/grid-computing-tools-steps-do-a-dry-run.rst

   For example:

   .. code-block:: shell

     $ DRYRUN=1 ./src/compress/launch_compress.sh ./samples/compress/gzip_compress_config.sh
     Your job-array 5.1-6:1 ("compress") has been submitted

   Then after waiting for the job to complete, inspect:

   .. code-block:: shell

     $ head -n 5 compress.o3.1
     Task host: compute001
     Task start: 1
     Input list file: ./samples/compress/gzip_compress_file_list.txt
     Output path: gs://cookbook-bucket/output_path/compress_gzip
     Output log path: gs://cookbook-bucket/log_path/compress_gzip

     $ grep "^Will download:" compress.o5.*
     compress.o5.1:Will download: gs://genomics-public-data/platinum-genomes/vcf/NA12877_S1.genome.vcf to /scratch/compress.5.1/in/
     compress.o5.2:Will download: gs://genomics-public-data/platinum-genomes/vcf/NA12878_S1.genome.vcf to /scratch/compress.5.2/in/
     compress.o5.3:Will download: gs://genomics-public-data/platinum-genomes/vcf/NA12879_S1.genome.vcf to /scratch/compress.5.3/in/
     compress.o5.4:Will download: gs://genomics-public-data/platinum-genomes/vcf/NA12880_S1.genome.vcf to /scratch/compress.5.4/in/
     compress.o5.5:Will download: gs://genomics-public-data/platinum-genomes/vcf/NA12881_S1.genome.vcf to /scratch/compress.5.5/in/
     compress.o5.6:Will download: gs://genomics-public-data/platinum-genomes/vcf/NA12882_S1.genome.vcf to /scratch/compress.5.6/in/

6. .. include:: /includes/grid-computing-tools-steps-do-a-test-run.rst

   |br|
   For example to launch a Grid Engine array job that only processes line 1:

   .. code-block:: shell

     $ LAUNCH_MIN=1 LAUNCH_MAX=1 ./src/compress/launch_compress.sh ./samples/compress/gzip_compress_config.sh
     Your job-array 5.1-1:1 ("compress") has been submitted

   The ``LAUNCH_MIN`` and ``LAUNCH_MAX`` values can be used with the
   ``DRYRUN`` environment variable:

   .. code-block:: shell

     $ DRYRUN=1 LAUNCH_MIN=1 LAUNCH_MAX=1 ./src/compress/launch_compress.sh ./samples/compress/gzip_compress_config.sh
     Your job-array 6.1-5:1 ("compress") has been submitted

7. **Launch the job**

  On the master instance, run the launch script, passing in the config file:

  .. code-block:: shell

    ./src/compress/launch_compress.sh my_job_config.sh

  where *my_job_config.sh* is replaced by the name of your config file created
  in step 2.

