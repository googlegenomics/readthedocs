GABrowse
========

Try it now: https://gabrowse.appspot.com/

GABrowse is a sample application designed to demonstrate the capabilities of the
`GA4GH API v0.5.1 <http://ga4gh.org/#/api>`_.  Currently, you can view data from Google and Ensembl.

* Use the button on the left to select a Read group set or Call set.
* Once loaded, choose a chromosome and zoom or drag the main graph to explore Read data.
* Individual bases will appear once you zoom in far enough.

To make use of this upon your own data:

(1) First, load your data into Google Genomics.  See :doc:`../load_data/index` for more detail as to how to do this.
(2) Navigate to the auth-enabled endpoint http://gabrowse-with-auth.appspot.com/ and go through the oauth flow.
(3) View some data, for example http://gabrowse-with-auth.appspot.com/#=&readsetId=CMvnhpKTFhCJyLrAurGOnrAB&backend=GOOGLE&callsetId=10473108253681171589-538&cBackend=GOOGLE&location=5%3A90839366
(4) Then modify the ReadGroupSetId and/or CallsetId in the URL to those of your data.

The code for this sample application is on GitHub https://github.com/googlegenomics/api-client-python
