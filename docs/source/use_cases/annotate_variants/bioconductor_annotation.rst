Bioconductor Annotation
=======================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/annotate_variants/bioconductor_annotation.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

.. toctree::
   :maxdepth: 2

`Bioconductor`_ provides a convenient way to annotate small regions of the genome.

.. code-block:: shell

  require(GoogleGenomics)
  require(VariantAnnotation)
  require(BSgenome.Hsapiens.UCSC.hg19)
  require(TxDb.Hsapiens.UCSC.hg19.knownGene)

  GoogleGenomics::authenticate("/PATH/TO/YOUR/client_secrets.json")

  variants <- getVariants(datasetId="10473108253681171589", chromosome="17", start=41196311, end=41277499)
  granges <- variantsToGRanges(variants)

  txdb <- TxDb.Hsapiens.UCSC.hg19.knownGene
  codingVariants <- locateVariants(granges, txdb, CodingVariants())
  codingVariants

  coding <- predictCoding(rep(granges, elementLengths(granges$ALT)),
                          txdb,
                          seqSource=Hsapiens,
                          varAllele=unlist(granges$ALT, use.names=FALSE))
  coding

A more extensive example of variant annotation with `Bioconductor`_ is documented towards the end of codelab  `Data Analysis using Google Genomics <https://github.com/googlegenomics/codelabs/tree/master/R/1000Genomes-BRCA1-analysis/AllModalitiesDemo.md#annotate-variants-with-bioconductor>`__.

To make use of this upon your own data:

(1) First, load your data into Google Genomics.  See :doc:`/use_cases/load_data/index` for more detail as to how to do this.

(2) If you do not have them already, install the necessary Bioconductor packages.  See `Using Bioconductor`_ for more detail as to how to do this.

(3) Update the parameters to the ``getVariants`` call the example above to match that of your data and desired genomic region to annotate.
