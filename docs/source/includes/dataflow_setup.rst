Most users *kick off* Dataflow jobs from their local machine.  This is unrelated to where the job itself actually runs (which is controlled by the ``--runner`` parameter).  Either way, `Java 7 or 8 <http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html>`_ is needed to run the Jar that kicks off the job.

#. If you have not already done so, follow the Google Genomics `getting started instructions <https://cloud.google.com/genomics/install-genomics-tools>`_ to set up your environment including `installing gcloud <https://cloud.google.com/sdk/>`_ and running ``gcloud init``.

#. If you have not already done so, follow the Google Cloud Dataflow `getting started instructions <https://cloud.google.com/dataflow/getting-started>`_ to set up your environment for Dataflow.

#. Download the latest GoogleGenomics dataflow **runnable** jar from the `Maven Central Repository <https://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22com.google.cloud.genomics%22%20AND%20a%3A%22google-genomics-dataflow%22>`_.

#. Download the correct version of the `ALPN`_.  Many of these pipelines require `ALPN`_.  When running locally, this must be provided on the boot classpath but when running on Google Cloud this is already configured for you.
  #. See the `ALPN documentation <http://www.eclipse.org/jetty/documentation/9.2.10.v20150310/alpn-chapter.html>`_ for a table of which ALPN jar to use for your JRE version.
  #. Then download the correct version from `here <http://mvnrepository.com/artifact/org.mortbay.jetty.alpn/alpn-boot>`__.
