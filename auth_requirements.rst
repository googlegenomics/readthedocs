API authorization requirements
------------------------------

Calls to the Google Genomics API can be made with 
`OAuth <https://developers.google.com/genomics/auth#OAuth2Authorizing>`_ or with an 
`API key <https://developers.google.com/genomics/auth#APIKey>`_. 

* To access private data or to make any write calls, an API request needs to be authenticated with OAuth. 
* Read-only calls to public data only require an API key to identify the calling project. (OAuth will also work)

Some APIs have not yet been implemented, and others are still in the testing phase. 
The following lays out where each API call stands and also indicates whether a call 
supports requests without OAuth.


Available APIs
~~~~~~~~~~~~~~

=========================  ==============
API method                 OAuth required
=========================  ==============
genomics.datasets.get      False
genomics.datasets.create   True
genomics.datasets.delete   True
genomics.datasets.list     False
genomics.datasets.patch    True
genomics.datasets.update   True
genomics.readsets.get	     False
genomics.readsets.search   False
genomics.reads.search      False
genomics.jobs.get          True
=========================  ==============


APIs in testing
~~~~~~~~~~~~~~~

========================  ==============
API method                OAuth required
========================  ==============
genomics.readsets.import  True
genomics.variants.*       Some calls
genomics.callsets.*       Some calls
genomics.experimental.*   True
========================  ==============


APIs in development
~~~~~~~~~~~~~~~~~~~

========================  ==============
API method                OAuth required
========================  ==============
genomics.readsets.create  True
genomics.readsets.delete  True
genomics.readsets.export  True
genomics.readsets.patch   True
genomics.readsets.update  True
genomics.reads.get        False
genomics.beacons.get      False
========================  ==============
