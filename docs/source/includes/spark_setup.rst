.. container:: toggle

    .. container:: header

        Deploy and configure the cluster: **Show/Hide Instructions**

    .. container:: content

      (1) Use `bdutil <https://cloud.google.com/hadoop/setting-up-a-hadoop-cluster>`_ to deploy the cluster.  If you have not already done so, `install and configure <https://cloud.google.com/hadoop/setting-up-a-hadoop-cluster>`_ bdtuil.

    .. code-block:: shell

      ./bdutil -e extensions/spark/spark_env.sh deploy

    .. container:: content

      (2) Copy your ``client_secrets.json`` to the master.  If you do not already have this file, the `sign up instructions <https://cloud.google.com/genomics/install-genomics-tools#authenticate>`_ to obtain it.

    .. code-block:: shell

      gcloud compute copy-files client_secrets.json hadoop-m:~/

    .. container:: content

      (3) ssh to the master.

    .. code-block:: shell

      gcloud compute ssh hadoop-m

    .. container:: content

      (4) Install `sbt <http://www.scala-sbt.org/release/tutorial/Installing-sbt-on-Linux.html>`_.

    .. code-block:: shell

      echo "deb http://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
      sudo apt-get update
      sudo apt-get install sbt

    .. container:: content

      (5) Clone the github repository.

    .. code-block:: shell

      sudo apt-get install git
      git clone https://github.com/googlegenomics/spark-examples.git

    .. container:: content

      (6) Compile the Jar.

    .. code-block:: shell

      cd spark-examples
      sbt assembly
      cp target/scala-2.10/googlegenomics-spark-examples-assembly-*.jar ~/
      cd ~/
