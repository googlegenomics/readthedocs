These instructions are based on `Genomics Tools tutorial <https://cloud.google.com/genomics/install-genomics-tools#install>`_.

Set up your account and a cloud project
---------------------------------------

.. include:: /includes/account_signup.rst

.. include:: /includes/gcp_signup.rst

.. include:: /includes/create_project.rst

Install gcloud tool and validate access to genomics data
--------------------------------------------------------

.. include:: /includes/collapsible_gcloud_setup.rst

* Install the Genomics tools:

.. code-block:: shell

     $ gcloud components update alpha

*  Confirm the access to Genomics data works:

.. code-block:: shell

     $ cloud alpha genomics readgroupsets list 10473108253681171589 --limit 10
     ID                      NAME     REFERENCE_SET_ID
     CMvnhpKTFhDq9e2Yy9G-Bg  HG02573  EOSt9JOVhp3jkwE
     CMvnhpKTFhCEmf_d_o_JCQ  HG03894  EOSt9JOVhp3jkwE
     ...

Set up credentials for programs accessing the genomics data
-----------------------------------------------------------

.. include:: /includes/collapsible_get_client_secrets.rst

Copy **client_secrets.json** to the directory where you installed the Genomics tools.

The first time you query the API you will be authenticated using the values in the client_secrets file you downloaded. After this initial authentication, the Genomics tools save a token to use during subsequent API requests.