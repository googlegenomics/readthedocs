Count Reads
===========

.. toctree::
   :maxdepth: 2

.. contents::

*a sentence or two about the task this job is accomplishing; counting reads in GCS BAMs or in the API*

*a sentence or two about the results of this job in action, how do people use this in their work?*

A `Google Cloud Dataflow`_ implementation is available.

Setup Dataflow
---------

.. include:: ../../includes/dataflow_setup.rst

.. include:: ../../includes/dataflow_on_gce_setup.rst

Run the job
--------------

The following command will run *what* over *which small genomic region* within the *which* dataset.

The following command will count reads from a BAM in `Google Cloud Storage`_, specifically those in the BRCA1 region for sample NA12877 within the `Platinum Genomes`_ dataset:

.. code-block:: shell

  java -cp /PATH/TO/google-genomics-dataflow*.jar \
    com.google.cloud.genomics.dataflow.pipelines.CountReads \
    --project=YOUR-GOOGLE-CLOUD-PLATFORM-PROJECT-ID \
    --stagingLocation=gs://YOUR-BUCKET/dataflow-staging \
    --genomicsSecretsFile=/PATH/TO/YOUR/client_secrets.json \
    --references=chr17:41196311:41277499 \
    --BAMFilePath=gs://genomics-public-data/platinum-genomes/bam/NA12877_S1.bam

The following command will count those same reads but from the `Google Genomics Reads API`_:

.. code-block:: shell

  java -cp /PATH/TO/google-genomics-dataflow*.jar \
    com.google.cloud.genomics.dataflow.pipelines.CountReads \
    --project=YOUR-GOOGLE-CLOUD-PLATFORM-PROJECT-ID \
    --stagingLocation=gs://YOUR-BUCKET/dataflow-staging \
    --genomicsSecretsFile=/PATH/TO/YOUR/client_secrets.json \
    --references=chr17:41196311:41277499 \
    --datasetId=3049512673186936334 \
    --readGroupSetId=$READGROUPSET_ID

*any other pipeline-specific details we wish to highlight here?*

To run this job over a large portion of the genome:

  #. add ``--runner=DataflowPipelineRunner`` to run the job on Google Cloud instead of locally
  #. add more references

    * Use a comma-separated list to run over multiple disjoint regions.  For example to run over `BRCA1`_ and `BRCA2`_ ``--references=chr13:32889610:32973808,chr17:41196311:41277499``
    * Use ``--allReferences`` instead of ``--references=chr17:41196311:41277499`` to run over the entire genome.

To run the job on a different dataset, change the variant set id for the ``--datasetId`` id parameter.

Additional details
------------------

.. include:: ../../includes/dataflow_details.rst
