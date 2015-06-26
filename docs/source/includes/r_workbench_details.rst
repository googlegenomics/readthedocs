If you would also like a shell prompt, ssh to the instance and:

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

To attach a data disk ... *more here*

To save changes to your docker image ... *more here*

See https://github.com/googlegenomics/gce-images for the Docker file.
