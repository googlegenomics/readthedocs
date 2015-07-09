**Upload input list file, config file, and** ``grid-computing-tools`` **source to the gridengine cluster master**

.. code-block:: shell

  elasticluster sftp gridengine << EOF
  put ../my_jobs/*
  mkdir src
  put -r src
  EOF
