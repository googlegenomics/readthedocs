.. container:: toggle

    .. container:: header

        To kick off the job from Google Compute Engine: **Show/Hide Instructions**

    .. container:: content

    If you do not have Java on your local machine, you can set up Java 7 on a `Google Compute Engine`_ instance.  The following setup instructions will allow you to *launch* Dataflow jobs from a Compute Engine instance:

      (1) Use the `Google Developers Console`_ to spin up a `Google Compute Engine`_ instance and ssh into it.  If you have not done this before, see the `step-by-step instructions <https://cloud.google.com/compute/docs/quickstart-developer-console>`_.

      (2) Run the following commands on the Compute Engine instance to install `Java 7 <http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html>`_ and copy the Jar.

      .. code-block:: shell

        sudo apt-get update
        sudo apt-get install --assume-yes openjdk-7-jdk maven
        curl -O -L https://github.com/googlegenomics/dataflow-java/raw/master/google-genomics-dataflow.jar
        sudo update-alternatives --config java

      (3) Run the following command from your local machine to copy the ``client_secrets.json`` to the Compute Engine instance.  If you do not already have this file, see the `sign up instructions <https://cloud.google.com/genomics/install-genomics-tools#authenticate>`_ to obtain it.

      .. code-block:: shell

        gcloud compute copy-files ~/googlegenomics/dataflow-java/client_secrets.json INSTANCE-NAME:~/

      (4) If you have not already done so, enable the Google Cloud Platform APIs used by `Google Cloud Dataflow`_.  See the `Core Cloud Platform Setup Steps <https://cloud.google.com/dataflow/getting-started#Core>`_ for the list of APIs to enable.

    *Tip:* Add option ``--noLaunchBrowser`` your dataflow command lines so that the authorization flow prints a URL to be copied instead of launching a web browser.
