**Viewing the results of the jobs**

When tasks complete, the result files are uploaded to GCS.
You can view the list of output files with ``gsutil ls``, such as:

.. code-block:: shell

  gsutil ls OUTPUT_PATH

Where the ``OUTPUT_PATH`` should be the value you specified in the job config
file (step 6 above).
