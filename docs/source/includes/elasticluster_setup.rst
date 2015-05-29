.. _Elasticluster: https://elasticluster.readthedocs.org
.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

================================================
Create compute clusters on Google Compute Engine
================================================
---------------------------------------
Elasticluster and GCE - Getting Started
---------------------------------------

This document provides getting started instructions for using
Elasticluster_ to create clusters of Google Compute Engine instances
running job management software, such as Grid Engine, SLURM, or Hadoop.

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

1. Change directory to where you want to install Elasticluster.
You don't need to explicitly create an ``elasticluster`` directory (that will happen next).

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

4. Install setuptools into the virtualenv

.. code:: bash

   pip install setuptools==9.1
   
This will uninstall the current version of ``setuptools`` and install an older version.  Without this step, the Elasticluster installation will fail with:

.. code:: python

   Traceback (most recent call last):
     File "<string>", line 20, in <module>
     File "/tmp/pip-build-uwB7Cn/elasticluster/setup.py", line 31, in <module>
       del sdist.finders[:]
     AttributeError: 'module' object has no attribute 'finders'
     ----------------------------------------
     Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-uwB7Cn/elasticluster

5. Install ansible into the virtualenv

.. code:: bash

  pip install ansible==1.7.2

This will uninstall the current version of ansible and install an older version.  Without this step, the installation of any software during cluster start will fail with:

.. code:: python

  ERROR:gc3.elasticluster:the setup provider was not able to setup the cluster,
  but the cluster is running by now. Setup provider error message: `__init__()
  got an unexpected keyword argument 'sudo'`

See https://github.com/gc3-uzh-ch/elasticluster/issues/156

6. Install elasticluster (select one):

   a. Using pip 

   .. code:: bash

      pip install elasticluster

   b. From github (mbookman fork with Google-specific updates)

   .. code:: bash

      cd elasticluster
      git clone https://github.com/mbookman/elasticluster.git src
      cd src
      python setup.py install

      pip uninstall --yes google-api-python-client
      pip install google-api-python-client

   c. From github (mainline)

   .. code:: bash

      cd elasticluster
      git clone git://github.com/gc3-uzh-ch/elasticluster.git src
      cd src
      python setup.py install

      pip uninstall --yes google-api-python-client
      pip install google-api-python-client

**Note**: if you change versions of Elasticluster (from pip install to github install, for example),
it is common to get inexplicable "AttributeErrors" when trying to deploy.  This is due to
Elasticluster saving Python objects to ``~/.elasticluster/store/``.
Removing the contents of this directory may resolve your issues.


