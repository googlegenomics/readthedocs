.. _samtools: http://www.htslib.org/

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

================================================
Run SAMtools to index BAM files in Cloud Storage
================================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/run_samtools_over_many_files/index.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

Suppose you have thousands of BAMs, which you have stored in
Google Cloud Storage, and you need to create index files (BAI) for them.

The `Grid Computing Tools github repo`_ provides code and instructions
for running `SAMtools`_ many times in parallel to create those index files.

--------
Overview
--------

.. include:: /includes/grid-computing-tools-overview.rst

-------------------
Directory structure
-------------------

.. include:: /includes/grid-computing-tools-workstation-directory-structure.rst

-------------------
Running the samples
-------------------
The quickest way to get familiar with the ``samtools`` tool is by trying the
sample.

The sample provided here lists just 6 files to work on, and the instructions
below demonstrate spreading the processing over 3 worker instances.

1. .. include:: /includes/grid-computing-tools-steps-create-cluster.rst

2. .. include:: /includes/grid-computing-tools-steps-download-grid-computing-repo.rst

3. **Upload the** ``src`` **and** ``samples`` **directories to the Grid Engine master instance:**

  .. code-block:: shell

    cd grid-computing-tools

    elasticluster sftp gridengine << 'EOF'
    mkdir src
    mkdir src/common
    mkdir src/samtools
    put src/common/* src/common/
    put src/samtools/* src/samtools/
    mkdir samples
    mkdir samples/samtools
    put samples/samtools/* samples/samtools/
    EOF

4. .. include:: /includes/grid-computing-tools-steps-ssh-to-master.rst

5. **Set up the configuration files for the samples**

   The syntax for running the sample is:

   .. code-block:: shell

     ./src/samtools/launch_samtools.sh [config_file]

   The ``config_file`` lists two sets of key parameters:

   * What operation to perform
   * What are the source and destination locations

   |br|
   The operation to perform is controlled by the following:

   * SAMTOOLS_OPERATION: ``index``

   |br|
   The locations are determined by:

   * INPUT_LIST_FILE: file containing a list of GCS paths to the input files to process
   * OUTPUT_PATH: GCS path indicating where to upload the output files.
     If set to ``source``, the output will be written to the same path
     as the source file (with the extension ``.bai`` appended)
   * OUTPUT_LOG_PATH: (optional) GCS path indicating where to upload log files

   |br|
   To use the samples, you must update the ``OUTPUT_PATH`` and
   ``OUTPUT_LOG_PATH`` to contain a valid GCS bucket name.
   The sample config file sets a placeholder
   for the ``OUTPUT_PATH`` and ``OUTPUT_LOG_PATH`` such as:

   .. code-block:: shell

     export OUTPUT_PATH=gs://MY_BUCKET/output_path/samtools_index
     export OUTPUT_LOG_PATH=gs://MY_BUCKET/log_path/samtools_index

   You can do this manually with the editor of your choice or you can change the
   ``config`` file with the command:

   .. code-block:: shell

     sed --in-place -e 's#MY_BUCKET#your_bucket#' samples/samtools/*_config.sh

   Where ``your_bucket`` should be replaced with the name of a GCS bucket in
   your Cloud project to which you have write access.

   |br|
6. **Run the sample:**

   * Index a list of files using ``samtools index`` [ Estimated time to complete: 5 minutes ]

   .. code-block:: shell

     ./src/samtools/launch_samtools.sh ./samples/samtools/samtools_index_config.sh

   When successfully launched, Grid Engine should emit a message such as:

   .. code-block:: shell

     Your job-array 1.1-6:1 ("samtools") has been submitted

   This message tells you that the submitted job is a `gridengine array job`_.
   The above message indicates that the job id is **1** and that the tasks are
   numbered **1** through **6**.
   The name of the job **samtools** is also indicated.

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
To run your own job to index a list of BAM files requires the following:

.. include:: /includes/grid-computing-tools-run-your-own-overview.rst

1. **Create an** ``input list file``

   If all of your input files appear in a single directory, then the
   easiest way to generate a file list is with ``gsutil``. For example:

   .. code-block:: shell

     gsutil ls gs://MY_BUCKET/PATH/*.bam > ${WS_ROOT}/my_jobs/bam_indexing_list_file.txt

2. **Create a** ``job config file``

   The easiest way to create a job config file is to base it off the
   sample and update:

     * INPUT_LIST_FILE
     * OUTPUT_PATH
     * OUTPUT_LOG_PATH

   To have the generated BAM index file written to the same location as the
   source BAM, set:

   .. code-block:: shell

     OUTPUT_PATH=source

   Save the job config file to ``${WS_ROOT}/my_jobs/``.

   |br|
3. .. include:: /includes/grid-computing-tools-steps-sizing-disks.rst

4. **Upload input list file, config file, and** ``grid-computing-tools`` **source to the gridengine cluster master**

  .. code-block:: shell

    elasticluster sftp gridengine << EOF
    put ../my_jobs/*
    mkdir src
    mkdir src/common
    mkdir src/samtools
    put src/common/* src/common/
    put src/samtools/* src/samtools/
    EOF

5. .. include:: /includes/grid-computing-tools-steps-do-a-dry-run.rst

   For example:

   .. code-block:: shell

      $ DRYRUN=1 ./src/samtools/launch_samtools.sh ./samples/samtools/samtools_index_config.sh
      Your job-array 2.1-6:1 ("samtools") has been submitted

   Then after waiting for the job to complete, inspect:

   .. code-block:: shell

      $ head -n 5 samtools.o3.1
      Task host: compute002
      Task start: 1
      Input list file: ./samples/samtools/samtools_index_file_list.txt
      Output path: gs://cookbook-bucket/output_path/samtools_index
      Output log path: gs://cookbook-bucket/log_path/samtools_index

      $ grep "^Will download:" samtools.o3.*
      samtools.o3.1:Will download: gs://genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/technical/pilot2_high_cov_GRCh37_bams/data/NA12878/alignment/NA12878.chrom9.SOLID.bfast.CEU.high_coverage.20100125.bam to /scratch/samtools.3.1/in/
      samtools.o3.2:Will download: gs://genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/technical/pilot2_high_cov_GRCh37_bams/data/NA12878/alignment/NA12878.chrom1.LS454.ssaha2.CEU.high_coverage.20100311.bam to /scratch/samtools.3.2/in/
      samtools.o3.3:Will download: gs://genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/pilot_data/data/NA12878/alignment/NA12878.chrom11.SOLID.corona.SRP000032.2009_08.bam to /scratch/samtools.3.3/in/
      samtools.o3.4:Will download: gs://genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/pilot_data/data/NA12878/alignment/NA12878.chrom12.SOLID.corona.SRP000032.2009_08.bam to /scratch/samtools.3.4/in/
      samtools.o3.5:Will download: gs://genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/pilot_data/data/NA12878/alignment/NA12878.chrom10.SOLID.corona.SRP000032.2009_08.bam to /scratch/samtools.3.5/in/
      samtools.o3.6:Will download: gs://genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/pilot_data/data/NA12878/alignment/NA12878.chromX.SOLID.corona.SRP000032.2009_08.bam to /scratch/samtools.3.6/in/

      $ grep "^Will upload:" samtools.o3.*
      samtools.o3.1:Will upload: /scratch/samtools.3.1/in/NA12878.chrom9.SOLID.bfast.CEU.high_coverage.20100125.bam.bai to gs://cookbook-bucket/output_path/samtools_index/
      samtools.o3.2:Will upload: /scratch/samtools.3.2/in/NA12878.chrom1.LS454.ssaha2.CEU.high_coverage.20100311.bam.bai to gs://cookbook-bucket/output_path/samtools_index/
      samtools.o3.3:Will upload: /scratch/samtools.3.3/in/NA12878.chrom11.SOLID.corona.SRP000032.2009_08.bam.bai to gs://cookbook-bucket/output_path/samtools_index/
      samtools.o3.4:Will upload: /scratch/samtools.3.4/in/NA12878.chrom12.SOLID.corona.SRP000032.2009_08.bam.bai to gs://cookbook-bucket/output_path/samtools_index/
      samtools.o3.5:Will upload: /scratch/samtools.3.5/in/NA12878.chrom10.SOLID.corona.SRP000032.2009_08.bam.bai to gs://cookbook-bucket/output_path/samtools_index/
      samtools.o3.6:Will upload: /scratch/samtools.3.6/in/NA12878.chromX.SOLID.corona.SRP000032.2009_08.bam.bai to gs://cookbook-bucket/output_path/samtools_index/

6. .. include:: /includes/grid-computing-tools-steps-do-a-test-run.rst

   |br|
   For example to launch a Grid Engine array job that only processes line 1:

   .. code-block:: shell

     $ LAUNCH_MIN=1 LAUNCH_MAX=1 ./src/samtools/launch_samtools.sh ./samples/samtools/samtools_index_config.sh
     Your job-array 5.1-1:1 ("samtools") has been submitted

   The ``LAUNCH_MIN`` and ``LAUNCH_MAX`` values can be used with the
   ``DRYRUN`` environment variable:

   .. code-block:: shell

     $ DRYRUN=1 LAUNCH_MIN=1 LAUNCH_MAX=5 ./src/samtools/launch_samtools.sh ./samples/samtools/samtools_index_config.sh
     Your job-array 6.1-5:1 ("samtools") has been submitted

7. **Launch the job**

  On the master instance, run the launch script, passing in the config file:

  .. code-block:: shell

    ./src/samtools/launch_samtools.sh my_job_config.sh

  where *my_job_config.sh* is replaced by the name of your config file
  created in step 2.

