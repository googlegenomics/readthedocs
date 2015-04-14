Annotate Variants with Bioconductor
===================================

.. toctree::
   :maxdepth: 2

`Bioconductor`_ provides a convenient way to annotate small regions of the genome.

A more extensive example of variant annotation with `Bioconductor`_ is documented towards the end of codelab  `Data Analysis using Google Genomics <https://github.com/googlegenomics/codelabs/tree/master/R/1000Genomes-BRCA1-analysis/AllModalitiesDemo.md#annotate-variants-with-bioconductor>`_.

To make use of this upon your own data:

(1) First, load your data into Google Genomics.  See :doc:`../load_data/index` for more detail as to how to do this.

(2) If you do not have them already, install the neccessary Bioconductor packages.  See `Using Bioconductor`_ for more detail as to how to do this.

(3) Update the parameters to the ``getVariants`` call the example below to match that of your data and desired genomic region to annotate.

.. code-block:: shell

  require(GoogleGenomics)
  require(VariantAnnotation)
  require(BSgenome.Hsapiens.UCSC.hg19)
  require(TxDb.Hsapiens.UCSC.hg19.knownGene)

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

