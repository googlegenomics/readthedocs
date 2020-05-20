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

Compute Identity By State
==========================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/compute_identity_by_state/index.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

.. toctree::
   :maxdepth: 2

.. contents::

`Identity-by-State <https://www.youtube.com/watch?v=NRiI1RbE_-I>`_ is a simple similarity measure that describes the alleles shared by two individuals as a single number.

See the `Quality Control using Google Genomics codelab <https://github.com/googlegenomics/codelabs/blob/master/R/PlatinumGenomes-QC/Sample-Level-QC.md#genome-similarity>`_ for an example that makes use of the results of this analysis run upon :doc:`/use_cases/discover_public_data/platinum_genomes`.

A `Google Cloud Dataflow`_ implementation is available.

Setup Dataflow
--------------

.. include:: /includes/collapsible_dataflow_setup_instructions.rst

Run the pipeline
----------------
The following command will run Identity-by-State over the BRCA1 region within the :doc:`/use_cases/discover_public_data/platinum_genomes` variant set.

.. code-block:: shell

  java -Xbootclasspath/p:alpn-boot.jar \
    -cp google-genomics-dataflow-runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.IdentityByState \
    --variantSetId=3049512673186936334 \
    --references=chr17:41196311:41277499 \
    --hasNonVariantSegments \
    --output=gs://YOUR-BUCKET/dataflow-output/platinum-genomes-brca1-ibs.tsv

Note that there are several IBS calculators from which to choose. Use the ``--callSimilarityCalculatorFactory`` to switch between them.

Also notice use of the ``--hasNonVariantSegments`` parameter when running this pipeline on the :doc:`/use_cases/discover_public_data/platinum_genomes` variant set.

 * For data with non-variant segments (such as Complete Genomics data or data in Genome VCF (gVCF) format), specify this flag so that the pipeline correctly takes into account non-variant segment records that overlap variants within the variant set.
 * The source :doc:`/use_cases/discover_public_data/platinum_genomes` data imported into `Google Genomics`_ was in gVCF format.

.. include:: /includes/dataflow_on_gce_run.rst

|dataflowSomeRefs|

|dataflowAllRefs|

To run the pipeline on a different variant set:

* Change the variant set id for the ``--variantSetId`` id parameter.
* Update the ``--references`` as appropriate (e.g., add/remove the 'chr' prefix on reference names).
* Remove the ``--nonVariantSegments`` parameter if it is not applicable.

Gather the results into a single file
-------------------------------------

.. code-block:: shell

  gsutil cat gs://YOUR-BUCKET/output/platinum-genomes-brca1-ibs.tsv* \
    | sort > platinum-genomes-brca1-ibs.tsv

Additional details
------------------

.. include:: /includes/dataflow_details.rst

