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

igv.js is an embeddable interactive genome visualization component.
The source code for igv.js is available on github:

    https://github.com/igvteam/igv.js


Documentation is available at:

    https://github.com/igvteam/igv.js/wiki


Try it now with public data in Google Genomics:

    http://igv.org/web/examples/google-demo.html

IGV Desktop
-----------

IGV Desktop supports browsing of reads from the Google Genomics Reads API and also from BAM files in Google Cloud Storage.  It implements an OAuth flow to facilitate access to private data in addition to public data.

Setup
^^^^^^

.. include:: /includes/igv_desktop_setup.rst

View a Google Genomics ReadGroupSet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Choose menu item `Google` -> `Load Genomics ReadGroupSet` and enter the readGroupSet ID for the readGroupSet you wish to view.  For example, a readGroupSet ID of ``CMvnhpKTFhD3he72j4KZuyc`` will display the reads for NA12877 from :doc:`/use_cases/discover_public_data/platinum_genomes`.

View a BAM from Google Cloud Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Choose menu item `File` -> `Load from URL` and enter the Google Cloud Storage path for the BAM you wish to view.  For example, a path of ``gs://genomics-public-data/platinum-genomes/bam/NA12877_S1.bam`` will display the reads for NA12877 from :doc:`/use_cases/discover_public_data/platinum_genomes`.

Be sure to have a ``.bai`` file stored along side the ``.bam`` file you wish to view.
