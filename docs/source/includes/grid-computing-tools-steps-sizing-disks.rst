**Create a gridengine cluster with sufficient disk space attached to each** ``compute`` **node**

a. Determine disk size requirements

   Each ``compute`` node will require sufficient disk space to hold the
   input and output files for its current task. Determine the largest file
   in your input list and estimate the total space you will need.
   It may be necessary to download the file and perform the operation
   manually to get a maximum combined input and output size.

   Persistent disk performance also scales with the size of the volume.
   Independent of storage requirements, for consistent throughput on long
   running jobs, use a standard persistent disk of at least 1TB, or use
   SSD persistent disk. More documentation is available for
   `selecting the right persistent disk`_.

   |br|

b. Verify or increase quota

   Your choice for number of nodes and disk size must take into account your
   `Compute Engine resource quota`_ for the region of your cluster.

   Quota limits and current usage can be viewed with ``gcloud compute``:

   .. code-block:: shell

      gcloud compute regions describe *region*

   or in ``Developers Console``:

      https://console.developers.google.com/project/_/compute/quotas

   Important quota limits include ``CPUs``, ``in-use IP addresses``,
   and ``disk size``.

   To request additional quota, submit the
   `Compute Engine quota request form`_.

   |br|

c. Configure your cluster

   Instructions for setting the boot disk size for the compute nodes of your
   cluster can be found at :ref:`elasticluster-config-boot-disk`.

   You will likely want to set the number of ``compute`` nodes for your
   cluster to a number higher than the **3** specified in the example cluster
   setup instructions.

   Once configured, start your cluster.

