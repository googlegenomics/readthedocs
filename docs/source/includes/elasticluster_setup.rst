.. _S3IT: http://www.s3it.uzh.ch/
.. _Elasticluster: https://elasticluster.readthedocs.org
.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/
.. _gcloud: https://cloud.google.com/sdk/
.. _SFTP: http://linux.die.net/man/1/sftp
.. _HERE DOCUMENTS: http://tldp.org/LDP/abs/html/here-docs.html
.. _googlegenomics github organization: https://github.com/googlegenomics

================================================
Create compute clusters on Google Compute Engine
================================================
---------------------------------------
Elasticluster and GCE - Getting Started
---------------------------------------

This document provides getting started instructions for using
Elasticluster_ to create clusters of Google Compute Engine instances
running job management software, such as Grid Engine, SLURM, or Hadoop.
Elasticluster "aims to provide a user-friendly command line tool to
create, manage and setup computional clusters hosted on cloud infrastructures"

What you will do
================
By following the instructions in this document, you will:

#. Install Elasticluster software
#. Configure Elasticluster to access your Google Cloud Project
#. Configure a cluster of Compute Engine virtual machines running Grid Engine
#. Start a cluster of Compute Engine virtual machine running Grid Engine
#. List nodes of your cluster
#. SSH to the instances of your Cluster
#. Destroy the cluster

Install Elasticluster
=====================
It is highly recommended that you install elasticluster in a python virtualenv_.
This will allow you to contain your Elasticluster install and dependent libraries in one place.

The instructions here explicitly use a Python virtualenv and have only been tested in this environment.

0. If you have not installed ``virtualenv``, then do so with:

.. code-block:: shell

   [sudo] pip install virtualenv

1. Change directory to where you want to install Elasticluster. You don't need to explicitly create an ``elasticluster`` directory (that will happen next).

.. |br| raw:: html

   <br />

2. Create the elasticluster virtualenv:

.. code-block:: shell

   virtualenv elasticluster

This creates a directory named ``elasticluster`` and populates it with the necessary Python library files and shell scripts to contain the Elasticluster installation.  No Elasticluster software has yet been installed.

3. Activate the ``elasticluster`` virtualenv for the current shell session:

.. code-block:: shell

    source elasticluster/bin/activate

This script will set environment variables necessary for the virtualenv:

* ``VIRTUAL_ENV``: path to the ``elasticluster`` virtualenv directory
* ``PATH``: adds ``${VIRTUAL_ENV}/bin`` to the head of the PATH
* ``PYTHONHOME``: unset if currently set

The script also saves away changed environment variables and installs a ``deactivate`` function into the bash environment.

4. Install elasticluster (select one):

    The `googlegenomics github organization`_ maintains a fork of elasticluster. The purpose of this
    fork is to provide Google Cloud bug fixes and enhancements. All such changes are submitted as
    puull requests to the mainline branch, and development is coordinated with S3IT_.
    
    There is currently one significant feature in the googlegenomics fork, that is still an open
    `pull request <https://github.com/gc3-uzh-ch/elasticluster/pull/158>`_ to mainline
    (setting the boot disk type and size).


    a. From github (mbookman fork with Google-specific updates)

    .. code:: bash

      cd elasticluster
      git clone https://github.com/googlegenomics/elasticluster.git src
      cd src
      python setup.py install

    b. From github (mainline)

    .. code:: bash

      cd elasticluster
      git clone git://github.com/gc3-uzh-ch/elasticluster.git src
      cd src
      python setup.py install

Create your cluster definition file
===================================
Elasticluster cluster definitions are driven from a configuration file.  By default this file is:

.. code:: bash

   ~/.elasticluster/config
   
Details of the config file can be found at:

   https://elasticluster.readthedocs.org/en/latest/configure.html
   
Elasticluster provides a command to automatically create the config file for you, however
using this command will create a template configuration file which you cannot immediately
use as it includes a list of clusters that are not correctly configured.

You can either:

#. Install the default template using list-templates and then fix it up, or
#. Install a minimal template provided below

