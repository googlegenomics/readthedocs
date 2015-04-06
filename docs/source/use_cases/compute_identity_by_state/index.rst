Compute Identity By State
==========================

.. toctree::
   :maxdepth: 2

.. contents::

`Identity-by-State <https://www.youtube.com/watch?v=NRiI1RbE_-I>`_ is a simple similarity measure that describes the alleles shared by two individuals as a single number.

See the `Quality Control using Google Genomics codelab <https://github.com/googlegenomics/codelabs/blob/master/R/PlatinumGenomes-QC/Sample-Level-QC.md#genome-similarity>`_ for an example that makes use of the results of this analysis run upon `Platinum Genomes`_.

A `Google Cloud Dataflow`_ implementation is available.

Setup Dataflow
---------

Local Setup
^^^^^^^^^^^^

.. include:: ../../includes/dataflow_setup.rst

Compute Engine Setup
^^^^^^^^^^^^^^^^^^^^

.. include:: ../../includes/dataflow_on_gce_setup.rst

Run the job
--------------
The following command will run Identity-by-State over the BRCA1 region within the `Platinum Genomes`_ dataset.

.. code-block:: shell

  java -cp /PATH/TO/google-genomics-dataflow*.jar \
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

Additional details
------------------

.. include:: ../../includes/dataflow_details.rst

