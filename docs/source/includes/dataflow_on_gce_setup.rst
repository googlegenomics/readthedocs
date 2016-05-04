If you do not have Java on your local machine, the following setup instructions will allow you to *launch* Dataflow jobs using the `Google Cloud Shell`_:

#. If you have not already done so, follow the `Genomics Quickstart`_.

#. If you have not already done so, follow the `Dataflow Quickstart`_.

#. Use the `Cloud Console`_ to activate the `Google Cloud Shell`_.

#. Run the following commands in the Cloud Shell to install `Java 8`_.

.. code-block:: shell

  sudo apt-get update
  sudo apt-get install --assume-yes openjdk-8-jdk maven
  sudo update-alternatives --config java
  sudo update-alternatives --config javac

.. note::

  Depending on the pipeline, Cloud Shell may not not have sufficient memory to run pipeline locally (e.g., without the ``--runner`` command line flag).  If you get error ``java.lang.OutOfMemoryError: Java heap space``, follow the instructions to run the pipeline on Compute Engine Dataflow workers instead of locally (e.g. use ``--runner=DataflowPipelineRunner``).
