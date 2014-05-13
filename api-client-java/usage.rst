Command line options for api-client-java
----------------------------------------

To see the help menu on the command line::

  java -jar target/genomics-tools-client-java-v1beta.jar

The first argument to the jar is the ``request_type``. This type is always
required and tells the program what kind of API call to make. Each type
supports, and requires, slightly different options although some options are
common to all requests.

All the request types map to Genomics API calls. You can read the
`API documentation <https://developers.google.com/genomics/v1beta/reference>`_
for more information about the various objects, and what each method is doing.

Supported request types
~~~~~~~~~~~~~~~~~~~~~~~

**importreadsets**

  --dataset_id  Required. The datasetId to import into.
  --bam_file    Required. The file to import. You can repeat this option.

  ::

    java -jar target/genomics-tools-client-java-v1beta.jar importreadsets --dataset_id "mydataset" --bam_file gs://mybucket/file1.bam --bam_file gs://mybucket/file2.bam


**searchreadsets**

  --dataset_id  Required. The dataset to search in.

  ::

    java -jar target/genomics-tools-client-java-v1beta.jar searchreadsets --dataset_id "376902546192"


**getreadset**

  --readset_id  Required. The readset to fetch. You can repeat this option.

  ::

    java -jar target/genomics-tools-client-java-v1beta.jar getreadset --readset_id "CJDmkYn8ChCh4IH4hOf4gacB" --readset_id "CJDmkYn8ChCcnc7i4KaWqmQ"


**getjob**

  --job_id  Required. The job to fetch. You can repeat this option.

  ::

    java -jar target/genomics-tools-client-java-v1beta.jar getjob --job_id "myjob1" --job_id "myjob2"



**searchreads**

  --readset_id        Required. The readset to search in. 
                      You can repeat this option.
  --sequence_name     The name of the sequence to search over.
  --sequence_start    The start position of the search.
  --sequence_end      The end position of the search.
  --page_token        Optional. When you get a paginated request, 
                      use this option to get the next page of results.

  ::

    java -jar target/genomics-tools-client-java-v1beta.jar searchreads --readset_id "CJDmkYn8ChCh4IH4hOf4gacB" --sequence_name 1 --sequence_start 10000 --sequence_end 10000


**custom**

  If you wish to call an API method that doesn't have a pre-defined request type, 
  or if you wish to pass in additional JSON fields that aren't supported with the 
  existing options, then you can issue a fully custom request with the following parameters:

  --custom_endpoint  Required. The API endpoint to query. This is relative 
                     to the base URL and shouldn't start with a ``/`` Example: ``readsets/search``.
  --custom_method    The HTTP method to query with. Defaults to ``POST``. Other valid examples are 
                     ``GET``, ``PATCH``, ``DELETE``.
  --custom_body      If the API endpoint you are hitting requires a HTTP body, use this 
                     parameter to pass in a JSON object as a string. It should look something like ``{"key": "value"}``
                     
  Putting these pieces together, if you wanted to do a readsets search with name filtering 
  (which isn't supported through the other options) you could do so with this query::

    java -jar target/genomics-tools-client-java-v1beta.jar custom --custom_endpoint "readsets/search" --custom_body '{"datasetIds": ["376902546192"], "name": "NA1287"}' --fields "readsets(id,name)" --pretty_print

  If instead you wanted to make a ``GET`` call, your custom request could look like this::

    java -jar target/genomics-tools-client-java-v1beta.jar custom --custom_endpoint "readsets/CJDmkYn8ChCh4IH4hOf4gacB" --custom_method "GET" --fields "id,name" --pretty_print



Common options
~~~~~~~~~~~~~~

These options can be used with any request type.

**--client_secrets_filename**

  If your client_secrets.json file is not in the same directory
  that you call the jar from, then use this path to specify where the file is located.
  The client_secrets.json file must exist.
  
  ::

    java -jar genomics-tools-client-java-v1beta.jar searchreadsets --dataset_id "376902546192" --client_secrets_filename ~/Downloads/client_secrets.json


**--root_url**

  Use this to hit a different API provider (like NCBI or EBI).
  
  ::

    java -jar target/genomics-tools-client-java-v1beta.jar searchreadsets --root_url "http://trace.ncbi.nlm.nih.gov/Traces/gg/" --dataset_id "SRP034507" --fields "readsets(id,name,fileData),pageToken"


**--pretty_print**

  When this is option is used, the json results will be pretty printed.

**--fields**

  Use this option to fetch a partial response from the API
  (i.e. only return some fields) See the
  `API docs <https://developers.google.com/genomics/performance#partial>`_
  for more details.
  
  ::

    java -jar target/genomics-tools-client-java-v1beta.jar searchreadsets --dataset_id 376902546192 --fields "readsets(id,name)"
