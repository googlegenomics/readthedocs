.. container:: toggle

    .. container:: header

        To kick off the job from your local machine: **Show/Hide Instructions**

    .. container:: content

      Most users *kick off* Dataflow jobs from their local machine.  This is unrelated to where the job itself actually runs (which is controlled by the ``--runner`` parameter).  Either way, `Java 7 <http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html>`_ is needed to run the Jar that kicks off the job.

      (1) Click to download the `GoogleGenomics Dataflow Jar <https://github.com/googlegenomics/dataflow-java/blob/master/google-genomics-dataflow.jar>`_ or use ``curl``:

    .. code-block:: shell

      curl -O -L https://github.com/googlegenomics/dataflow-java/raw/master/google-genomics-dataflow.jar

    .. container:: content

      (2) Copy your ``client_secrets.json`` to same directory as the Jar.  If you do not already have this file, see the `sign up instructions <https://cloud.google.com/genomics/install-genomics-tools#authenticate>`_ to obtain it.

      (3) If you have not already done so, enable the Google Cloud Platform APIs used by `Google Cloud Dataflow`_.  See the `Core Cloud Platform Setup Steps <https://cloud.google.com/dataflow/getting-started#Core>`_ for the list of APIs to enable.
