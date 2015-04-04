Compute Identity By State
==========================

.. toctree::
   :maxdepth: 2

.. contents::

Dataflow setup
--------------

.. include:: ../../includes/dataflow_setup.rst

Run the job
--------------
The following command will run Identity-by-State over the the BRCA1 region within the Platinum Genomes dataset.

.. code-block:: shell

  java -cp target/google-genomics-dataflow-*.jar \
  com.google.cloud.genomics.dataflow.pipelines.IdentityByState \
  --project=YOUR_GOOGLE_CLOUD_PLATFORM_PROJECT_ID \
  --stagingLocation=gs://YOUR_BUCKET/dataflow-staging \
  --genomicsSecretsFile=/PATH/TO/YOUR/client_secrets.json \
  --datasetId=3049512673186936334 \
  --references=chr17:41196311:41277499 \
  --hasNonVariantSegments \
  --output=gs://YOUR_BUCKET/output/platinum-genomes-brca1-ibs.tsv

Note that there are several IBS calculators from which to choose. Use the ``--callSimilarityCalculatorFactory`` to switch between them.

To run this job on the entire dataset:

* Add ``--runner=DataflowPipelineRunner`` to run the job on Google Cloud instead of locally.
* Use ``--allReferences`` instead of ``--references=chr17:41196311:41277499`` to run over the entire genome.
* To run the job on a different dataset, change the variant set id for the ``--datasetId`` id parameter. (Also, remove the ``--nonVariantSegments`` parameter if the data does not contain them.)

Gather the results into a single file
-------------------------------------

.. code-block:: shell

  gsutil cat gs://YOUR-BUCKET/output/platinum-genomes-ibs.tsv* | sort > platinum-genomes-ibs.tsv

Additional Details
------------------

Use ``--help`` to get more information about the command line options.

.. code-block:: shell

  java -cp google-genomics-dataflow-*.jar \
  com.google.cloud.genomics.dataflow.pipelines.IdentityByState --help
  java -cp google-genomics-dataflow-*.jar \
  com.google.cloud.genomics.dataflow.pipelines.IdentityByState --help=IdentityByState

See the source code for implementation details: https://github.com/googlegenomics/dataflow-java

