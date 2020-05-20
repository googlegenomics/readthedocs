.. _SFTP: http://linux.die.net/man/1/sftp
.. _HERE DOCUMENTS: http://tldp.org/LDP/abs/html/here-docs.html
.. _xcode-select: https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/xcode-select.1.html
.. |suggested_client_id_name| replace:: ``Elasticluster``
+--------------------------------------------------------------------------------------------------------------+
| Note: Google Genomics is now Cloud Life Sciences.                                                            |       
| The Google Genomics Cookbook on Read the Docs is not actively                                                |
| maintained and may contain incorrect or outdated information.                                                |
| The cookbook is only available for historical reference. For                                                 |
| the most up to date documentation, view the official Cloud                                                   |
| Life Sciences documentation at https://cloud.google.com/life-sciences.                                       |
|                                                                                                              |
| Also note that much of the Genomics v1 API surface has been                                                  |
| superseded by `Variant Transforms <https://cloud.google.com/life-sciences/docs/how-tos/variant-transforms>`_ |
| and `htsget <https://cloud.google.com/life-sciences/docs/how-tos/reading-data-htsget>`_.                     |
+--------------------------------------------------------------------------------------------------------------+

==============================================
Create a Grid Engine cluster on Compute Engine
==============================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/setup_gridengine_cluster_on_compute_engine/index.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

This document provides getting started instructions for using
`Elasticluster`_ to create clusters of Google Compute Engine instances
running the `Grid Engine`_ job management software.

Elasticluster *"aims to provide a user-friendly command line tool to
create, manage and setup computional clusters hosted on cloud infrastructures"*
and can be used to setup software such as `Grid Engine`_, `SLURM`_, or
`Apache Hadoop`_.

What you will do
----------------
By following the instructions in this document, you will learn to:

#. Install Elasticluster software on your workstation/laptop
#. Configure Elasticluster to access your Google Cloud Project
#. Configure a cluster of Compute Engine virtual machines running Grid Engine
#. Start a cluster of Compute Engine virtual machine running Grid Engine
#. List nodes of your cluster
#. Copy files to the master instance of your cluster
#. SSH to the instances of your cluster
#. Destroy your cluster
#. Update your Elasticluster installation

Install Elasticluster on your workstation/laptop
------------------------------------------------
The following instructions have been tested on Linux and MacOS.

+--------------------------------------------------------------------+
| When installing on MacOS, some dependent modules must be compiled, |
| notably `pycrypto <https://pypi.python.org/pypi/pycrypto>`_.       |
|                                                                    |
| If the command line developer tools are not installed, run:        |
|                                                                    |
| ``xcode-select --install``                                         |
|                                                                    |
| and follow the installation instructions. See xcode-select_ for    |
| more information.                                                  |
+--------------------------------------------------------------------+

It is highly recommended that you install elasticluster in a python virtualenv_.
This will allow you to contain your Elasticluster installation and dependent libraries in one place.

The instructions here explicitly use a Python virtualenv and have only been tested in this environment.

0. **If you have not installed** ``virtualenv`` **, then do so with:**

.. code-block:: shell

   [sudo] pip install virtualenv

If you do not have write permission to the global Python site-packages directory, you can install virtualenv with the `Python user scheme`_:

.. code-block:: shell

   pip install --user virtualenv

If you do not have pip installed, you can find instructions `here <http://pip.readthedocs.org/en/stable/installing/>`_.

1. **Change directory to where you want to install Elasticluster**

You don't need to explicitly create an ``elasticluster`` directory (that will happen next).

2. **Create a virtualenv called** ``elasticluster``:

.. code-block:: shell

   virtualenv elasticluster

This creates a directory named ``elasticluster`` and populates it with the necessary Python library files and shell scripts to contain the Elasticluster installation.  No Elasticluster software has yet been installed.

.. _index--activate-elasticluster-virtualenv:

3. **Activate the** ``elasticluster`` **virtualenv for the current shell session:**

