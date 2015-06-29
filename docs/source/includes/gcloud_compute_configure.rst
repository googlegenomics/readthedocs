The instructions are below but if you want to learn more, see: https://cloud.google.com/compute/docs/gcloud-compute/

(1) Set your default project ID.  *Note: Project ID is not the same as project name.  You can view your project ID on the overview page of the Developers Console*.

  ``gcloud config set project YOUR-PROJECT-ID``

(2) Set your default zone.

  ``gcloud config set compute/zone us-central1-f``

(3) Authorize gcloud.

  ``gcloud auth login``
