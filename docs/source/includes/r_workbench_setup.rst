.. sidebar:: Details

  This script will create virtual machine on Google Cloud Platform with a locked down network (only SSH port 22 open).  Your local machine will securely connect to the VM via an ssh tunnel.

  This script is idempotent - you can re-run it and it will pick up where it last left off (e.g., to reconnect to a preexisting Google Compute Engine instance running Bioconductor).

(1) Download the `BiocDockerOnGCE launch script`_ to your local machine.

(2) Run the script on your local machine.  After about 5-10 minutes your browser should redirect to RStudioServer's sign-in page.

.. code:: bash

  sh ./bioconductorRStudioGCE.sh

(3) Log into RStudio.

  username
    rstudio

  password
    rstudio

(4) Upload ``client_secrets.json``. From the RStudio *Files Pane* click on the "Upload" button.

  .. image:: /_static/upload_client_secrets.png
    :alt: Upload Client Secrets

