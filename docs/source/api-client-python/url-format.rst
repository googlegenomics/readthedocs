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
GABrowse URL format
-------------------

The genome browser code supports direct linking to specific backends, readsets, and genomic positions.

These parameters are set `using the hash <http://blog.mgm-tp.com/2011/10/must-know-url-hashtechniques-for-ajax-applications/>`_. 
The format is very simple with only 3 supported key value pairs separated by ``&`` and then ``=``:

* backend

  The backend to use for API calls. example: ``GOOGLE`` or ``NCBI``
  
* readsetId

  The ID of the readset that should be loaded. See :doc:`/constants` for more information. 

* location

  The genomic position to display at. Takes the form of ``<chromosome>:<base pair position>``. example: ``14:25419886``
  This can also be an `RS ID <https://customercare.23andme.com/entries/21263638-What-are-all-the-rs-numbers-rsids->`_ 
  or a string that will be searched on `snpedia <http://www.snpedia.com/index.php/SNPedia>`_.
  
As you navigate in the browser (either locally or at http://gabrowse.appspot.com), 
the hash will automatically populate to include these parameters. 
But you can also manually create a direct link without having to go through the UI.

Putting all the pieces together, here is what a valid url looks like::

  http://gabrowse.appspot.com/#backend=GOOGLE&readsetId=CPHG3MzoCRDY5IrcqZq8hMIB&location=14:25419886
