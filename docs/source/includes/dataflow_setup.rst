.. container:: toggle

    .. container:: header

        **Show/Hide Instructions**

    .. container:: content

      Google Cloud Dataflow is currently in Alpha.  If you have not already done so, `request to be whitelisted <https://cloud.google.com/dataflow/getting-started>`_ to use Dataflow.

      Click to download the `GoogleGenomics Dataflow Jar <https://github.com/googlegenomics/dataflow-java/blob/master/google-genomics-dataflow.jar>`_ or use ``curl``:

    .. code-block:: shell

      curl -O -L https://github.com/googlegenomics/dataflow-java/blob/master/google-genomics-dataflow.jar?raw=true

    .. container:: content

      Copy the ``client_secrets.json`` to same directory at the Jar.  If you do not already have this file, the `sign up instructions <https://cloud.google.com/genomics/install-genomics-tools#authenticate>`_ to obtain it.

      `Java 7<http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html>`_ is needed to run the Jar.  The Jar can be run on your local machine.  You can also set up Java 7 on a Google Compute Engine instance you do not have Java on your local machine.

    .. code-block:: shell

      sudo apt-get update
      sudo apt-get install openjdk-7-jdk maven

