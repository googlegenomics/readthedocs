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

Perform Quality Control Checks on Reads
=======================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/perform_quality_control_checks/verify_bam_id.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

.. toctree::
   :maxdepth: 2

.. contents::

This pipeline tests a set of reads for contamination. It takes as input:

* a set of ReadGroupSets to test
* statistics on reference allele frequencies for SNPs with a single alternative from a set of VariantSets

and combines these to produce an estimate of the amount of contamination.

Uses the sequence data alone approach described in:

| `Detecting and Estimating Contamination of Human DNA Samples in Sequencing and Array-Based Genotype Data <http://www.sciencedirect.com/science/article/pii/S0002929712004788>`_
| Jun, Goo et al.
| The American Journal of Human Genetics, Volume 91, Issue 5, 839 - 848
| DOI: http://dx.doi.org/10.1016/j.ajhg.2012.09.004
|

The pipeline is implemented on `Google Cloud Dataflow`_.

Setup Dataflow
--------------

**Note: this pipeline is new and still** `undergoing testing <https://github.com/googlegenomics/dataflow-java/issues/155>`_.  We recommend that you follow the instructions `here <https://github.com/googlegenomics/dataflow-java>`__ to build the latest version of the source code.

.. include:: /includes/collapsible_dataflow_setup_instructions.rst

Run the pipeline
----------------

The following command will calculate the contamination estimate for a given ReadGroupSet and specific region
in the :doc:`/use_cases/discover_public_data/1000_genomes` dataset.  It also uses the VariantSet within :doc:`/use_cases/discover_public_data/1000_genomes` for retrieving the allele frequencies.

.. code-block:: shell

  java -Xbootclasspath/p:alpn-boot.jar \
    -cp google-genomics-dataflow-runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.VerifyBamId \
    --references=17:41196311:41277499 \
    --readGroupSetIds=CMvnhpKTFhDq9e2Yy9G-Bg \
    --variantSetId=10473108253681171589 \
    --output=gs://YOUR-BUCKET/dataflow-output/verifyBamId-platinumGenomes-BRCA1-readGroupSet-CMvnhpKTFhCAv6TKo6Dglgg.txt

.. include:: /includes/dataflow_on_gce_run.rst

|dataflowSomeRefs|

|dataflowAllRefs|

To run the pipeline on a different group of read group sets:
* Change the ``--readGroupSetIds`` or the ``--inputDatasetId`` parameter.
* Update the ``--references`` as appropriate (e.g., add/remove the 'chr' prefix on reference names).

To configure the pipeline more to fit your needs in terms of the minimum allele frequency to use or the fraction of positions to check, change the ``--minFrequency`` and ``--samplingFraction`` parameters.

Additional details
------------------

.. include:: ../../includes/dataflow_details.rst
