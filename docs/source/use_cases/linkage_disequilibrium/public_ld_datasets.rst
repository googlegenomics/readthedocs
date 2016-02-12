Location of Linkage Disequilibrium Datasets
======================================

Linkage disequilibrium is run separately for each `super population and sub population <http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/integrated_call_samples_v3.20130502.ALL.panel>`_ using the `Linkage Disequilibrium pipeline <compute_linkage_disequilibrium.rst>`_. LD is computed for all pairs of variants within a window of 1,000,000 bp (1 megabase) and all pairs with absolute allelic correation of 0.4 are retained. 

The `output files <https://pantheon.corp.google.com/storage/browser/genomics-public-data/linkage-disequilibrium/1000-genomes-phase-3/ldCutoff0.4_window1MB/>`_ are split by chromosome with `output columns <https://github.com/googlegenomics/linkage-disequilibrium#linkage-disequilibrium-calculation-pipeline>`_ indicating the identity of each pair of values and the resulting LD value. The output files have also been `loaded into BigQuery <https://bigquery.cloud.google.com/dataset/genomics-public-data:linkage_disequilibrium_1000G_phase_3?pli=1>`_ with the same columns. Examples of using BigQuery to analyze LD are `available as datalabs <https://github.com/googlegenomics/linkage-disequilibrium/tree/master/datalab>`_.

