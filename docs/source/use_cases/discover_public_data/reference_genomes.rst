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

Reference Genomes
===========================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/reference_genomes.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

Reference Genomes such as GRCh37, GRCh37lite, GRCh38, hg19, hs37d5, and b37 are available on Google Cloud Platform.

Google Cloud Platform data locations
------------------------------------

* Google Cloud Storage folder `gs://genomics-public-data/references <https://console.cloud.google.com/storage/genomics-public-data/references/>`_
* Google Genomics `reference sets <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.referencesets.search>`_

Provenance
----------

GRCh37
^^^^^^

Genome Reference Consortium Human Build 37 includes data from 35 gzipped fasta files:

* `assembled chromosomes <ftp://ftp.ncbi.nlm.nih.gov/genbank/genomes/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh37/Primary_Assembly/assembled_chromosomes/FASTA>`__
* `unlocalized scaffolds <ftp://ftp.ncbi.nlm.nih.gov/genbank/genomes/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh37/Primary_Assembly/unlocalized_scaffolds/FASTA>`__
* `unplaced scaffolds <ftp://ftp.ncbi.nlm.nih.gov/genbank/genomes/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh37/Primary_Assembly/unplaced_scaffolds/FASTA>`__

More information on this source data can be found in this `NCBI article <http://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.13/>`__ and in the `FTP README <ftp://ftp.ncbi.nlm.nih.gov/genbank/genomes/README_ASSEMBLIES>`__.

GRCh37lite
^^^^^^^^^^

GRCh37lite is a subset of the full GRCh37 reference set plus the human mitochondrial genome reference sequence in one file: `GRCH37-lite.fa.gz <ftp://ftp.ncbi.nih.gov/genbank/genomes/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh37/special_requests/>`_

More information on this source data can be found in the `FTP README <ftp://ftp.ncbi.nih.gov/genbank/genomes/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh37/special_requests/README.GRCh37-lite>`__.

GRCh38
^^^^^^

Genome Reference Consortium Human Build 38 includes data from 39 gzipped fasta files:

* `assembled chromosomes <ftp://ftp.ncbi.nlm.nih.gov/genbank/genomes/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh38/Primary_Assembly/assembled_chromosomes/FASTA>`__
* `unlocalized scaffolds <ftp://ftp.ncbi.nlm.nih.gov/genbank/genomes/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh38/Primary_Assembly/unlocalized_scaffolds/FASTA>`__
* `unplaced scaffolds <ftp://ftp.ncbi.nlm.nih.gov/genbank/genomes/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh38/Primary_Assembly/unplaced_scaffolds/FASTA>`__
* `non-nuclear references <ftp://ftp.ncbi.nlm.nih.gov/genbank/genomes/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh38/non-nuclear/assembled_chromosomes/FASTA/>`__

More information on this source data can be found in this `NCBI article <http://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.26/>`__ and in the `FTP README <ftp://ftp.ncbi.nlm.nih.gov/genbank/genomes/README_ASSEMBLIES>`__.


.. _vgrch38:

Verily's GRCh38
^^^^^^^^^^^^^^^

Verily's GRCh38 reference genome is fully compatible with any b38 genome in the autosome.

Verily's GRCh38:

* excludes all patch sequences
* omits alternate haplotype chromosomes
* includes decoy sequences
* masks out duplicate copies of centromeric regions

The base assembly is `GRCh38_no_alt_plus_hs38d1 <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.15_GRCh38/seqs_for_alignment_pipelines.ucsc_ids/GCA_000001405.15_GRCh38_no_alt_plus_hs38d1_analysis_set.fna.gz>`_. This assembly version was created specifically for analysis, with its rationale and exact genome modifications thoroughly documented in its `README <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.15_GRCh38/seqs_for_alignment_pipelines.ucsc_ids/README_analysis_sets.txt>`_ file.

Verily applied the following modifications to the base assembly:

* Reference segment names are prefixed with "chr".

   +--------------------------------------------------------------+
   | Many of the additional data files we use are provided        |
   | by GENCODE, which uses "chr" naming convention.              |
   +--------------------------------------------------------------+

* All 74 extended IUPAC codes are converted to the first matching alphabetical base pair as recommended in the VCF 4.3 specification.

* This release of the genome reference is named ``GRCh38_Verily_v1``

hg19
^^^^

Similar to GRCh37, this is the February 2009 assembly of the human genome with a different mitochondrial sequence and additional alternate haplotype assemblies. Includes data from all 93 gzipped fasta files from `the UCSC FTP site <ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes>`_.

More information on this source data can be found in the `FTP README <ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/README.txt>`__.

hs37d5
^^^^^^

Includes data from GRCh37, the rCRS mitochondrial sequence, Human herpesvirus 4 type 1 and the concatenated decoy sequences in one file: `hs37d5.fa.gz <ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence>`_

More information on this source data can be found in the `FTP README <ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/README_human_reference_20110707>`__.

b37
^^^

The reference genome included by some versions of the GATK software which includes data from GRCh37, the rCRS mitochondrial sequence, and the Human herpesvirus 4 type 1 in one file: `Homo_sapiens_assembly19.fasta <http://www.broadinstitute.org/ftp/pub/seq/references>`_.

More information on this source data can be found in the `GATK FAQs <https://www.broadinstitute.org/gatk/guide/article.php?id=1213>`_.
