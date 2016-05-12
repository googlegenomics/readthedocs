Integrative Genomics Viewer (IGV)
=================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/browse_genomic_data/igv.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

IGV Web
-------

Try it now: http://igv.org/web/demo/ga4gh-demo.html

There is also an embeddable version: http://igv.org/web/examples/ga4gh.html

IGV Desktop
-----------

IGV Desktop supports browsing of reads from the Google Genomics Reads API and also from BAM files in Google Cloud Storage.  It implements an OAuth flow to facilitate access to private data in addition to public data.

Setup
^^^^^^

/includes/igv_desktop_setup.rst

View a Google Genomics ReadGroupSet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Choose menu item `Google` -> `Load Genomics ReadGroupSet` and enter the readGroupSet ID for the readGroupSet you wish to view.  For example, a readGroupSet ID of ``CMvnhpKTFhD3he72j4KZuyc`` will display the reads for NA12877 from :doc:`/use_cases/discover_public_data/platinum_genomes`.

View a BAM from Google Cloud Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Choose menu item `File` -> `Load from URL` and enter the Google Cloud Storage path for the BAM you wish to view.  For example, a path of ``gs://genomics-public-data/platinum-genomes/bam/NA12877_S1.bam`` will display the reads for NA12877 from :doc:`/use_cases/discover_public_data/platinum_genomes`.

Be sure to have a ``.bai`` file stored along side the ``.bam`` file you wish to view.
