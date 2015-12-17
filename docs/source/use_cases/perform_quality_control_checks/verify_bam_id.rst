Verify Bam Id
==============

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
G. Jun, M. Flickinger, K. N. Hetrick, Kurt, J. M. Romm, K. F. Doheny, G. Abecasis, M. Boehnke, and
H. M. Kang, Detecting and Estimating Contamination of Human DNA Samples in Sequencing and Array-Based
Genotype Data, American journal of human genetics doi:10.1016/j.ajhg.2012.09.004 (volume 91 issue 5 pp.839 - 848).
`See here for more details. <http://www.sciencedirect.com/science/article/pii/S0002929712004788>`_

The pipeline is implemented on `Google Cloud Dataflow`_.

Setup Dataflow
--------------

.. include:: /includes/collapsible_dataflow_setup_instructions.rst

Run the pipeline
----------------

The following command will calculate the contamination estimate for a given ReadGroupSet and specific region
in the :doc:`/use_cases/discover_public_data/1000_genomes` dataset.  It also uses the VariantSet within :doc:`/use_cases/discover_public_data/1000_genomes` for retrieving the allele frequencies.

.. code-block:: shell

  java -Xbootclasspath/p:PATH/TO/YOUR/alpn-boot-YOUR-ALPN-JAR-VERSION.jar \
    -cp /PATH/TO/google-genomics-dataflow*runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.VerifyBamId \
    --references=17:41196311:4127749 \
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
