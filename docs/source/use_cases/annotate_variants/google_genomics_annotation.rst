Annotate Variants with Google Genomics
======================================

.. toctree::
   :maxdepth: 2

.. contents::

Variant annotation is a mechanism for finding and filtering interesting variants in a given variant set.

An annotated variant set might be used to identify variants which affect a gene of interest, or to highlight potential rare variants in an individual.

A `Google Cloud Dataflow`_ implementation is available.

Setup Dataflow
---------

.. include:: ../../includes/dataflow_setup.rst

.. include:: ../../includes/dataflow_on_gce_setup.rst

Run the job
-----------

The following command will use `ClinVar`_ to annotate variants in the `BRCA1`_ gene within the `Platinum Genomes`_ dataset for individual NA12877.

**Disclaimer:** This program is currently intended to be a *sample*, and provides only a small subset of functionality found in most variant annotation programs. `Pull requests <https://github.com/googlegenomics/dataflow-java>`_ are welcome!

.. code-block:: shell

  java -cp /PATH/TO/google-genomics-dataflow*.jar \
    com.google.cloud.genomics.dataflow.pipelines.AnnotateVariants \
    --project=YOUR_GOOGLE_CLOUD_PLATFORM_PROJECT_ID \
    --stagingLocation=gs://YOUR_BUCKET/dataflow-staging \
    --genomicsSecretsFile=/PATH/TO/YOUR/client_secrets.json \
    --datasetId=3049512673186936334 \
    --references=chr17:41196311:41277499 \
    --transcriptSetIds=CIjfoPXj9LqPlAEQ6Mm91Ya458eqAQ \
    --variantAnnotationSetIds=CILSqfjtlY6tHxC0nNH-4cu-xlQ \
    --callSetIds=3049512673186936334-0 \
    --output=gs://YOUR_BUCKET/output/platinum-genomes-brca1-clinvar-annotation.tsv

Note that this program accepts `VariantSets` and `AnnotationSets` as input. The analogous inputs to traditional variant annotation programs are `VCF` and `.csv` files, respectively.

To run this job over the entire genome:

* Add ``--runner=DataflowPipelineRunner`` to run the job on Google Cloud instead of locally.
* Use ``--allReferences`` instead of ``--references=chr17:41196311:41277499`` to run over the entire genome.
* To run the job on a different dataset, change the variant set id for the ``--datasetId`` id parameter and update the ``--callSetIds`` parameter accordingly.

Gather the results into a single file
-------------------------------------

.. code-block:: shell

  gsutil cat gs://YOUR_BUCKET/output/platinum-genomes-brca1-clinvar-annotation.tsv* \
    | sort > platinum-genomes-brca1-clinvar-annotation.tsv

Additional details
------------------

.. include:: ../../includes/dataflow_details.rst
