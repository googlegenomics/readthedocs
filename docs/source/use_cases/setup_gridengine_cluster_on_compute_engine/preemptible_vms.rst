.. _preemptible_rollup branch: https://github.com/googlegenomics/elasticluster/tree/preemptible_rollup
.. _googlegenomics fork: https://github.com/googlegenomics/elasticluster
.. _cluster_monitor.sh: https://github.com/googlegenomics/grid-computing-tools/blob/master/bin/cluster_monitor.sh
.. _array_job_monitor.sh: https://github.com/googlegenomics/grid-computing-tools/blob/master/tools/array_job_monitor.sh
.. _grid-computing-tools github project: https://github.com/googlegenomics/grid-computing-tools
.. _manually terminate instances: https://cloud.google.com/compute/docs/instances/stopping-or-deleting-an-instance

Create a Grid Engine cluster with Preemptible VM workers
========================================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/setup_gridengine_cluster_on_compute_engine/preemptible_vms.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

With `Compute Engine Preemptible Virtual Machines`_ you can create and
run VMs in the cloud at a much
`lower price <https://cloud.google.com/compute/pricing#machinetype>`_
than normal instances. The trade-off for the lower price is that
individual instances will run for *at most* 24 hours.

This trade-off is often a very good fit for distributed batch compute jobs,
such as a large Grid Engine job consisting of many small stateless tasks.
When a preemptible VM is terminated, only the work of the current task running
on it is lost, and the lost task can be requeued for execution on another
worker node. The preempted VM can also often be replaced to bring the cluster
back to full strength.

This document builds on the instructions to :doc:`index`
to create a Grid Engine cluster of preemptible VMs.

Toolset
-------
To succesfully run a Grid Engine workload on preemptible VMs, the instructions
here employ three tools:

* `Elasticluster`_ - to create, configure, and destroy the cluster

* `cluster_monitor.sh`_ - to replace TERMINATED virtual machine instances

* `array_job_monitor.sh`_ - to requeue failed Grid Engine tasks

The main Elasticluster fork does not currently have support built in for
Compute Engine preemptible VMs.
For this the Google Genomics team has created a branch of Elasticluster,
along with the supporting "grid computing" tools.

Steps
-----

Setting up your cluster
~~~~~~~~~~~~~~~~~~~~~~~

To create a Grid Engine cluster with preemptible VMs, follow the instructions
provided in :doc:`index` with the following changes:

#. Use the `preemptible_rollup branch`_ of the googlegenomics fork
#. Configure the compute nodes of your cluster to be preemptible

Use the preemptible_rollup branch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At step 4 (:ref:`Install elasticluster <index--install-elasticluster>`) do the following:

::

  cd elasticluster
  git clone https://github.com/googlegenomics/elasticluster.git src
  cd src
  git checkout preemptible_rollup
  python setup.py install

The two key lines here are:

::

  git clone https://github.com/googlegenomics/elasticluster.git src

which pulls from the `googlegenomics fork`_ of elasticluster, and

::

  git checkout preemptible_rollup

which sets the git branch for the ``elasticluster`` directory to the
``preemptible_rollup`` branch for installation.

Configure the compute nodes of your cluster to be preemptible
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A gridengine cluster is composed of one ``frontend`` node, and multiple
``compute`` nodes. The ``frontend`` node should NOT be preemptible. Only the
``compute`` nodes should be.

If your cluster is named ``gridengine`` then after you
:ref:`index--create-your-cluster-definition-file`,
configure the compute nodes to be preemptible by adding the following to
``~/.elasticluster/config``:

::

  [cluster/gridengine/compute]
  scheduling=preemptible

Monitoring your cluster
~~~~~~~~~~~~~~~~~~~~~~~

As the cluster runs, Compute Engine instances will be automatically
terminated independently some time within 24 hours of being created.
You typically will want the following to happen:

#. TERMINATED instances get removed from the cluster
#. New instances are created to replace TERMINATED instances

This is what the `cluster_monitor.sh`_ script does.

The cluster monitoring script is available in the
`grid-computing-tools github project`_.

Downloading the grid-computing-tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To clone the `grid-computing-tools github project`_, issue the following:

