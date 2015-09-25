Verify Bam Id
===========

.. toctree::
   :maxdepth: 2

.. contents::

This pipeline tests a set of reads for contamination.  It takes a set of specified ReadGroupSet
of reads to test and statistics on reference allele frequencies for SNPs with a single alternative
from a specified set of VariantSets and combines these to produce an estimate of the amount of
contamination.

Uses the sequence data alone approach described in:
G. Jun, M. Flickinger, K. N. Hetrick, Kurt, J. M. Romm, K. F. Doheny, G. Abecasis, M. Boehnke, and
H. M. Kang, Detecting and Estimating Contamination of Human DNA Samples in Sequencing and Array-Based
Genotype Data, American journal of human genetics doi:10.1016/j.ajhg.2012.09.004 (volume 91 issue 5 pp.839 - 848).
`See here for more details. <http://www.sciencedirect.com/science/article/pii/S0002929712004788>`_

The pipeline is implemented on `Google Cloud Dataflow`_.

Setup Dataflow
--------------

.. include:: /includes/collapsible_dataflow_setup_instructions.rst

Your project must be whitelisted to use gRPC in order to run this pipeline, as it makes use of
gRPC streaming to retrieve data.  `Contact us`_ if you are interested in being whitelisted to test this pipeline and other gRPC tools.

Download ALPN
-------------

Running this pipeline locally requires that you have the ALPN jar that matches your JRE version
on your computer.  See the `ALPN documentation <http://www.eclipse.org/jetty/documentation/9.2.10.v20150310/alpn-chapter.html>`_ for a table of which ALPN jar to use.

You will not need to provide the ALPN flag or jar if you run the pipeline on Google cloud instead of locally.

Run the pipeline
----------------

The following command will calculate the contamination estimate for a given ReadGroupSet and specific region
in the :doc:`/use_cases/discover_public_data/1000_genomes` dataset.  It also uses the VariantSet within :doc:`/use_cases/discover_public_data/1000_genomes` for retrieving the allele frequencies.

.. code-block:: shell

  java -Xbootclasspath/p:PATH/TO/YOUR/alpn-boot-YOUR-ALPN-JAR-VERSION.jar \
    -cp /PATH/TO/google-genomics-dataflow*runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.VerifyBamId \
    --project=YOUR-GOOGLE-CLOUD-PLATFORM-PROJECT-ID \
    --stagingLocation=gs://YOUR-BUCKET/dataflow-staging \
    --secretsFile=/PATH/TO/YOUR/client_secrets.json \
    --references=17:41196311:4127749 \
    --readGroupSetIds=CMvnhpKTFhDq9e2Yy9G-Bg \
    --variantSetIds=10473108253681171589 \
    --output=gs://YOUR-BUCKET/dataflow-output/test-output.txt

The following command will also calculate the contamination estimate in the same manner as the previous
command, but will use the entire :doc:`/use_cases/discover_public_data/1000_genomes` dataset (all ReadGroupSet and the VariantSet within).  This will
take much longer to run.

.. code-block:: shell

  java -Xbootclasspath/p:PATH/TO/YOUR/alpn-boot-YOUR-ALPN-JAR-VERSION.jar \
    -cp /PATH/TO/google-genomics-dataflow*runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.CalculateCoverage \
    --project=YOUR-GOOGLE-CLOUD-PLATFORM-PROJECT-ID \
    --stagingLocation=gs://YOUR-BUCKET/dataflow-staging \
    --secretsFile=/PATH/TO/YOUR/client_secrets.json \
    --references=17:41196311:4127749 \
    --inputDatasetId=10473108253681171589 \
    --output=gs://YOUR-BUCKET/dataflow-output/test-output.txt

The above command lines run the pipeline over a small portion of the genome, only taking a few minutes.
If modified to run over a larger portion of the genome or the entire genome, it may take a few hours
depending upon how many machines are configured to run concurrently via ``--numWorkers``.

To run this pipeline over a large portion of the genome:

* Add ``--runner=DataflowPipelineRunner`` and remove the ALPN jar from the command line to run the pipeline on Google Cloud instead of locally.
* Add ``--numWorkers=#`` for faster processing that will shard the data.
* Add more references:

  #. Use a comma-separated list to run over multiple disjoint regions.  For example to run over `BRCA1`_ and `BRCA2`_ ``--references=13:32889610:32973808,17:41196311:41277499``
  #. Use ``--allReferences`` instead of ``--references=1:552960:557056`` to run over the entire genome.

To run the pipeline on a different dataset, change the ``--inputDatasetId`` parameter.

To run the pipeline on a different group of read group sets and variant sets, change the ``--readGroupSetIds`` and ``--variantSetIds`` parameters.

To configure the pipeline more to fit your needs in terms of the minimum allele frequency to use or the fraction of positions to check, change the ``--minFrequency`` and ``--samplingFraction`` parameters.

Additional details
------------------

.. include:: ../../includes/dataflow_details.rst
