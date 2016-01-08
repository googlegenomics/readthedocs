.. sidebar:: Details

  This will create a virtual machine on Google Cloud Platform with a locked down network (only SSH port 22 open).  Your local machine will securely connect to the VM via an ssh tunnel.

  Within the docker container the directory ``/home/rstudio/data`` will correspond to directory ``/mnt/data`` on the virtual machine.  This is where the persistent data disk is attached to the VM.  **Store important files there.**  Docker containers are stateless, so if the container restarts for any reason, then files you created within the container will be lost.
