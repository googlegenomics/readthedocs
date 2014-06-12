Common API workflows
--------------------

Currently, the Google backend only supports a subset of all the 
`documented APIs <https://developers.google.com/genomics/v1beta/reference>`_.

Of the publicly available calls, there are some very common patterns that can 
be useful when developing your own code. 

The following sections describe these workflows using plain URLs and 
simplified request bodies. Each step should map 1-1 with all of the auto-generated client libraries.


Browsing read data
~~~~~~~~~~~~~~~~~~

* ``GET /datasets``                                    
  
  List all available datasets that a current user has access to. (Or all public datasets when not using OAuth)
  Choose one datasetId from the result.
  
  Note: This is not currently implemented!! This is why we have the :doc:`/constants` page for now.

* ``POST /readsets/search {datasetId: x}``

  Search for readsets in a particular dataset. Choose one readsetId from the result.
  
  Note: This is a good place to use a `partial request <https://developers.google.com/genomics/performance#partial>`_ 
  to only ask for the id and name fields on a readset. Then you can follow up with a ``GET /readsets/<readsetId>`` 
  call to get the complete readset data.
  
* ``POST /reads/search {readsetId: x}``   

  Get reads for a particular readset. 
  
  Note: The call also requires ``sequenceName``, ``sequenceStart`` and ``sequenceEnd``. 
  You can get the valid sequenceName values by looking at a readset's ``fileData[0].refSequences[].name`` fields.


Map reducing over read data within a readset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``GET /readsets/<readsetId>``

  First get the readset you are working with.
  
  Iterate over the sequences present on the readset by using the ``fileData[0].refSequences`` array. 
  For each sequence, there is a field ``length``. Using this field, and the number of shards 
  you wish to have, you can calculate sharding bounds. 

  Let's say there are 23 sequences, and you want 115 shards. The easiest math would 
  have us creating 5 shards per sequence, each with a ``start`` of ``i * seq.length/5`` 
  and an ``end`` of ``min(seq.length, start + seq.length/5)``
 
* ``POST /reads/search {readsetId: x, sequenceName: shard.seqName, sequenceStart: shard.start, sequenceEnd: shard.end}``

  Once you have your shard bounds, each shard will then do a reads search to get data. 
  (Don't forget to use a use a `partial request <https://developers.google.com/genomics/performance#partial>`_)


Map reducing over variant data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``GET /variants/summary?datasetId=<datasetId>``

  First get the summary of the variants you are working with. This includes the contigs
  that have data, as well as their upper bounds.
  
  Iterate over the ``contigBounds`` array. 
  For each contig, there is a field ``upperBound``. Using this field, and the number of shards 
  you wish to have, you can calculate sharding bounds. 

  Let's say there are 23 contigs, and you want 115 shards. The easiest math would 
  have us creating 5 shards per sequence, each with a ``start`` of ``i * contig.upperBound/5`` 
  and an ``end`` of ``min(contig.upperBound, start + contig.upperBound/5)``
 
* ``POST /variants/search {datasetId: x, contig: shard.contig, startPosition: shard.start, endPosition: shard.end}``

  Once you have your shard bounds, each shard will then do a variants search to get data. 
  (Don't forget to use a use a `partial request <https://developers.google.com/genomics/performance#partial>`_)
  
  If you only want to look at certain callsets, you can include the ``callsetIds: ["id1", "id2"]`` 
  field on the search request. Only call information for those callsets will be returned. Variants 
  without any of the requested callsets won't be included at all.



