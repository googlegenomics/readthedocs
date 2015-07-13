**Upload the** ``src`` **and** ``samples`` **directories to the Grid Engine master instance:**

.. code-block:: shell

  cd grid-computing-tools
  
  elasticluster sftp gridengine << 'EOF'
  mkdir src
  put -r src
  mkdir samples
  put -r samples
  EOF
