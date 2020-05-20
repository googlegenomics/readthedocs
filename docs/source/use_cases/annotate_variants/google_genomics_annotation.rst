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

The following command will use `ClinVar`_ to annotate variants on a portion of chromosome 17 within the :doc:`/use_cases/discover_public_data/platinum_genomes` dataset for individual NA12877.

**Disclaimer:** This program is currently intended to be a *sample*, and provides only a small subset of functionality found in most variant annotation programs. `Pull requests <https://github.com/googlegenomics/dataflow-java>`_ are welcome!

.. code-block:: shell

  java -Xbootclasspath/p:alpn-boot.jar \
    -cp google-genomics-dataflow-runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.AnnotateVariants \
    --variantSetId=3049512673186936334 \
    --references=chr17:40700000:40800000 \
    --transcriptSetIds=CIjfoPXj9LqPlAEQ5vnql4KewYuSAQ \
    --variantAnnotationSetIds=CILSqfjtlY6tHxC0nNH-4cu-xlQ \
    --callSetIds=3049512673186936334-0 \
    --output=gs://YOUR-BUCKET/dataflow-output/platinum-genomes-chr17region-annotation.tsv

You can check your results by ensuring that the following three results are contained in the output files::

  chr17:40714803:A:CI7s77ro84KpKhIFY2hyMTcYs4S1EyDwuoPB1PDR19AB: [{alternateBases=A, effect=NONSYNONYMOUS_SNP, geneId=ChYIiN-g9eP0uo-UARDi_aPt7qzv9twBEgIxNxjr_rQTIJrU8My-4_2UdA, transcriptIds=[ChYIiN-g9eP0uo-UARDm-eqXgp7Bi5IBEgIxNxjr_rQTII_53bW3_PSh6AE], type=SNP}]
  chr17:40722028:G:CI7s77ro84KpKhIFY2hyMTcY7Ly1EyDvqeCryb2xrQw: [{alternateBases=G, effect=NONSYNONYMOUS_SNP, geneId=ChYIiN-g9eP0uo-UARDi_aPt7qzv9twBEgIxNxjlpbUTIL3v58KG8MzFJw, transcriptIds=[ChYIiN-g9eP0uo-UARDm-eqXgp7Bi5IBEgIxNxjlpbUTIMvX96zMvJyV0gE], type=SNP}]
  chr17:40706905:A:CI7s77ro84KpKhIFY2hyMTcY2ca0EyCw4NnN8qzS8S0: [{alternateBases=A, effect=NONSYNONYMOUS_SNP, geneId=ChYIiN-g9eP0uo-UARDi_aPt7qzv9twBEgIxNxjvr7QTIITZ6M7yo8CnbA, transcriptIds=[ChYIiN-g9eP0uo-UARDm-eqXgp7Bi5IBEgIxNxjvr7QTINX5koLhyJHYkwE], type=SNP}]

.. include:: /includes/dataflow_on_gce_run.rst

|dataflowSomeRefs|

|dataflowAllRefs|

Note that this program accepts `VariantSets` and `AnnotationSets` as input. The analogous inputs to traditional variant annotation programs are `VCF` and `.csv` files, respectively.  To run the pipeline on a different `VariantSet` change the ``--variantSetId`` id parameter and:

 * update the ``--callSetIds`` parameter accordingly
 * see :doc:`../discover_public_data/clinvar_annotations` if the variants were aligned to GRCh38 instead of GRCh37/hg19 and update ``--variantAnnotationSetIds``
 * see :doc:`../discover_public_data/ucsc_annotations` if the variants were aligned to GRCh38 instead of GRCh37/hg19 and update ``--transcriptSetIds``

Gather the results into a single file
-------------------------------------

.. code-block:: shell

  gsutil cat gs://YOUR-BUCKET/output/platinum-genomes-brca1-clinvar-annotation.tsv* \
    | sort > platinum-genomes-brca1-clinvar-annotation.tsv

Additional details
------------------

.. include:: /includes/dataflow_details.rst
