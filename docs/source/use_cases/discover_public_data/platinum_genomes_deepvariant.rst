Platinum Genomes DeepVariant
============================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/platinum_genomes_deepvariant.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

This dataset comprises the `6 member CEPH pedigree 1463 <http://www.ebi.ac.uk/ena/data/view/PRJEB3381>`_ called using the alpha version of the `Verily DeepVariant`_ toolchain aligned to :ref:`vgrch38` reference genome.  See the `DeepVariant preprint <http://biorxiv.org/content/early/2016/12/14/092890>`_ for full details:

|  `Creating a universal SNP and small indel variant caller with deep neural networks <http://biorxiv.org/content/early/2016/12/14/092890>`_
|  Ryan Poplin, Dan Newburger, Jojo Dijamco, Nam Nguyen, Dion Loy, Sam Gross, Cory Y. McLean, Mark A. DePristo
|  DOI: https://doi.org/10.1101/092890
|

Google Cloud Platform data locations
------------------------------------

* Google Cloud Storage folder `gs://genomics-public-data/platinum-genomes-deepvariant <https://console.cloud.google.com/storage/genomics-public-data/platinum-genomes-deepvariant/>`_
* Google Genomics Dataset ID `14839180708999654392 <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.datasets.get?datasetId=14839180708999654392>`_

  * `Variant Reference Bounds <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.variantsets.get?variantSetId=4775355778792783584>`_

* Google BigQuery Dataset ID `genomics-public-data:platinum_genomes_deepvariant <https://bigquery.cloud.google.com/dataset/genomics-public-data:platinum_genomes_deepvariant>`_

Provenance
----------

* The FASTQ files in `gs://genomics-public-data/platinum-genomes/fastq/ <https://console.cloud.google.com/storage/genomics-public-data/platinum-genomes/fastq/>`_ were run through the DeepVariant toolchain to produce the corresponding ``*.deepvariant.g.vcf`` and ``*.deepvariant.vcf`` files in `gs://genomics-public-data/platinum-genomes-deepvariant/vcf/ <https://console.cloud.google.com/storage/genomics-public-data/platinum-genomes-deepvariant/vcf/>`_.
* These files were then imported to Google Genomics and the variants were exported to Google BigQuery as table `genomics-public-data:platinum_genomes_deepvariant.single_sample_genome_calls <https://bigquery.cloud.google.com/table/genomics-public-data:platinum_genomes_deepvariant.single_sample_genome_calls?tab=details>`_.
* The data was then merged to produce variants-only `multisample-platinum-genomes-deepvariant.vcf <https://console.cloud.google.com/storage/genomics-public-data/platinum-genomes-deepvariant/multisample-vcf/>`_ and  table `genomics-public-data:platinum_genomes_deepvariant.multisample_variants <https://bigquery.cloud.google.com/table/genomics-public-data:platinum_genomes_deepvariant.multisample_variants?tab=details>`_.

  * The merging logic:

    * groups together only single- and multi-nucleotide polymorphisms with the same reference representation and alternate allele length that originate at the same chromosome and reference position
    * merges all insertions at the same reference position, and
    * splits complex variants into multiple records.
  * Individual variants with GQ < 20 are hard-masked to no-calls, with the genotype likelihoods retained.
