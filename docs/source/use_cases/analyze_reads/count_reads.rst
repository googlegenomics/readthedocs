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

Count Reads
===========

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/analyze_reads/count_reads.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

.. toctree::
   :maxdepth: 2

.. contents::

This simple pipeline counts reads and can be run either against a BAM file
in `Google Cloud Storage`_ or against data accessed via the `Google Genomics Reads API`_.
It demonstrates the decoupling of reads data processing from ways of getting the read data
and shows how to use common classes for getting reads from BAM or API data sources.

The pipeline produces a small text file with the number of reads counted.

The pipeline is implemented on `Google Cloud Dataflow`_.

Setup Dataflow
--------------

.. include:: /includes/collapsible_dataflow_setup_instructions.rst

Run the pipeline
----------------

The following command will count reads from a BAM in `Google Cloud Storage`_,
specifically those in the BRCA1 region for sample NA12877 within the :doc:`/use_cases/discover_public_data/platinum_genomes` dataset:

.. code-block:: shell

  java -Xbootclasspath/p:alpn-boot.jar \
    -cp google-genomics-dataflow-runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.CountReads \
    --references=chr17:41196311:41277499 \
    --BAMFilePath=gs://genomics-public-data/platinum-genomes/bam/NA12877_S1.bam \
    --output=gs://YOUR-BUCKET/dataflow-output/NA12877-BAM-reads.tsv

The following command will count those same reads but from the `Google Genomics Reads API`_:

.. code-block:: shell

  java -Xbootclasspath/p:alpn-boot.jar \
    -cp google-genomics-dataflow-runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.CountReads \
    --references=chr17:41196311:41277499 \
    --readGroupSetId=CMvnhpKTFhD3he72j4KZuyc \
    --output=gs://YOUR-BUCKET/dataflow-output/NA12877-API-reads.tsv

You can check your results by ensuring that both of these examples return the answer 45,081 in their output files.

.. include:: /includes/dataflow_on_gce_run.rst

|dataflowSomeRefs|

|dataflowAllRefs|

To run the pipeline on a different read group set:

* Change the ``--readGroupSetId`` id parameter.
* Update the ``--references`` as appropriate (e.g., add/remove the 'chr' prefix on reference names).

To run the pipeline over a different BAM file:

* Change ``--BAMFilePath`` parameter.  Set ``--shardBAMReading=false`` if no BAM index file is available.
* Update the ``--references`` as appropriate (e.g., add/remove the 'chr' prefix on reference names).

Additional details
------------------

.. include:: /includes/dataflow_details.rst
