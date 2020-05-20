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

Beacon
======

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/browse_genomic_data/beacon.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

What's a beacon? [#beacon]_

    A beacon is a simple web service that answers questions of the form, "Do you have any genomes with an 'A' at position 100,735 on chromosome 3?" (or similar data). It responds simply with either "Yes" or "No." This open web service is designed both to be technically simple (so it is easy to implement) and to mitigate risks associated with genomic data sharing.

    We call these applications "Beacons" because, like the SETI project, many dedicated people have been scanning the universe of human research for signs of willing participants in far-reaching data sharing efforts, but despite many assurances of interest, it has remained a dark and quiet place. Once your "Beacon" is lit, you can start to take the next steps to add functionality to it, and finding the other groups who may help by following their Beacons.

There is an AppEngine implementation of the Beacon API from the Global Alliance for Genomics and Health written in Go.  Here is an example query that is running against a private copy (for demonstration purposes) of the :doc:`/use_cases/discover_public_data/platinum_genomes` variants:

  http://goapp-beacon.appspot.com/?chromosome=chr17&coordinate=41196407&allele=A

To turn on a beacon for your own data:

(1) First, load your data into Google Genomics.  See `Load Genomic Variants`_ for more detail as to how to do this.
(2) Then follow the instructions on https://github.com/googlegenomics/beacon-go to deploy the AppEngine implementation of Beacon.

.. rubric:: Footnotes

.. [#beacon] http://ga4gh.org/#/beacon

