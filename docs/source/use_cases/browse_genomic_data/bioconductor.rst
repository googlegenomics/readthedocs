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

.. toctree::
   :maxdepth: 2

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

(2) If you do not have them already, install the necessary `Bioconductor`_ packages.  See `Using Bioconductor`_ for more detail as to how to do this.

(3) Update the parameters to the ``getReads`` call the example above to match that of your data and desired genomic region to view.
