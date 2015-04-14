Compute Principal Coordinate Analysis
=======================================

.. toctree::
   :maxdepth: 2

.. contents::

`Principal Coordinate Analysis <http://occamstypewriter.org/boboh/2012/01/17/pca_and_pcoa_explained/>`_
counts the number of variants two samples have in common.  These counts are then placed into an
``NxN`` matrix where ``N`` is the number of samples in the dataset.  The matrix is centered,
scaled, and then the first two principal components are computed for each invididual.

See the `Data Analysis using Google Genomics codelab <https://github.com/googlegenomics/codelabs/blob/master/R/1000Genomes-BRCA1-analysis/AllModalitiesDemo.md#cluster-computing>`_ for an example that makes use of the results of this analysis run upon `1,000 Genomes`_.

Both `Google Cloud Dataflow`_ and `Apache Spark`_ implementations are available.

Dataflow
--------

Setup
^^^^^^^^^^^^

.. include:: ../../includes/dataflow_setup.rst

.. include:: ../../includes/dataflow_on_gce_setup.rst

Run the job
^^^^^^^^^^^

The following command will run PCA over the BRCA1 region within the `Platinum Genomes`_ dataset.

.. code-block:: shell

  java -cp /PATH/TO/google-genomics-dataflow*.jar \
    com.google.cloud.genomics.dataflow.pipelines.VariantSimilarity \
    --project=YOUR_GOOGLE_CLOUD_PLATFORM_PROJECT_ID \
    --stagingLocation=gs://YOUR_BUCKET/dataflow-staging \
    --genomicsSecretsFile=/PATH/TO/YOUR/client_secrets.json \
    --datasetId=3049512673186936334 \
    --references=chr17:41196311:41277499 \
    --output=gs://YOUR_BUCKET/output/platinum-genomes-brca1-pca.tsv

To run this job over the entire genome:

* Add ``--runner=DataflowPipelineRunner`` to run the job on Google Cloud instead of locally.
* Use ``--allReferences`` instead of ``--references=chr17:41196311:41277499`` to run over the entire genome.
* To run the job on a different dataset, change the variant set id for the ``--datasetId`` id parameter.

Additional details
^^^^^^^^^^^^^^^^^^

.. include:: ../../includes/dataflow_details.rst

Spark
-----

Setup
^^^^^

.. include:: ../../includes/spark_setup.rst

Run the job
^^^^^^^^^^^

The following command will run PCA over the BRCA1 region within the `Platinum Genomes`_ dataset.

.. code-block:: shell

  spark-submit \
    --class com.google.cloud.genomics.spark.examples.VariantsPcaDriver \
    --conf spark.shuffle.spill=true \
    --master spark://hadoop-m:7077 \
    /PATH/TO/googlegenomics-spark-examples-assembly-1.0.jar \
    --client-secrets /PATH/TO/YOUR/client_secrets.json \
    --bases-per-partition 1000000 \
    --variant-set-id 3049512673186936334 \
    --references chr17:41196311:41277499 \
    --output-path gs://YOUR_BUCKET/output/platinum-genomes-brca1-pca.tsv

To run this job over the entire genome:

* Add ``--num-reduce-partitions #`` to be equal to the number of cores in your cluster.
* Use ``--all-references`` instead of ``--references chr17:41196311:41277499`` to run over the entire genome.
* To run the job on a different dataset, change the variant set id for the ``--variant-set-id`` id parameter.

Additional details
^^^^^^^^^^^^^^^^^^

.. include:: ../../includes/spark_details.rst

Gather the results into a single file
-------------------------------------

.. code-block:: shell

  gsutil cat gs://YOUR_BUCKET/output/platinum-genomes-brca1-pca.tsv* \
    | sort > platinum-genomes-brca1-pca.tsv

