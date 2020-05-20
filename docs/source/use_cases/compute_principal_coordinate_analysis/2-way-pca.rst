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

Compute Principal Coordinate Analysis on the Intersection of Two Variant Sets
=============================================================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/compute_principal_coordinate_analysis/2-way-pca.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

.. toctree::
   :maxdepth: 2

.. contents::

`Principal Coordinate Analysis <http://occamstypewriter.org/boboh/2012/01/17/pca_and_pcoa_explained/>`_ counts the number of variants two samples have in common.  These counts are then placed into an ``(N+M)x(N+M)`` matrix where ``N`` is the number of samples in the control variant set (e.g., 1,000 Genomes) and ``M`` is the number of samples in the case variant set.  The matrix is centered, scaled, and then the first two principal components are computed for each individual.

In the two-way version, the variants shared between two variant sets are used to compute PCA among the individuals in both variant sets.  This can be useful, for example, as an ethnicity check when comparing a variant set to 1,000 Genomes.  See codelab `Quality Control using Google Genomics`_ for an example of this.

An `Apache Spark`_ implementation is available.

Setup
-----

.. include:: /includes/spark_setup.rst

Run the job
-----------

The following command will run a two-way PCA over the BRCA1 region within the :doc:`/use_cases/discover_public_data/platinum_genomes` variant set and the :doc:`/use_cases/discover_public_data/1000_genomes` phase 1 variants.

.. code-block:: shell

  spark-submit \
    --class com.google.cloud.genomics.spark.examples.VariantsPcaDriver \
    --conf spark.shuffle.spill=true \
    googlegenomics-spark-examples-assembly-1.0.jar \
    --variant-set-id 10473108253681171589 3049512673186936334 \
    --references 17:41196311:41277499 chr17:41196311:41277499 \
    --output-path gs://YOUR-BUCKET/output/two-way-brca1-pca.tsv

The above command line runs the job over a small portion of the genome, only taking a couple minutes.  If modified to run over a larger portion of the genome or the entire genome, it may take a few hours depending upon how many machines are in the Spark cluster.

To run this job over the entire genome:

* Create a larger cluster: ``gcloud beta dataproc clusters create cluster-2 --scopes cloud-platform --num-workers #``
* Add ``--num-reduce-partitions #`` to be somewhere between 10-20 this will be the level of parallelism when computing the reference call similarity, keep it bounded to a small number, otherwise the shuffle will need to move a full similarity matrix for each reducer.
* Use ``--all-references`` instead of ``--references 17:41196311:41277499 chr17:41196311:41277499`` to run over the entire genome.

To run the job on a different variant set:

* Change the second variant set id for the ``--variant-set-id`` id parameter.
* Update the second value in ``--references`` as appropriate (e.g., add/remove the 'chr' prefix on reference names).
* Increase the memory used when running with a large ``M`` via ``--conf spark.driver.maxResultSize=10G`` and ``--driver-memory 20G``

Additional details
------------------

.. include:: /includes/spark_details.rst

Gather the results into a single file
-------------------------------------

.. code-block:: shell

  gsutil cat gs://YOUR-BUCKET/output/two-way-brca1-pca.tsv* \
    | sort > two-way-brca1-pca.tsv

