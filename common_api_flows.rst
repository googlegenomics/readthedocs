Common API workflows
--------------------

Currently, the Google backend only supports a subset of all the 
`documented APIs <https://developers.google.com/genomics/v1beta/reference>`_.

Of the publicly available calls, there are some very common patterns that can 
be useful when developing your own code. 

The following sections describe these workflows using plain URLs and 
simplified request bodies. Each step should map 1-1 with all of the generated client libraries.


Browsing read data
~~~~~~~~~~~~~~~~~~

``GET /datasets``                                    
  
  List all available datasets that a current user has access to. (Or all public datasets when not using OAuth)
  Choose one datasetId from the result.
  
  Note: This is not currently implemented!! This is why we have the :doc:`/constants` page for now.

``POST /readsets/search {datasetId=x}``

  Search for readsets in a particular dataset. Choose one readsetId from the result.
  
  Note: This is a good place to use a `partial request <https://developers.google.com/genomics/performance#partial>`_ 
  to only ask for the id and name fields on a readset. Then you can follow up with a ``GET readsets/<readsetId>`` 
  call to get the complete readset data.
  
``POST /reads/search {readsetId=x}``   

  Get reads for a particular readset. 
  
  Note: The call also requires ``sequenceName``, ``sequenceStart`` and ``sequenceEnd``. 
  You can get the valid sequenceName values by looking at a readset's ``.fileData[0].refSequences[].name`` field.