::

  git clone https://github.com/googlegenomics/grid-computing-tools.git

It is recommended that you clone the ``grid-computing-tools`` project into a
sibling directory of your elasticluster directory.

Running cluster_monitor.sh
^^^^^^^^^^^^^^^^^^^^^^^^^^

Be sure that the elasticluster executable is in your PATH. You can do this
by setting the PATH explicitly or by 
:ref:`activating the elasticluster virtualenv <index--activate-elasticluster-virtualenv>` in your shell:

::

  source elasticluster/bin/active

Then run the cluster monitor script:

::

  grid-computing-tools/bin/cluster_monitor.sh gridengine

The script will run continuously; to terminate the script, hit ``Ctrl-C``.

By default, the monitor will check the cluster status and then sleep for
10 minutes. To change the sleep interval, you can pass an additional
argument on the command line, for example:

::

  grid-computing-tools/bin/cluster_monitor.sh gridengine 5

would sleep for 5 minutes between checks.

To grow your cluster
^^^^^^^^^^^^^^^^^^^^

To increase the number of workers in your cluster while it is running,
update the ``compute_nodes`` value in ``~/.elasticluster/config``.
For example, to increase the number of compute nodes from the **3**
specified in the :doc:`index` instructions to **10**, set:

::

   [cluster/gridengine]
   ...
   compute_nodes=10
   ...

The next time the cluster monitor wakes up, it will add nodes to the cluster
to reach the new value.

To shrink your cluster
^^^^^^^^^^^^^^^^^^^^^^

To reduce the number of workers in your cluster while it is running,
update the ``compute_nodes`` value in ``~/.elasticluster/config``.

As the preemptible VMs are terminated, the cluster monitor will remove
them from the cluster, and will only replace instances if the total
number in the cluster is less than the configured value.  
You can also `manually terminate instances`_ if desired.

Monitoring your job
~~~~~~~~~~~~~~~~~~~

.. sidebar:: Note

  Grid Engine provides built-in mechanisms for detecting dead nodes
  (configured via ``reschedule_unknown`` and ``max_unheard``). In practice
  this detection and rescheduling of tasks was found to be unreliable.

When nodes are TERMINATED, any tasks running on those nodes need to be
restarted. If the TERMINATED node is re-added by the cluster monitor,
and the task is NOT submitted for restart, then the new node may sit idle
(if the new node has the same name as the TERMINATED node).

Independent of node terminations, tasks can also stall due to programming
bugs or unexpected resource contention. Failing to restart stalled tasks
results in a node effectively sitting idle.

To detect tasks that need to be restarted, either due to a TERMINATED
node or a stalled task, you can use the `array_job_monitor.sh`_
script in the `grid-computing-tools github project`_, which will:

* For each task allocated to a node:
   * Get the associated node's uptime
      * Restart the task if
         * the node is down
         * the node's uptime is less than the task's running time (meaning that the node has been replaced since the task started)
         * the task runtime is longer than a configurable timeout interval (optional)

Note: when you launch your job on the Grid Engine cluster, be sure to mark
the job as "restartable". This can be done by passing the flag ``-r y`` to
the ``qsub`` command.

Upload the job monitor script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The job monitor script must be run on the cluster's ``frontend`` node.
To upload ``array_job_monitor.sh``:

::

  elasticluster sftp gridengine << EOF
  mkdir tools
  put tools/array_job_monitor tools/
  EOF

Run the job monitor script
^^^^^^^^^^^^^^^^^^^^^^^^^^

To run the ``array_job_monitor.sh``, ssh to the frontend instance:

.. code:: bash

  elasticluster ssh gridengine

Parameters for ``array_job_monitor.sh`` are:

job_id
  Grid Engine job ID to monitor

monitor_interval
  Minutes to sleep between checks of running tasks

  Default: 15 minutes

task_timeout
  Number of minutes a task may run before it is considered stalled,
  and is eligible to be resubmitted.

  Default: None

queue_name
  Grid Engine job queue the job_id is associated with

  Default: all.q

For example, to monitor job 1, every 5 minutes, for jobs that should
not take more than 10 minutes:

::

  ./tools/array_job_monitor.sh 1 5 10