.. code-block:: shell

    source elasticluster/bin/activate

This script will set environment variables necessary for the virtualenv:

* ``VIRTUAL_ENV``: path to the ``elasticluster`` virtualenv directory
* ``PATH``: adds ``${VIRTUAL_ENV}/bin`` to the head of the PATH
* ``PYTHONHOME``: unset if currently set

The script also saves away changed environment variables and installs a ``deactivate`` function into the bash environment.

.. _index--install-elasticluster:

4. **Install elasticluster** (select one):

    The `googlegenomics github organization`_ maintains a fork of elasticluster. The purpose of this
    fork is to provide bug fixes and enhancements relevant to Google Cloud and customer use-cases.
    All such changes are submitted as pull requests to the mainline branch, and development is
    coordinated with S3IT_.

    The mainline fork is currently up-to-date with pull requests from the ``googlegenomics`` fork.
    We suggest you use the mainline fork unless you are interested in submitting a pull request
    for new features and bugs, including any items from the
    `Issues list <https://github.com/googlegenomics/elasticluster/issues>`_.

   a. From github (mainline)

   .. code:: bash

    cd elasticluster
    git clone git://github.com/gc3-uzh-ch/elasticluster.git src
    cd src
    pip install -e .

   b. From github (googlegenomics fork)

   .. code:: bash

    cd elasticluster
    git clone https://github.com/googlegenomics/elasticluster.git src
    cd src
    pip install -e .

.. _index--create-your-cluster-definition-file:

Create your cluster definition file
-----------------------------------
Elasticluster cluster definitions are driven from a configuration file.  By default this file is:

.. code:: bash

   ~/.elasticluster/config

Details of the config file can be found at:

   https://elasticluster.readthedocs.org/en/latest/configure.html

Elasticluster provides a command to automatically create the config file for you, however
using this command will create a template configuration file which you cannot immediately
use as it includes a list of clusters that are not correctly configured.

You can either:

#. Install the default template using ``list-templates`` and then fix it up, or
#. Install a minimal template provided below

In either case, you will need to configure the ``~/.elasticluster/config`` file for accessing
your Google Cloud project.

Install the default template
============================

If you install the default template using the command:

.. code:: bash

   elasticluster list-templates

It will copy a default file to ``~/.elasticluster/config`` and will emit a number of WARNINGS
and ERRORS to the console.  To use this configuration file, you must then comment out or remove
all of the "cluster" examples.  Look for the section:

.. code:: ini

   # Cluster Section

and then comment out or remove everything up to the:

.. code:: ini

  # Cluster node section

You can then copy each element (except ``setup/ansible-gridengine``) of the following minimal
template into the config file.

Install a minimal template
==========================
Copy the following into ``~/.elasticluster/config`` and update the fields marked with \*\*\*\*.

Instructions for getting your client_id and client_secret can be found
:ref:`below <index--obtaining-client_id_and_client_secrets>`.

Instructions for ensuring your SSH keypair exists can be found
:ref:`below <index--generating-ssh-keypair>`.

.. code:: ini

   # Gridengine software to be configured by Ansible
   [setup/ansible-gridengine]
   provider=ansible
   frontend_groups=gridengine_master
   compute_groups=gridengine_worker

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
   setup=ansible-gridengine
   security_group=default
   image_id=****REPLACE WITH OUTPUT FROM: gcloud compute images list | grep debian | cut -f 1 -d " "****
   flavor=n1-standard-1
   frontend_nodes=1
   compute_nodes=3
   image_userdata=
   ssh_to=frontend

.. _elasticluster-config-boot-disk:

Setting the boot disk size
==========================
For cluster tasks you may want to create use SSD persistent disk or a boot disk larger than the default 10 GB.
Elasticluster allows for specifying both the boot disk type and size for instances of your cluster:

``boot_disk_type``
    Define the type of boot disk to use.
    Supported values are `pd-standard` and `pd-ssd`.
    Default value is `pd-standard`.

