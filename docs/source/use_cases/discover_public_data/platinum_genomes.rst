Illumina Platinum Genomes
===========================

This dataset comprises the 17 member CEPH pedigree 1463.  See http://www.illumina.com/platinumgenomes/ for full details.

Google Cloud Platform data locations
------------------------------------

* Google Cloud Storage folder `gs://genomics-public-data/platinum-genomes <https://console.developers.google.com/storage/genomics-public-data/platinum-genomes/>`_
* Google Genomics Dataset ID `3049512673186936334 <https://developers.google.com/apis-explorer/#p/genomics/v1beta2/genomics.datasets.get?datasetId=3049512673186936334>`_

  * `ReadGroupSet IDs <https://developers.google.com/apis-explorer/#p/genomics/v1beta2/genomics.readgroupsets.search?fields=readGroupSets(id%252Cname)&_h=5&resource=%257B%250A++%2522datasetIds%2522%253A+%250A++%255B%25223049512673186936334%2522%250A++%255D%250A%257D&>`_
  * `Variant Reference Bounds <https://developers.google.com/apis-explorer/#p/genomics/v1beta2/genomics.variantsets.get?variantSetId=3049512673186936334&_h=2&>`_

* Google BigQuery Dataset ID `genomics-public-data:platinum_genomes <https://bigquery.cloud.google.com/table/genomics-public-data:platinum_genomes.variants>`_

Beacon
------
You can find a `Global Alliance for Genomics and Health Beacon`_ at http://webdev.dnastack.com/p/beacon/platinum?chromosome=1&coordinate=10177&allele=AC

Provenance
----------

* The source files for this data include:
   * All of the BAM files listed at `the EBI FTP site <ftp://ftp.sra.ebi.ac.uk/vol1/ERA172/ERA172924/bam>`_.
   * All of the VCF files were listed at `the Illumina FTP site <ftp://ussd-ftp.illumina.com/>`_ prior to the IlluminaPlatinumGenomes_v6.0 release but they have since been taken down.
* These files were copied to Google Cloud Storage, uploaded to Google Genomics, and the variants were exported to Google BigQuery.
