* Deploy your Spark cluster using `Google Cloud Dataproc`_.

  .. code-block:: shell

    gcloud beta dataproc clusters create example-cluster --scopes cloud-platform

* ssh to the master.

  .. code-block:: shell

    gcloud compute ssh example-cluster-m

* Compile and build the pipeline jar.  You can `build locally <https://github.com/googlegenomics/spark-examples>`_ or build on the Spark master running on Google Compute Engine.

.. container:: toggle

  .. container:: header

    To compile and build on Compute Engine: **Show/Hide Instructions**

  .. container:: content

    (1) Install `sbt <http://www.scala-sbt.org/release/tutorial/Installing-sbt-on-Linux.html>`_.

      .. code-block:: shell

        echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
        sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823
        sudo apt-get install apt-transport-https
        sudo apt-get update
        sudo apt-get install sbt

    (2) Clone the github repository.

      .. code-block:: shell

        sudo apt-get install git
        git clone https://github.com/googlegenomics/spark-examples.git

    (3) Compile the Jar.

      .. code-block:: shell

        cd spark-examples
        sbt assembly
        cp target/scala-2.10/googlegenomics-spark-examples-assembly-*.jar ~/
        cd ~/

