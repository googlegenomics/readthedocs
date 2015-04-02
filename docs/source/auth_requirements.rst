API authorization requirements
------------------------------

Calls to the Google Genomics API can be made with 
`OAuth <https://cloud.google.com/genomics/auth#OAuth2Authorizing>`_ or with an 
`API key <https://cloud.google.com/genomics/auth#APIKey>`_. 

* To access private data or to make any write calls, an API request needs to be authenticated with OAuth. 
* Read-only calls to public data only require an API key to identify the calling project. (OAuth will also work)

Some APIs are still in the testing phase. 
The following lays out where each API call stands and also indicates whether a call 
supports requests without OAuth.


Available APIs
~~~~~~~~~~~~~~

============================================= ==============
API method                                    OAuth required
============================================= ==============
Get, List and Search methods (except on Jobs) False
Create, Delete, Patch and Update methods      True
Import and Export methods                     True
All Job methods                               True
============================================= ==============


APIs in testing
~~~~~~~~~~~~~~~

========================  ==============
API method                OAuth required
========================  ==============
genomics.experimental.*   True
========================  ==============
