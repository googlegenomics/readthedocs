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
