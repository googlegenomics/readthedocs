Use ``--help`` to get more information about the command line options.  Change
the pipeline class name below to match the one you would like to run.

.. code-block:: shell

  java -cp target/linkage-disequilibrium*runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.LinkageDisequilibrium \
    --help=com.google.cloud.genomics.dataflow.pipelines.LinkageDisequilibrium\$LinkageDisequilibriumOptions

See the source code for implementation details: https://github.com/googlegenomics/linkage-disequilibrium
