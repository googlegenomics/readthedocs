Follow the Windows, Mac OS X or Linux instructions to install gcloud on your local machine: https://cloud.google.com/sdk/

* Download and install the Google Cloud SDK by running this command in your shell or Terminal:

.. code-block:: shell

  curl https://sdk.cloud.google.com | bash

Or, you can download `google-cloud-sdk.zip <https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip>`_ or `google-cloud-sdk.tar.gz <https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz>`_, unpack it, and launch the *./google-cloud-sdk/install.sh* script.

Restart your shell or Terminal.

* Authenticate: 

.. code-block:: shell

   $ gcloud auth login

* Configure the project:

.. code-block:: shell

     $ gcloud config set project <YOUR_PROJECT_ID>

