Run Picard and GATK tools on Cloud-Resident Genomic Data
=========================================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/run_picard_and_gatk/index.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

`Picard`_ and `GATK`_ tools are popular utilities used for genomics analysis and
processing pipelines.

They usually work with BAM files but we are working on teaching them to work
with the genomic data in the cloud.

If your dataset is loaded into a cloud provider supporting `GA4GH`_ API
(e.g. `Google Genomics`_) or you want to use one of
the available datasets from :doc:`/use_cases/discover_public_data/index`,
you can check out `gatk-tools-java`_
library that makes it possible to run some Picard tools against genomic data
in the cloud.

It is now also possible to make a special build of `Picard`_ tools
that will have this support built in by default.

See https://github.com/broadinstitute/picard/blob/master/README.md for details.
