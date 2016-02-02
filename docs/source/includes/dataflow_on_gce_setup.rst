If you do not have Java on your local machine, you can set up Java 7 on a `Google Compute Engine`_ instance.  The following setup instructions will allow you to *launch* Dataflow jobs from a Compute Engine instance:

(1) If you have not already enabled the Google Cloud Platform APIs used by `Google Cloud Dataflow`_, click `here <https://console.cloud.google.com/flows/enableapi?apiid=dataflow,compute_component,logging,storage_component,storage_api,bigquery,pubsub,datastore&_ga=1.38537760.2067798380.1406160784>`_ to do so.

(2) Use the `Google Cloud Platform Console`_ to spin up a `Google Compute Engine`_ instance and ssh into it.  If you have not done this before, see the `step-by-step instructions <https://cloud.google.com/compute/docs/quickstart-developer-console>`_.

(3) Run the following command from your local machine to copy the **runnable** jar to the Compute Engine instance.  You can download the latest GoogleGenomics dataflow **runnable** jar from the `Maven Central Repository <https://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22com.google.cloud.genomics%22%20AND%20a%3A%22google-genomics-dataflow%22>`_.

.. code-block:: shell

  gcloud compute copy-files /PATH/TO/google-genomics-dataflow*runnable.jar INSTANCE-NAME:~/

(4) Run the following command from your local machine to copy the ``client_secrets.json`` to the Compute Engine instance.  If you do not already have ``client_secrets.json``, see the `sign up instructions <https://cloud.google.com/genomics/install-genomics-tools#authenticate>`_ to obtain it.

.. code-block:: shell

  gcloud compute copy-files /PATH/TO/client_secrets.json INSTANCE-NAME:~/

(5) Run the following commands on the Compute Engine instance to install `Java 7 <http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html>`_.

.. code-block:: shell

  sudo apt-get update
  sudo apt-get install --assume-yes openjdk-7-jdk maven
  sudo update-alternatives --config java
