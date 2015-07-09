**Checking the logging output of tasks**

Each gridengine task will write to an "output" file and an "error" file.
These files will be located in the directory the job was launched from (the ``HOME`` directory).
The files will be named respectively:

* *job_name*.\ **o**\ *job_id*.\ *task_id* (for example: ``my-job.o1.10``)
* *job_name*.\ **e**\ *job_id*.\ *task_id* (for example: ``my-job.e1.10``)

|br|
The error file will contain any unexpected error output, and will also
contain any download and upload logging from ``gsutil``.
