Count Reads
===========

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

  java -cp /PATH/TO/google-genomics-dataflow*runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.CountReads \
    --project=YOUR-GOOGLE-CLOUD-PLATFORM-PROJECT-ID \
    --stagingLocation=gs://YOUR-BUCKET/dataflow-staging \
    --secretsFile=/PATH/TO/YOUR/client_secrets.json \
    --references=chr17:41196311:41277499 \
    --BAMFilePath=gs://genomics-public-data/platinum-genomes/bam/NA12877_S1.bam \
    --output=gs://YOUR-BUCKET/dataflow-output/NA12877-BAM-reads.tsv

The following command will count those same reads but from the `Google Genomics Reads API`_:

.. code-block:: shell

  java -cp /PATH/TO/google-genomics-dataflow*runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.CountReads \
    --project=YOUR-GOOGLE-CLOUD-PLATFORM-PROJECT-ID \
    --stagingLocation=gs://YOUR-BUCKET/dataflow-staging \
    --secretsFile=/PATH/TO/YOUR/client_secrets.json \
    --references=chr17:41196311:41277499 \
    --readGroupSetId=CMvnhpKTFhD3he72j4KZuyc \
    --output=gs://YOUR-BUCKET/dataflow-output/NA12877-API-reads.tsv

You can check your results by ensuring that both of these examples return the answer 45,081 in their output files.

The above command lines run the pipeline over a small portion of the genome, only taking a few minutes.
If modified to run over a larger portion of the genome or the entire genome, it may take a few hours
depending upon how many machines are configured to run concurrently via ``--numWorkers``.

To run this pipeline over a large portion of the genome:

* Add ``--runner=DataflowPipelineRunner`` to run the pipeline on Google Cloud instead of locally.
* Add  ``--numWorkers=#`` for faster processing that will shard the data.
* Add more references:

  #. Use a comma-separated list to run over multiple disjoint regions.  For example to run over `BRCA1`_ and `BRCA2`_ ``--references=chr13:32889610:32973808,chr17:41196311:41277499``
  #. Use ``--allReferences`` instead of ``--references=chr17:41196311:41277499`` to run over the entire genome.

To run the pipeline on a different read group set, change the ``--readGroupSetId`` id parameter.

To run the pipeline over a different BAM file, change ``--BAMFilePath`` parameter.  Set ``--shardBAMReading=false`` if no BAM index file is available.

Additional details
------------------

.. include:: /includes/dataflow_details.rst
