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

Compute Principal Coordinate Analysis
=======================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/compute_principal_coordinate_analysis/1-way-pca.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

.. toctree::
   :maxdepth: 2

.. contents::

`Principal Coordinate Analysis <http://occamstypewriter.org/boboh/2012/01/17/pca_and_pcoa_explained/>`_
counts the number of variants two samples have in common.  These counts are then placed into an
``NxN`` matrix where ``N`` is the number of samples in the variant set.  The matrix is centered,
scaled, and then the first two principal components are computed for each individual.

See the `Data Analysis using Google Genomics codelab <https://github.com/googlegenomics/codelabs/blob/master/R/1000Genomes-BRCA1-analysis/AllModalitiesDemo.md#cluster-computing>`_ for an example that makes use of the results of this analysis run upon :doc:`/use_cases/discover_public_data/1000_genomes`.

Both `Google Cloud Dataflow`_ and `Apache Spark`_ implementations are available.

Dataflow
--------

Setup
^^^^^

.. include:: /includes/collapsible_dataflow_setup_instructions.rst

Run the pipeline
^^^^^^^^^^^^^^^^

The following command will run PCA over the BRCA1 region within the :doc:`/use_cases/discover_public_data/platinum_genomes` variant set.

.. code-block:: shell

  java -Xbootclasspath/p:alpn-boot.jar \
    -cp google-genomics-dataflow-runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.VariantSimilarity \
    --variantSetId=3049512673186936334 \
    --references=chr17:41196311:41277499 \
    --output=gs://YOUR-BUCKET/dataflow-output/platinum-genomes-brca1-pca.tsv

.. include:: /includes/dataflow_on_gce_run.rst

|dataflowSomeRefs|

|dataflowAllRefs|

To run the pipeline on a different variant set:

* Change the variant set id for the ``--variantSetId`` id parameter.
* Update the ``--references`` as appropriate (e.g., add/remove the 'chr' prefix on reference names).

Additional details
^^^^^^^^^^^^^^^^^^

.. include:: /includes/dataflow_details.rst

Spark
-----

Setup
^^^^^

.. include:: /includes/spark_setup.rst

Run the job
^^^^^^^^^^^

The following command will run PCA over the BRCA1 region within the :doc:`/use_cases/discover_public_data/platinum_genomes` variant set.

.. code-block:: shell

  spark-submit \
    --class com.google.cloud.genomics.spark.examples.VariantsPcaDriver \
    --conf spark.shuffle.spill=true \
    googlegenomics-spark-examples-assembly-1.0.jar \
    --variant-set-id 3049512673186936334 \
    --references chr17:41196311:41277499 \
    --output-path gs://YOUR-BUCKET/output/platinum-genomes-brca1-pca.tsv

The above command line runs the job over a small portion of the genome, only taking a couple minutes.  If modified to run over a larger portion of the genome or the entire genome, it may take a few hours depending upon how many machines are in the Spark cluster.

To run this job over a large portion of the genome or the entire genome:

* Create a larger cluster: ``gcloud beta dataproc clusters create cluster-2 --scopes cloud-platform --num-workers #``
* Add ``--num-reduce-partitions #`` to be equal to the number of cores in your cluster.
* Use a comma-separated list to run over multiple disjoint regions.  For example to run over `BRCA1`_ and `BRCA2`_ ``--references chr13:32889610:32973808,chr17:41196311:41277499``.
* Use ``--all-references`` instead of ``--references chr17:41196311:41277499`` to run over the entire genome.

To run the job on a different variant set:

* Change the variant set id for the ``--variant-set-id`` id parameter.
* Update the ``--references`` as appropriate (e.g., add/remove the 'chr' prefix on reference names).

Additional details
^^^^^^^^^^^^^^^^^^

.. include:: /includes/spark_details.rst

Gather the results into a single file
-------------------------------------

.. code-block:: shell

  gsutil cat gs://YOUR-BUCKET/output/platinum-genomes-brca1-pca.tsv* \
    | sort > platinum-genomes-brca1-pca.tsv

