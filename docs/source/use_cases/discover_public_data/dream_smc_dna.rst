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

ICGC-TCGA DREAM Mutation Calling Challenge synthetic genomes
=============================================================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/dream_smc_dna.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

This dataset comprises the three public synthetic tumor/normal pairs created for the `ICGC-TCGA DREAM Mutation Calling challenge <https://www.synapse.org/#!Synapse:syn312572/wiki/>`_.  See the journal article for full details regarding how the synthetic data for challenge *in silico #1* was created:

|  `Combining tumor genome simulation with crowdsourcing to benchmark somatic single-nucleotide-variant detection <http://www.nature.com/nmeth/journal/vaop/ncurrent/full/nmeth.3407.html>`_
|  Adam D Ewing,	Kathleen E Houlahan,	Yin Hu,	Kyle Ellrott,	Cristian Caloian,
|  Takafumi N Yamaguchi,	J Christopher Bare,	Christine P'ng,	Daryl Waggott,
|  Veronica Y Sabelnykova, ICGC-TCGA DREAM Somatic Mutation Calling Challenge participants,
|  Michael R Kellen, Thea C Norman,	David Haussler,	Stephen H Friend,	Gustavo Stolovitzky,
|  Adam A Margolin, Joshua M Stuart	& Paul C Boutros
|  Published: May 18, 2015
|  DOI: 10.1038/nmeth.3407
|

Google Cloud Platform data locations
------------------------------------
* Google Cloud Storage folder `gs://public-dream-data/ <https://console.cloud.google.com/storage/browser/public-dream-data/>`_
* Google Genomics dataset `337315832689 <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.datasets.get?datasetId=337315832689>`_.

Provenance
----------

* The authoritative data location is NCBI Sequence Read Archive: `SRP042948 <http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?study=SRP042948>`_.
* The BAMs were uploaded to Google Cloud Storage and the reads were then imported to Google Genomics.
