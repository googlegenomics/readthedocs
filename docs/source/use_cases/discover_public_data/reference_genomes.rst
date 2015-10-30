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

Reference Genomes such as GRCh37, GRCh37lite, GRCh38, hg19, hs37d5 are available on Google Cloud Platform.

Google Cloud Platform data locations
------------------------------------

* Google Cloud Storage folder `gs://genomics-public-data/references <https://console.developers.google.com/storage/genomics-public-data/references/>`_
* Google Genomics `reference sets <https://developers.google.com/apis-explorer/#p/genomics/v1beta2/genomics.referencesets.search>`_

Provenance
----------

GRCh37
^^^^^^

Genome Reference Consortium Human Build 37 includes data from 35 gzipped fasta files:

* `assembled chromosomes <ftp://ftp.ncbi.nlm.nih.gov/genbank/genomes/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh37/Primary_Assembly/assembled_chromosomes/FASTA>`_
* `unlocalized scaffolds <ftp://ftp.ncbi.nlm.nih.gov/genbank/genomes/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh37/Primary_Assembly/unlocalized_scaffolds/FASTA>`__
* `unplaced scaffolds <ftp://ftp.ncbi.nlm.nih.gov/genbank/genomes/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh37/Primary_Assembly/unplaced_scaffolds/FASTA>`__

More information on this source data can be found in this `NCBI article <http://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.13/>`__ and in the `FTP README <ftp://ftp.ncbi.nlm.nih.gov/genbank/genomes/README_ASSEMBLIES>`__

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

hg19
^^^^

Similar to GRCh37, this is the February 2009 assembly of the human genome with a different mitochondrial sequence and additional alternate haplotype assemblies. Includes data from all 93 gzipped fasta files from `the UCSC FTP site <ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes>`_.

More information on this source data can be found in the `FTP README <ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/README.txt>`__.

hs37d5
^^^^^^

Includes data from GRCh37, the rCRS mitochondrial sequence, Human herpesvirus 4 type 1 and the concatenated decoy sequences in one file: `hs37d5.fa.gz <ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence>`_

More information on this source data can be found in the `FTP README <ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/README_human_reference_20110707>`__.
