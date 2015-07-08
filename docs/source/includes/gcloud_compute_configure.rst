(1) Set your default project ID.  *Note: Project ID is not the same as project name.  You can view your project ID on the overview page of the* `Google Developers Console`_.

  ``gcloud config set project YOUR-PROJECT-ID``

(2) Set your default zone.

  ``gcloud config set compute/zone us-central1-f``

(3) Authorize gcloud.

  ``gcloud auth login``

(4) Set up your ssh keys.

  ``gcloud compute config-ssh``

For more information, see: https://cloud.google.com/compute/docs/gcloud-compute/

