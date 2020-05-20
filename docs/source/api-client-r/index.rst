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
The R client
------------

The `GoogleGenomics Bioconductor package`_ provides R methods to search for and retreive Reads and Variants stored in the Google Genomics API.

Additionally it provides converters to `Bioconductor`_ datatypes such as:

* `GAlignments <http://www.bioconductor.org/packages/release/bioc/html/GenomicAlignments.html>`_
* `GRanges <http://www.bioconductor.org/packages/release/bioc/html/GenomicRanges.html>`_
* `VRanges <http://www.bioconductor.org/packages/release/bioc/html/VariantAnnotation.html>`_