In either case, you will need to configure the ``~/.elasticluster/config`` file for accessing
your Google Cloud project.

Install the default template
****************************

If you install the default template using the command:

.. code:: bash

   elasticluster list-templates
   
It will copy a default file to ``~/.elasticluster/config`` and will emit a number of WARNINGS
and ERRORS to the console.  To use this configuration file, you must then comment out or remove
all of the "cluster" examples.  Look for the section:

.. code:: bash

   # Cluster Section
   
and then comment out or remove everything up to the:

.. code:: bash

  # Cluster node section
  
You can then copy each element (except ``setup/ansible-gridengine``) of the following minimal
template into the config file.

Install a minimal template
**************************
Copy the file into ``~/.elasticluster/config`` and update the fields marked with ****.
Instructions for getting your client_id and client_secret can be found below.
The instructions provided on the Elasticluster installation site are currently out of date.

.. code:: bash

   # Gridengine software to be configured by Ansible
   [setup/ansible-gridengine]
   provider=ansible
   frontend_groups=gridengine_master
   compute_groups=gridengine_clients
   
   # Create a cloud provider (call it "google-cloud")
   [cloud/google-cloud]
   provider=google
   gce_project_id=****REPLACE WITH YOUR PROJECT ID****
   gce_client_id=****REPLACE WITH YOUR CLIENT ID****
   gce_client_secret=****REPLACE WITH YOUR SECRET KEY****
   
   # Create a login (call it "google-login")
   [login/google-login]
   image_user=****REPLACE WITH YOUR GOOGLE USERID (just the userid, not email)****
   image_user_sudo=root
   image_sudo=True
   user_key_name=elasticluster
   user_key_private=~/.ssh/google_compute_engine
   user_key_public=~/.ssh/google_compute_engine.pub
   
   # Bring all of the elements together to define a cluster called "gridengine"
   [cluster/gridengine]
   cloud=google-cloud
   login=google-login
   setup_provider=ansible-gridengine
   security_group=default
   image_id=****REPLACE WITH OUTPUT FROM: gcloud compute images list --uri | grep backports ****
   flavor=n1-standard-1
   frontend_nodes=1
   compute_nodes=2
   image_userdata=
   ssh_to=frontend

Obtaining your client_id and client_secret
******************************************
To generate a client_id and client_secret to access the Google Compute Engine visit the following page:

   https://console.developers.google.com/project/_/apiui/credential
   
#. Select the project to be used for your cluster
#. If a "Client ID for native application" is listed on this page, skip to step 8
#. Under the OAuth section, click "Create new Client ID"
#. Select "Installed Application"
#. If prompted, click "Configure consent screen" and follow the instructions to set a "product name" to identify your Cloud project in the consent screen
#. In the Create Client ID dialog, be sure the following are selected::

    Application type: Installed application
    Installed application type: Other
   
#. Click the "Create Client ID" button
#. You'll see your Client ID and Client secret listed under "Client ID for native application"

Elasticluster operations
========================
Deploy your cluster
*******************
.. code:: bash

  elasticluster start -v gridengine

List your cluster instances
***************************
.. code:: bash

  elasticluster list-nodes gridengine

SSH to your instances
*********************
Elasticluster provides a convenience routine to connect to your frontend instance:

.. code:: bash

  elasticluster ssh gridengine
  
However, you can connect to other instances using gcloud_:

.. code:: bash

  gcloud compute ssh <instance> --zone <zone>

Copy files to your instances
****************************
Elasticluster provides a convenience routine to connect to your frontend instance for SFTP_:

.. code:: bash

  elasticluster sftp gridengine

To script commands for sftp, you can use bash `HERE DOCUMENTS`_:

.. code:: bash

  elasticluster sftp gridengine << 'EOF'
  put *.sh
  EOF


See the SFTP_ man page for more commands.

Destroy your cluster
********************
.. code:: bash

  elasticluster stop -v --yes gridengine

Exit the virtualenv
===================
The ``activate`` command creates a function in the bash environment called ``deactivate``.
To exit the virtualenv, just execute the command:

.. code:: bash

  deactivate
