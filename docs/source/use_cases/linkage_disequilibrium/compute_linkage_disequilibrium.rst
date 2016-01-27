Compute Linkage Disequilibrium on a Variant Set
=======================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/linkage_disequilibrium/compute_linkage_disequilibrium.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

.. toctree::
   :maxdepth: 2

.. contents::

This pipeline calculates linkage disequilibrium between pairs of variants in a Variant Set. It takes as input:

* a VariantSet for which the linkage disequilibrium values will be calculated

and calculates the D' and allelic correlation measures of linkage disequilibrium, defined in
Box 1 of:

| `Linkage disequilibrium — understanding the evolutionary past and mapping the medical future <http://www.nature.com/nrg/journal/v9/n6/full/nrg2361.html>`_
| Slatkin, Montgomery
| Nature Reviews Genetics, Volume 9, Issue 6, 477 - 485
| DOI: http://dx.doi.org/10.1038/nrg2361
|

The pipeline is implemented on `Google Cloud Dataflow`_.

Setup Dataflow
--------------

.. include:: /includes/collapsible_dataflow_setup_instructions.rst

Run the pipeline
----------------

The following command will calculate linkage disequilibrium between all pairs of variants within 50,000 base pairs of each other for a specific region in the :doc:`/use_cases/discover_public_data/1000_genomes` Phase 3 VariantSet, and retain results for all pairs that have an absolute value of their allelic correlation of at least 0.4.

.. code-block:: shell

  java -Xbootclasspath/p:PATH/TO/YOUR/alpn-boot-YOUR-ALPN-JAR-VERSION.jar \
    -cp /PATH/TO/linkage-disequilibrium*runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.LinkageDisequilibrium \
    --variantSetId=11027761582969783635 \
    --references=17:41196311:41277499 \
    --window=50000 \
    --ldCutoff=0.4 \
    --output=gs://YOUR-BUCKET/dataflow-output/linkage-disequilibrium-1000G_Phase_3-BRCA1.txt

.. include:: /includes/dataflow_on_gce_run.rst

|dataflowSomeRefs|

|dataflowAllRefs|

To run the pipeline on a subset of individuals in a VariantSet:
* Add a ``--callSetsToUse`` flag that has a comma-delimited list of call sets to include.

Additional details
------------------

.. include:: ../../includes/dataflow_details.rst
