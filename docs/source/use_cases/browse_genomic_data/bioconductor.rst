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

Browse Reads with Bioconductor
==============================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/browse_genomic_data/bioconductor.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

`Bioconductor`_ provides a convenient way to browse regions of the genome. |browse-reads|

.. code-block:: shell

  require(ggbio)
  require(GoogleGenomics)

  GoogleGenomics::authenticate("/PATH/TO/YOUR/client_secrets.json")

  galignments <- getReads(readGroupSetId="CMvnhpKTFhDnk4_9zcKO3_YB", chromosome="17",
                          start=41218200, end=41218500, converter=readsToGAlignments)
  strand_plot <- autoplot(galignments, aes(color=strand, fill=strand))
  coverage_plot <- ggplot(as(galignments, "GRanges")) + stat_coverage(color="gray40",
                                                      fill="skyblue")
  tracks(strand_plot, coverage_plot, xlab="chr17")

.. |browse-reads| image:: https://raw.githubusercontent.com/googlegenomics/codelabs/master/R/1000Genomes-BRCA1-analysis/figure/alignments-1.png

A more extensive example of read browsing with `Bioconductor`_ is documented towards the end of codelab  `Data Analysis using Google Genomics <https://github.com/googlegenomics/codelabs/blob/master/R/1000Genomes-BRCA1-analysis/AllModalitiesDemo.md#visualize-reads-with-bioconductor>`__.

To make use of this upon your own data:

(1) First, load your data into `Google Genomics`_.  See :doc:`/use_cases/load_data/index` for more detail as to how to do this.

(2) If you do not have them already, install the necessary `Bioconductor`_ packages.  See `Using Bioconductor`_ for more detail as to how to do this.  Alternatively, you can :doc:`/use_cases/run_familiar_tools/bioconductor`.

(3) Update the parameters to the ``getReads`` call the example above to match that of your data and desired genomic region to view.
