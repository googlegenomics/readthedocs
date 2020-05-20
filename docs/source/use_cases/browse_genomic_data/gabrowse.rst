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

GABrowse
========

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/browse_genomic_data/gabrowse.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

Try it now: https://gabrowse.appspot.com/

GABrowse is a sample application designed to demonstrate the capabilities of the
`Global Alliance for Genomics and Health API`_ GA4GH v0.5.1.  Currently, you can view data from Google and Ensembl.

* Use the button on the left to select a Read group set or Call set.
* Once loaded, choose a chromosome and zoom or drag the main graph to explore Read data.
* Individual bases will appear once you zoom in far enough.

To make use of this upon your own data:

(1) First, load your data into Google Genomics.  See :doc:`/use_cases/load_data/index` for more detail as to how to do this.
(2) Navigate to the auth-enabled endpoint http://gabrowse-with-auth.appspot.com/ and go through the oauth flow.
(3) View some data, for example http://gabrowse-with-auth.appspot.com/#=&readsetId=CMvnhpKTFhCJyLrAurGOnrAB&backend=GOOGLE&callsetId=10473108253681171589-538&cBackend=GOOGLE&location=5%3A90839366
(4) Then modify the ReadGroupSetId and/or CallsetId in the URL to those of your data.

The code for this sample application is on GitHub https://github.com/googlegenomics/api-client-python
