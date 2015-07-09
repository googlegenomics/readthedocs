**Viewing log files**

When tasks complete, the result log files are uploaded to GCS if
``OUTPUT_LOG_PATH`` was set in the job config file. The log files can be of
value both to verify success/failure of all tasks, as well as to gather
some performance statistics before starting a larger job.

* Count number of successful tasks

  .. code-block:: shell

    gsutil cat OUTPUT_LOG_PATH/* | grep SUCCESS | wc -l

Where the ``OUTPUT_LOG_PATH`` should be the value you specified in the job
config file (step 6 above).

* Count number of failed tasks

  .. code-block:: shell

    gsutil cat OUTPUT_LOG_PATH/* | grep FAILURE | wc -l

Where the ``OUTPUT_LOG_PATH`` should be the value you specified in the job
config file (step 6 above).

* Compute total task time

  .. code-block:: shell

    gsutil cat OUTPUT_LOG_PATH/* | \
      sed -n -e 's#^Task time.*: \([0-9]*\) seconds#\1#p' | \
      awk '{ sum += $1; } END { print sum/NR " seconds"}'

* Compute average task time

  .. code-block:: shell

    gsutil cat OUTPUT_LOG_PATH/* | \
      sed -n -e 's#^Task time.*: \([0-9]*\) seconds#\1#p' | \
      awk '{ sum += $1; } END { print sum " seconds"}'