``boot_disk_size``
    Define the size of boot disk to use.
    Values are specified in gigabytes.
    Default value is 10.

The disk type and size can be set for a cluster or for a group of nodes.

For example to set up the above Grid Engine cluster such that nodes have a 100 GB
SSD `persistent disk`_, add the following:

.. code:: ini

   [cluster/gridengine]
   ...
   boot_disk_type=pd-ssd
   boot_disk_size=100

or to configure all of the ``compute`` worker nodes to have a 2 TB Standard (HDD) `persistent disk`_:

.. code:: ini

   [cluster/gridengine/compute]
   boot_disk_type=pd-standard
   boot_disk_size=2000

.. _index--generating-ssh-keypair:

Generating your SSH keypair
===========================

If you have already connected to a Google Compute Engine instance using ``gcloud compute ssh``, then you will have a keypair generated in:

* ``~/.ssh/google_compute_engine``
* ``~/.ssh/google_compute_engine.pub``

If you do not have a keypair, then the ``user_key_private`` and ``user_key_public`` file paths in the ``[login/google-login]`` section above will not be valid.

You can generate your keypair with the command:

.. code:: bash

   gcloud compute config-ssh

.. _index--running-elasticluster-remote:

Running Elasticluster on a remote workstation
=============================================
The first time you run an Elasticluster command that needs to make
Compute Engine API calls (such as ``elasticluster start``, you will
be required to authorize Elasticluster to issue Compute Engine API
requests on your behalf.

The authorization flow by default will launch a web browser session
on the machine that the Elasticluster command is run on.
If that machine (such as a remote workstation or a virtual machine)
is not able to open a web browser, the operation will fail
with a message like:

.. code:: bash

  If your browser is on a different machine then exit and re-run this
  application with the command-line parameter

    --noauth_local_webserver

Passing the ``noauth_local_webserver`` value to Elasticluster is done
by setting the ``noauth_local_webserver`` configuration value in the
**cloud provider** section of ``~/.elasticluster/config``:

.. code:: bash

  # Create a cloud provider
  [cloud/google-cloud]
  provider=google
  noauth_local_webserver=True
  ...


.. _index--obtaining-client_id_and_client_secrets:

Obtaining your client_id and client_secret
==========================================

.. include:: /includes/get_client_secrets.rst

Elasticluster operations
------------------------
Deploy your cluster
===================
.. code:: bash

  elasticluster start gridengine

To get verbose output during startup, use the ``-v`` flag:

  elasticluster start -v gridengine

List your cluster instances
===========================
.. code:: bash

  elasticluster list-nodes gridengine

Copy files to your instances
============================
Elasticluster provides a convenience routine to connect to your frontend instance for SFTP_:

.. code:: bash

  elasticluster sftp gridengine

To script commands for sftp, you can use bash `HERE DOCUMENTS`_:

.. code:: bash

  elasticluster sftp gridengine << 'EOF'
  put *.sh
  EOF


See the SFTP_ man page for more commands.

SSH to your instances
=====================
Elasticluster provides a convenience routine to connect to your frontend instance:

.. code:: bash

  elasticluster ssh gridengine

To connect to other nodes, you can use the ``-n`` flag command:

.. code:: bash

  elasticluster ssh gridengine -n <nodename>

Where the nodename is the elasticluster name for the node (such as ``compute001``).

Destroy your cluster
====================
.. code:: bash

  elasticluster stop gridengine

or without prompt:

.. code:: bash

  elasticluster stop --yes gridengine

Exit the virtualenv
-------------------
The ``activate`` command creates a function in the bash environment called ``deactivate``.
To exit the virtualenv, just execute the command:

.. code:: bash

  deactivate

Note that any time you want to use elasticluster commands, you must re-activate the virtualenv
by sourcing the ``activate`` script.

Updating your installation
--------------------------
To update your installation, active the virtualenv, pull the source from GitHub, and run the install command again:

.. code:: bash

    source elasticluster/bin/activate
    cd elasticluster/src
    git pull
    pip install -e .
