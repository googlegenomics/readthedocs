.. _samtools: http://www.htslib.org/

.. |br| raw:: html

   <br />

=============================================
Run SAMtools on files in Google Cloud Storage
=============================================

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

3. .. include:: /includes/grid-computing-tools-steps-upload-source.rst

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
   * OUTPUT_PATH: GCS path indicating where to upload the output files
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

If all of your input files appear in a single directory, then the easiest way
to generate a file list is with ``gsutil``. For example:

.. code-block:: shell

  gsutil ls gs://MY_BUCKET/PATH/*.vcf.bz2 > ${WS_ROOT}/my_jobs/bam_indexing_list_file.txt
  
2. **Create a** ``job config file``

The easiest way to create a job config file is to base it off the appropriate sample and update

* INPUT_LIST_FILE
* OUTPUT_PATH
* OUTPUT_LOG_PATH

3. .. include:: /includes/grid-computing-tools-steps-sizing-disks.rst

4. .. include:: /includes/grid-computing-tools-steps-upload-your-config.rst

5. **Do a "dry run"** (*optional*)

The ``samtools`` tool supports the DRYRUN environment variable.
Setting this value to 1 when launching your job will cause the queued job to
execute *without downloading or uploading* any files.

The local output files, however, will be populated with useful information about
what files *would* be copied. This can be useful for ensuring your file list
is valid and that the output path is correct.

For example:

.. code-block:: shell

   $ DRYRUN=1 ./src/samtools/launch_samtools.sh ./samples/samtools/samtools_config.sh
   Your job-array 5.1-6:1 ("samtools") has been submitted

Then after waiting for the job to complete, inspect:

** FIXME: add real output here:

.. code-block:: shell

   $ head -n 5 samtools.o3.1 
   Task host: compute001
   Task start: 1
   Input list file: ./samples/samtools/samtools_index_file_list.txt
   Output path: gs://cookbook-bucket/bigtools/output_path/samtools_index
   Output log path: gs://cookbook-bucket/bigtools/log_path/samtools_index

   $ grep "^Will download:" samtools.o5.*
   samtools.o5.1:Will download: gs://genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/technical/pilot2_high_cov_GRCh37_bams/data/NA12878/alignment/NA12878.chrom9.SOLID.bfast.CEU.high_coverage.20100125.bam to /scratch/samtools.5.1/in/
   samtools.o5.2:Will download: gs://genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/technical/pilot2_high_cov_GRCh37_bams/data/NA12878/alignment/NA12878.chrom1.LS454.ssaha2.CEU.high_coverage.20100311.bam to /scratch/samtools.5.2/in/
   samtools.o5.3:Will download: gs://genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/pilot_data/data/NA12878/alignment/NA12878.chrom11.SOLID.corona.SRP000032.2009_08.bam to /scratch/samtools.5.3/in/
   samtools.o5.4:Will download: gs://genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/pilot_data/data/NA12878/alignment/NA12878.chrom12.SOLID.corona.SRP000032.2009_08.bam to /scratch/samtools.5.4/in/
   samtools.o5.5:Will download: gs://genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/pilot_data/data/NA12878/alignment/NA12878.chrom10.SOLID.corona.SRP000032.2009_08.bam to /scratch/samtools.5.5/in/
   samtools.o5.6:Will download: gs://genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/pilot_data/data/NA12878/alignment/NA12878.chromX.SOLID.corona.SRP000032.2009_08.bam to /scratch/samtools.5.6/in/

6. **Launch the job**

  SSH to the master instance
 
  .. code-block:: shell

    elasticluster ssh gridengine

  Run the launch script, passing in the config file:

  .. code-block:: shell

    ./src/samtools/launch_samtools.sh my_job_config.sh
  
  where *my_job_config.sh* is replaced by the name of your config file
  created in step 2.

