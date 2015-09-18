Annotate Variants with Google Genomics
======================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/annotate_variants/google_genomics_annotation.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

.. toctree::
   :maxdepth: 2

.. contents::

Variant annotation is a mechanism for finding and filtering interesting variants in a given variant set.

An annotated variant set might be used to identify variants which affect a gene of interest, or to highlight potential rare variants in an individual.

A `Google Cloud Dataflow`_ implementation is available.

Setup Dataflow
--------------

.. include:: /includes/collapsible_dataflow_setup_instructions.rst

Run the pipeline
----------------

The following command will use `ClinVar`_ to annotate variants in the `BRCA1`_ gene within the :doc:`/use_cases/discover_public_data/platinum_genomes` dataset for individual NA12877.

**Disclaimer:** This program is currently intended to be a *sample*, and provides only a small subset of functionality found in most variant annotation programs. `Pull requests <https://github.com/googlegenomics/dataflow-java>`_ are welcome!

.. code-block:: shell

  java -cp /PATH/TO/google-genomics-dataflow*runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.AnnotateVariants \
    --project=YOUR-GOOGLE-CLOUD-PLATFORM-PROJECT-ID \
    --stagingLocation=gs://YOUR-BUCKET/dataflow-staging \
    --secretsFile=/PATH/TO/YOUR/client_secrets.json \
    --datasetId=3049512673186936334 \
    --references=chr17:41196311:41277499 \
    --transcriptSetIds=CIjfoPXj9LqPlAEQ5vnql4KewYuSAQ \
    --variantAnnotationSetIds=CILSqfjtlY6tHxC0nNH-4cu-xlQ \
    --callSetIds=3049512673186936334-0 \
    --output=gs://YOUR-BUCKET/output/platinum-genomes-brca1-clinvar-annotation.tsv

Note that this program accepts `VariantSets` and `AnnotationSets` as input. The analogous inputs to traditional variant annotation programs are `VCF` and `.csv` files, respectively.  To run the pipeline on a different `VariantSet` change the variant set id for the ``--datasetId`` id parameter and:

 * update the ``--callSetIds`` parameter accordingly
 * see :doc:`../discover_public_data/clinvar_annotations` if the variants were aligned to GRCh38 instead of GRCh37/hg19 and update ``--variantAnnotationSetIds``
 * see :doc:`../discover_public_data/ucsc_annotations` if the variants were aligned to GRCh38 instead of GRCh37/hg19 and update ``--transcriptSetIds``

The above command line runs the pipeline over a small portion of the genome, only taking a few minutes.  If modified to run over a larger portion of the genome or the entire genome, it may take a few hours depending upon how many machines are configured to run concurrently via ``--numWorkers``.  To run this pipeline over a large portion of the genome:

  #. add ``--runner=DataflowPipelineRunner`` to run the pipeline on Google Cloud instead of locally
  #. add more references

    * Use a comma-separated list to run over multiple disjoint regions.  For example to run over `BRCA1`_ and `BRCA2`_ ``--references=chr13:32889610:32973808,chr17:41196311:41277499``
    * Use ``--allReferences`` instead of ``--references=chr17:41196311:41277499`` to run over the entire genome.

Gather the results into a single file
-------------------------------------

.. code-block:: shell

  gsutil cat gs://YOUR-BUCKET/output/platinum-genomes-brca1-clinvar-annotation.tsv* \
    | sort > platinum-genomes-brca1-clinvar-annotation.tsv

Additional details
------------------

.. include:: /includes/dataflow_details.rst
