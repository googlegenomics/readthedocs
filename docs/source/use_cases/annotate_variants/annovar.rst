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

Annovar Annotation
==================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/annotate_variants/annovar.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs


If your source data is single-sample VCF, `gVCF`_, or Complete Genomics masterVar format, this page offers some solutions to annotate all variants found within the cohort using `Annovar`_ or similar tools.

(1) First, load your data into Google Genomics and export your variants to BigQuery.  See `Load Genomic Variants`_ for more detail as to how to do this.

(2) Note that merging has occurred during the import process, so each unique variant within the cohort will be a separate record within the variant set, with all calls for that variant nested within the record.  For more information see `Variant Import merge logic details`_.

(3) To create an export file similar to a VCF, run a query like the following and materialize the results to a new table. https://github.com/StanfordBioinformatics/mvp_aaa_codelabs/blob/master/sql/multisample-vcf.sql

(4) Export the table to Cloud Storage and then download it to a Compute Engine instance with sufficient disk space.

(5) Use ``sed`` or another file editing tool to finish the transformation needed.  See also https://github.com/StanfordBioinformatics/mvp_aaa_codelabs/blob/master/bin/bq-to-vcf.py  For example:

 * Add the ``#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT`` header line.
 * Convert commas to tabs.

(6) Then run `Annovar`_ or similar tools on the file(s).

(7) Lastly, import the result of the annotation back into BigQuery for use in your analyses.
