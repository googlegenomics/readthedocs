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
=========================================
Migrating from Genomics API v1beta2 to v1
=========================================

The v1beta2 version of the Google Genomics API is deprecated.

If you use the the Google Genomics v1beta2 API, you will need to update
your source code to use the v1 API.

Most changes are minor and updating your code will simply involve
changing the name of objects or methods.

API Documentation
-----------------

* v1beta2: https://cloud.google.com/genomics/v1beta2/reference/
* v1     : https://cloud.google.com/genomics/reference/rest/

New client libraries
--------------------

Python, Java, Go, and other language-specific client libraries for the
v1 API can be found at:

* https://cloud.google.com/genomics/v1/libraries

API Changes
-----------

New endpoint:
~~~~~~~~~~~~~

* v1beta2: ``https://www.googleapis.com/genomics/v1beta2``
* v1     : ``https://genomics.googleapis.com/v1``

End of paging response
~~~~~~~~~~~~~~~~~~~~~~

When reaching the end of paged-responses, the v1beta2 API would omit
the ``nextPageToken`` field from the response. The v1 API will always
return the ``nextPageToken`` field. When end of paging is reached,
the value will be an empty string.

New names
=========

+-------------------------------------+------------------------------+
| v1beta2                             | v1                           |
+=====================================+==============================+
| variantsets.importVariants          | variants.import              |
+-------------------------------------+------------------------------+
| variantsets.mergeVariants           | variant.merge                |
+-------------------------------------+------------------------------+
| jobs.cancel                         | operations.cancel            |
+-------------------------------------+------------------------------+
| jobs.get                            | operations.get               |
+-------------------------------------+------------------------------+
| jobs.search                         | operations.list              |
+-------------------------------------+------------------------------+

Changed parameters
==================

For Google Cloud project references, the v1beta2 API used the
Cloud project number, while the v1 API uses the Cloud project id.

This change impacts how you call APIs. The following APIs have changed
from accepting an input project number to a project id:

* datasets.list
* jobs.search (now operations.list)
* readgroupsets.export
* variantsets.export

This change impacts objects returned from APIs. The following objects
have changed to contain a project id instead of a project number:

* datasets
* jobs (now operations)

New datatypes
=============

+---------------------+----------------------------+------------------------------+
| Field               | v1beta2                    | v1                           |
+=====================+============================+==============================+
| dataset.create_time | long                       | A timestamp in RFC3339 UTC   |
|                     |                            | "Zulu" format                |
+---------------------+----------------------------+------------------------------+
| read.info           | map<string, array<string>> | map<string, array<object>>   |
+---------------------+----------------------------+------------------------------+
| annotations.info    | map<string, array<string>> | map<string, array<object>>   |
+---------------------+----------------------------+------------------------------+

New objects
===========

Operations replaces jobs
^^^^^^^^^^^^^^^^^^^^^^^^

The `jobs <https://cloud.google.com/genomics/v1beta2/reference/jobs>`_ object
has been replaced with
`operations <https://cloud.google.com/genomics/reference/rest/v1/operations>`_.

Job Status
~~~~~~~~~~

With v1beta2, the status was encoded in the ``status`` field with
detailed information in the detailedStatus.

With v1, the status is a combination of ``status`` field plus the
existence of the either the ``errors`` object (failure) *or* the
``response`` object (success).

ID
~~

With v1beta2, the job was identified with the ``id`` field.
With v1, the operation is identified by the ``name`` field.

importedIds
~~~~~~~~~~~

After a successful import, the job object would be populated with a list of
``importedIds``.
In the operation, this data is a child field of the ``response``, either the
``callSetIds`` or ``readGroupSetIds``.

created
~~~~~~~

The job ``created`` time is now in the operation ``metadata.createTime`` field.

request
~~~~~~~

The job ``request`` values are now in the operation ``metadata.request`` field.


Field Masks
===========

All Genomics APIs accept an optional list of fields to return.
This is sometimes referred to as a "field mask".
The ``patch`` and ``update`` APIs accept an ``updateMask`` indicating the specific
fields to change.

In v1beta2, the "/" character could be used to separate a parent object
from a child field, for example:

* ``readGroupSets/id``

In v1, the "/" character is not accepted, and parentheses must wrap the
child field:

* ``readGroupSets(id)``

You can test building a proper field mask by using the "fields editor"
available in the documentation for the `Google Genomics API`_, or from the
`Google APIs Explorer`_.

For example, for ``genomics.datasets.list`` see:

* `API Documentation <https://cloud.google.com/genomics/reference/rest/v1/datasets/list#try-it>`_
* `APIs Explorer <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.datasets.list>`_
