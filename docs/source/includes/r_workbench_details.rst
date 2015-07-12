If you would also like a shell prompt, use the `Google Developers Console`_ to ssh to the instance and:

**TODO: where to find ssh in developers console**

.. code:: bash

  # list the running containers
  sudo docker ps
  # open a bash shell in the Bioconductor container
  sudo docker exec -i -t THE-CONTAINER-ID /bin/bash
  # change to user rstudio
  su rstudio -s /bin/bash
  # go to /home/rstudio
  cd
  # start R
  R

To run on a larger machine ... *more here*

See https://github.com/googlegenomics/gce-images for the Docker file.  It depends upon http://www.bioconductor.org/help/docker/ which depends upon https://github.com/rocker-org/rocker/wiki

To save changes to your docker image ... *more here*
https://github.com/rocker-org/rocker/wiki/How-to-save-data

To attach a data disk ... *more here*
https://github.com/rocker-org/rocker/wiki/Sharing-files-with-host-machine

