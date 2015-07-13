This tool takes advantage of two key technologies to process
a large number of files:

* `Google Compute Engine`_
* `Grid Engine`_ (SGE)

Google Compute Engine provides virtual machines in the cloud. With sufficient
quota in your Google Cloud project, you can start dozens or hundreds of
instances concurrently. The more instances you add to your cluster, the more
quickly you can process your files.

Grid Engine is used to distribute the file operation tasks across
all of the instances such that each instance takes the responsibility
to download a single file, run the operation, and upload it back to
Cloud Storage.
