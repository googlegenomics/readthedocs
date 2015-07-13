**Monitoring the status of your job**

Grid Engine provides the ``qstat`` command to get the status of the execution queue.

While the job is in the queue, the `state` column will indicate the status of each task.
Tasks not yet allocated to a ``compute`` node will be collapsed into a single row as in the following output:

.. code-block:: shell

  $ qstat
  job-ID  prior   name       user      state submit/start at     queue            slots ja-task-ID 
  ------------------------------------------------------------------------------------------------
       1  0.00000 my-job     janedoe   qw    06/16/2015 18:03:32                      1 1-6:1

The above output indicates that tasks **1-6** of job **1** are all in a ``qw`` (queue waiting) state.

When tasks get allocated, the output will look something like:

.. code-block:: shell

  $ qstat
  job-ID  prior   name       user      state submit/start at     queue            slots ja-task-ID 
  ------------------------------------------------------------------------------------------------
       1  0.50000 my-job     janedoe   r     06/16/2015 18:03:45 all.q@compute002     1 1
       1  0.50000 my-job     janedoe   r     06/16/2015 18:03:45 all.q@compute001     1 2
       1  0.50000 my-job     janedoe   r     06/16/2015 18:03:45 all.q@compute003     1 3
       1  0.00000 my-job     janedoe   qw    06/16/2015 18:03:32                      1 4-6:1

which indicates tasks **1-3** are all in the ``r`` (running) state, while tasks **4-6** remain in a waiting state.

When all tasks have completed ``qstat`` will produce no output.
