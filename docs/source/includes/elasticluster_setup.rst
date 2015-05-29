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

0. If you have not installed virtualenv, then do so with:

.. code-block:: shell

   [sudo] pip install virtualenv

1. Change directory to where you want to install Elasticluster.
You don't need to explicitly create an elasticluster directory (that will happen next).

2. Create the elasticluster virtualenv:

.. code-block:: shell

   virtualenv elasticluster

This creates a directory named elasticluster and populates it with the necessary Python library files and shell scripts to contain the Elasticluster installation.  No Elasticluster software has yet been installed.

