Compute Principal Coordinate Analysis
=======================================

.. toctree::
   :maxdepth: 2

.. contents::

Principal Coordinate Analysis counts the number of variants two individuals have in common.  This is then placed into an NxN matrix
where N is the number of samples in the dataset.  The matrix is centered, scaled, and then the first to principal components are computed for each invididual.

Both Spark and Dataflow implementations of each are available.

Spark
-----

Setup
^^^^^

.. include:: ../../includes/spark_setup.rst

Run the job
^^^^^^^^^^^

The following command will run PCA over the the BRCA1 region within the Platinum Genomes dataset.

.. code-block:: shell
  command here

See the source code for implementation details: https://github.com/googlegenomics/spark-examples

Dataflow
--------

Setup
^^^^^

.. include:: ../../includes/dataflow_setup.rst


Run the job
^^^^^^^^^^^

The following command will run PCA over the the BRCA1 region within the Platinum Genomes dataset.

.. code-block:: shell

  java -cp target/google-genomics-dataflow-*.jar \
  com.google.cloud.genomics.dataflow.pipelines.VariantSimilarity \
  --project=YOUR_GOOGLE_CLOUD_PLATFORM_PROJECT_ID \
  --stagingLocation=gs://YOUR_BUCKET/dataflow-staging \
  --genomicsSecretsFile=/PATH/TO/YOUR/client_secrets.json \
  --datasetId=3049512673186936334 \
  --references=chr17:41196311:41277499 \
  --output=gs://YOUR_BUCKET/output/platinum-genomes-brca1-pca.tsv

To run this job on the entire dataset:

* Add ``--runner=DataflowPipelineRunner`` to run the job on Google Cloud instead of locally.
* Use ``--allReferences`` instead of ``--references=chr17:41196311:41277499`` to run over the entire genome.
* To run the job on a different dataset, change the variant set id for the ``--datasetId`` id parameter. (Also, remove the ``--nonVariantSegments`` parameter if the data does not contain them.)

Additional Details
^^^^^^^^^^^^^^^^^^

Use ``--help`` to get more information about the command line options.

.. code-block:: shell

  java -cp google-genomics-dataflow-*.jar \
  com.google.cloud.genomics.dataflow.pipelines.VariantSimilarity --help
  java -cp google-genomics-dataflow-*.jar \
  com.google.cloud.genomics.dataflow.pipelines.VariantSimilarity --help=VariantSimilarity

See the source code for implementation details: https://github.com/googlegenomics/dataflow-java

Gather the results into a single file
-------------------------------------

.. code-block:: shell

  gsutil cat gs://YOUR-BUCKET/output/platinum-genomes-pca.tsv* | sort > platinum-genomes-pca.tsv


