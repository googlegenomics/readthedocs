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
Common API workflows
--------------------

There are many genomics-related APIs documented at
`cloud.google.com/genomics/reference/rest/ <https://cloud.google.com/genomics/reference/rest/>`_.

Of the available calls, there are some very common patterns that can
be useful when developing your own code.

The following sections describe these workflows using plain URLs and
simplified request bodies. Each step should map 1-1 with all of the auto-generated client libraries.


Browsing read data
~~~~~~~~~~~~~~~~~~

* ``GET /datasets?projectId=YOUR-PROJECT-ID``

  List all available datasets in a particular project.

* ``POST /readgroupsets/search {datasetIds: [<datasetId>]}``

  Search for read group sets in a particular dataset. Choose one readGroupSetId from the result.

  Note: This is a good place to use a `partial request <https://cloud.google.com/genomics/performance#partial>`_
  to only ask for the id and name fields on a read group set. Then you can follow up with a
  ``GET /readgroupsets/<readGroupSetId>`` call to get the complete read group set data.

* ``GET /readgroupsets/<readGroupSetId>/coveragebuckets``

  Get coverage information for a particular read group set. This will tell you where the read data is located,
  and which referenceNames should be used in the next step.

* ``POST /reads/search {readGroupSetIds: [<readGroupSetId>]}``

  Get reads for a particular read group set.

  The referenceName can be chosen from the coverage buckets by the user, along with the
  start and end coordinates they wish to view. The API uses 0-based coordinates.


Map reducing over read data within a read group set
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``GET /readgroupsets/<readGroupSetId>/coveragebuckets``

  First get coverage information for the read group set you are working with.

  Iterate over the ``coverageBuckets`` array.
  For each bucket, there is a field ``range.end``. Using this field, and the number of shards
  you wish to have, you can calculate sharding bounds.

  Let's say there are 23 references, and you want 115 shards. The easiest math would
  have us creating 5 shards per reference, each with a ``start`` of ``i * range.end/5``
  and an ``end`` of ``min(range.end, start + range.end/5)``

* ``POST /reads/search {readGroupSetId: x, referenceName: shard.refName, start: shard.start, end: shard.end}``

  Once you have your shard bounds, each shard will then do a reads search to get data.
  (Don't forget to use a use a `partial request <https://cloud.google.com/genomics/performance#partial>`_)


Map reducing over variant data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``GET /variantsets/<datasetId>``

  First get a summary of the variants you are working with. This includes the references
  that have data, as well as their upper bounds.

  Iterate over the ``referenceBounds`` array.
  For each reference, there is a field ``upperBound``. Using this field, and the number of shards
  you wish to have, you can calculate sharding bounds.

  Let's say there are 23 references, and you want 115 shards. The easiest math would
  have us creating 5 shards per reference, each with a ``start`` of ``i * referenceBounds.upperBound/5``
  and an ``end`` of ``min(referenceBound.upperBound, start + referenceBounds.upperBound/5)``

* ``POST /variants/search {variantSetIds: [x], referenceName: shard.refName, start: shard.start, end: shard.end}``

  Once you have your shard bounds, each shard will then do a variants search to get data.
  (Don't forget to use a use a `partial request <https://cloud.google.com/genomics/performance#partial>`_)

  If you only want to look at certain call sets, you can include the ``callSetIds: ["id1", "id2"]``
  field on the search request. Only call information for those call sets will be returned. Variants
  without any of the requested call sets will not be included at all.



