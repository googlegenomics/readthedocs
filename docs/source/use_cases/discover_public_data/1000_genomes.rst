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

1,000 Genomes
=============

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/1000_genomes.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

This dataset comprises roughly 2,500 genomes from 25 populations around the world.  See the `1,000 Genomes project website <http://www.1000genomes.org/>`_ and publications for full details:

Pilot publication

| `An integrated map of genetic variation from 1,092 human genomes <http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3498066/>`_
| The 1000 Genomes Project Consortium
| Published: November 1, 2012
| DOI: 10.1038/nature11632
|

Phase 1 publication

| `A map of human genome variation from population scale sequencing <http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3042601/>`_
| The 1000 Genomes Project Consortium
| Published: October 28, 2010
| DOI: 10.1038/nature09534
|

Phase 3 publications

| `A global reference for human genetic variation <http://www.nature.com/nature/journal/v526/n7571/full/nature15393.html>`_
| The 1000 Genomes Project Consortium
| Published: September 30,2015
| DOI: 10.1038/nature15393
|

| `An integrated map of structural variation in 2,504 human genomes <http://www.nature.com/nature/journal/v526/n7571/full/nature15394.html>`_
| The 1000 Genomes Project Consortium
| Published: September 30,2015
| DOI: 10.1038/nature15394
|

Google Cloud Platform data locations
------------------------------------

* Google Cloud Storage folders
   * These files were loaded into Google Genomics datasets:
      * `gs://genomics-public-data/1000-genomes <https://console.cloud.google.com/storage/genomics-public-data/1000-genomes/>`_
      * `gs://genomics-public-data/1000-genomes-phase-3 <https://console.cloud.google.com/storage/genomics-public-data/1000-genomes-phase-3/>`_
   * A full mirror of http://ftp-trace.ncbi.nih.gov/1000genomes/ftp/ in is Cloud Storage location `gs://genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/ <https://console.cloud.google.com/storage/browser/genomics-public-data/ftp-trace.ncbi.nih.gov/1000genomes/ftp/>`_.
* Google Genomics Dataset IDs
   * Dataset Id `10473108253681171589 <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.datasets.get?datasetId=10473108253681171589>`_

     * `ReadGroupSet IDs <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.readgroupsets.search?fields=readGroupSets(id%252Cname)&_h=5&resource=%257B%250A++%2522datasetIds%2522%253A+%250A++%255B%252210473108253681171589%2522%250A++%255D%250A%257D&>`_ for the Phase 3 reads
     * Phase 1 variants

       * Variant Set Id: ``10473108253681171589``
       * `Reference Bounds <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.variantsets.get?variantSetId=10473108253681171589&_h=2&>`__
     * Phase 3 variants - `20150220 Release <http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/README_phase3_callset_20150220>`_

       * Variant Set Id: ``11027761582969783635``
       * `Reference Bounds <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.variantsets.get?variantSetId=11027761582969783635&_h=2&>`__

   * Dataset Id `4252737135923902652 <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.datasets.get?datasetId=4252737135923902652>`_

     * Phase 3 variants - initial release

       * Variant Set Id: ``4252737135923902652``
       * `Reference Bounds <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.variantsets.get?variantSetId=4252737135923902652&_h=2&>`__

* Google BigQuery Dataset IDs
   * `genomics-public-data:1000_genomes <https://bigquery.cloud.google.com/table/genomics-public-data:1000_genomes.variants>`_ phase 1 variants and sample information
   * `genomics-public-data:1000_genomes_phase_3 <https://bigquery.cloud.google.com/table/genomics-public-data:1000_genomes_phase_3.variants_20150220_release>`_ phase 3 variants

Beacon and GA4GH
----------------

You can find a `Global Alliance for Genomics and Health Beacon`_ at http://webdev.dnastack.com/p/beacon/thousandgenomes?chromosome=1&coordinate=10177&allele=AC

You can find an instance of the GA4GH reference server hosting this data at http://1kgenomes.ga4gh.org/.

Provenance
----------

The source files for this dataset include:
 * The mapped full-genome phase 3 BAM files listed at `the 1000 Genomes FTP site <ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/alignment_indices/20130502.low_coverage.alignment.index>`_.

  * All of the phase 1 VCF files listed at `the 1000 Genomes FTP site <ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase1/analysis_results/integrated_call_sets/>`__.
  * All of the phase 3 VCF files listed at `the 1000 Genomes FTP site <ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502>`__.

* These files were copied to Google Cloud Storage, uploaded to Google Genomics, and the variants were exported to Google BigQuery.

