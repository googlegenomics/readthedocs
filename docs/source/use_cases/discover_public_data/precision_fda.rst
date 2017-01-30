PrecisionFDA Truth Challenge
============================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/precision_fda.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

This dataset includes both:

* the input for the `PrecisionFDA Truth Challenge <https://precision.fda.gov/challenges/truth>`_ comprised of whole-genome sequences for HG001 (NA12878) and HG002 (NA24385)
* the output from the alpha version of the `Verily DeepVariant`_ toolchain aligned to :ref:`vgrch38` reference genome.  See the `DeepVariant preprint <http://biorxiv.org/content/early/2016/12/14/092890>`_ for full details:

  |  `Creating a universal SNP and small indel variant caller with deep neural networks <http://biorxiv.org/content/early/2016/12/14/092890>`_
  |  Ryan Poplin, Dan Newburger, Jojo Dijamco, Nam Nguyen, Dion Loy, Sam Gross, Cory Y. McLean, Mark A. DePristo
  |  DOI: https://doi.org/10.1101/092890
  |

Google Cloud Platform data locations
------------------------------------

* Google Cloud Storage folder `gs://genomics-public-data/precision-fda <https://console.cloud.google.com/storage/genomics-public-data/precision-fda/>`_

Provenance
----------

* The FASTQ files in `gs://genomics-public-data/precision-fda/input <https://console.cloud.google.com/storage/genomics-public-data/precision-fda/input>`_ were run through the `Verily DeepVariant`_ alpha toolchain to produce the corresponding files in `gs://genomics-public-data/precision-fda/output/deepvariant-alpha <https://console.cloud.google.com/storage/genomics-public-data/precision-fda/output/deepvariant-alpha>`_.
