+--------------------------------------------------------------------------------------------------------------+
| Note: Google Genomics is now Cloud Life Sciences.                                                            |       
| The Google Genomics Cookbook on Read the Docs is not actively                                                |
| maintained and may contain incorrect or outdated information.                                                |
| The cookbook is only available for historical reference. For                                                 |
| the most up to date documentation, view the official Cloud                                                   |
| Life Sciences documentation at https://cloud.google.com/life-sciences.                                       |
|                                                                                                              |
| Also note that much of the Genomics v1 API surface has been                                                  |
| superseded by `Variant Transforms <https://cloud.google.com/life-sciences/docs/how-tos/variant-transforms>`_ |
| and `htsget <https://cloud.google.com/life-sciences/docs/how-tos/reading-data-htsget>`_.                     |
+--------------------------------------------------------------------------------------------------------------+

Simons Genome Diversity Project
===============================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/simons_foundation.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

This dataset comprises 279 publicly available genomes from 127 diverse populations for the `Simons Genome Diversity Project <https://www.simonsfoundation.org/life-sciences/simons-genome-diversity-project-dataset/>`_.  See the journal articles for full details:

Pilot Publication

| `The complete genome sequence of a Neanderthal from the Altai Mountains <http://www.nature.com/nature/journal/v505/n7481/full/nature12886.html>`_
| Kay Prufer,	Fernando Racimo,	Nick Patterson,	Flora Jay,	Sriram Sankararaman,	Susanna Sawyer,	Anja Heinze,	Gabriel Renaud,	Peter H. Sudmant,	Cesare de Filippo,	Heng Li, Swapan Mallick,	Michael Dannemann,	Qiaomei Fu,	Martin Kircher,	Martin Kuhlwilm, Michael Lachmann,	Matthias Meyer,	Matthias Ongyerth,	Michael Siebauer,	Christoph Theunert,	Arti Tandon,	Priya Moorjani,	Joseph Pickrell,	James C. Mullikin,	et al.
| Published December 18, 2013
| DOI: 10.1038/nature12886
|

Full Dataset Publication

| `The Simons Genome Diversity Project: 300 genomes from 142 diverse populations <http://www.nature.com/nature/journal/v538/n7624/full/nature18964.html>`_
| Swapan Mallick,	Heng Li,	Mark Lipson,	Iain Mathieson,	Melissa Gymrek,	Fernando Racimo, Mengyao Zhao,	Niru Chennagiri,	Susanne Nordenfelt,	Arti Tandon,	Pontus Skoglund,	Iosif Lazaridis,	Sriram Sankararaman,	Qiaomei Fu,	Nadin Rohland,	Gabriel Renaud,	Yaniv Erlich, Thomas Willems,	Carla Gallo,	Jeffrey P. Spence,	Yun S. Song,	Giovanni Poletti,	Francois Balloux,	George van Driem,	Peter de Knijff	et al.
| Published 21 September 2016
| DOI:10.1038/nature18964
|

Google Cloud Platform data locations
------------------------------------

* Google Cloud Storage folder `gs://genomics-public-data/simons-genome-diversity-project <https://console.cloud.google.com/storage/genomics-public-data/simons-genome-diversity-project/>`_

* Google Genomics datasets

  * 279 genomes from the full dataset project `9897701284241799339 <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.datasets.get?datasetId=9897701284241799339>`_.

    * `Variant Reference Bounds <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.variantsets.get?variantSetId=4975780454274202040>`_

  * 25 genomes from the pilot project `461916304629 <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.datasets.get?datasetId=461916304629>`_.

    * `ReadGroupSet IDs <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.readgroupsets.search?fields=readGroupSets(id%252Cfilename%252Cname)&_h=5&resource=%257B%250A++%2522datasetIds%2522%253A+%250A++%255B%2522461916304629%2522%250A++%255D%250A%257D&>`_

* Google BigQuery Dataset `genomics-public-data:simons_genome_diversity_project <https://bigquery.cloud.google.com/dataset/genomics-public-data:simons_genome_diversity_project>`_

Provenance
----------

.. _sample metadata: http://simonsfoundation.s3.amazonaws.com/share/SCDA/datasets/10_24_2014_SGDP_metainformation_update.txt

For the full dataset of 279 genomes:

* The public VCFs described in the `README <http://reichdata.hms.harvard.edu/pub/datasets/sgdp/>`_ were downloaded from https://sharehost.hms.harvard.edu/genetics/reich_lab/sgdp/vcf_variants/ and extracted to `gs://genomics-public-data/simons-genome-diversity-project`_.
* These files were then imported to Google Genomics and the variants were exported to Google BigQuery as table `genomics-public-data:simons_genome_diversity_project.single_sample_genome_calls <https://bigquery.cloud.google.com/table/genomics-public-data:simons_genome_diversity_project.single_sample_genome_calls?tab=details>`_.
* The `sample metadata`_ was loaded to table `genomics-public-data:simons_genome_diversity_project.sample_metadata <https://bigquery.cloud.google.com/table/genomics-public-data:simons_genome_diversity_project.sample_metadata>`_ using the following commands:

  .. code-block:: shell

    wget http://simonsfoundation.s3.amazonaws.com/share/SCDA/datasets/10_24_2014_SGDP_metainformation_update.txt
    # Strip blank lines from end of file and white space from end of lines.
    sed ':a;/^[\t\r\n]*$/{$d;N;ba}' 10_24_2014_SGDP_metainformation_update.txt \
      | sed 's/\s*$//g' > 10_24_2014_SGDP_metainformation_update.tsv
    bq load --autodetect \
      simons_genome_diversity_project.sample_metadata 10_24_2014_SGDP_metainformation_update.tsv

* The `sample metadata`_ does not use the same sample identifiers as in the VCFs and is also missing one row, so sample attributes were

  * retrieved from http://www.ebi.ac.uk/ena/data/view/PRJEB9586
  * and reshaped into table `genomics-public-data:simons_genome_diversity_project.sample_attributes <https://bigquery.cloud.google.com/table/genomics-public-data:simons_genome_diversity_project.sample_attributes?tab=details>`_
  * using script `wrangle-simons-sample-attributes.R <https://github.com/googlegenomics/bigquery-examples/blob/master/sgdp/provenance/wrangle-simons-sample-attributes.R>`_.
  * This script also re-maps three samples whose ids in the source VCFs did not match the corresponding Illumina ID attribute on EBI.

For the pilot dataset of 25 genomes, the BAMs were imported into Google Genomics.
