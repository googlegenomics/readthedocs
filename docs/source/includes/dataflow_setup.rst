Most users *kick off* Dataflow jobs from their local machine.  This is unrelated to where the job itself actually runs (which is controlled by the ``--runner`` parameter).  Either way, `Java 7 <http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html>`_ is needed to run the Jar that kicks off the job.

(1) Download the latest GoogleGenomics dataflow **runnable** jar from the `Maven Central Repository <https://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22com.google.cloud.genomics%22%20AND%20a%3A%22google-genomics-dataflow%22>`_.

(2) Copy your ``client_secrets.json`` to same directory as the Jar.  If you do not already have this file, see the `sign up instructions <https://cloud.google.com/genomics/install-genomics-tools#authenticate>`_ to obtain it.

(3)  If you have not already enabled the Google Cloud Platform APIs used by `Google Cloud Dataflow`_, click `here <https://console.cloud.google.com/flows/enableapi?apiid=dataflow,compute_component,logging,storage_component,storage_api,bigquery,pubsub,datastore&_ga=1.38537760.2067798380.1406160784>`_ to do so.

(4) If you have not already done so, follow the instructions to `install gcloud`_.

(5) If you have not already done so, run the command ``gcloud auth login``.
