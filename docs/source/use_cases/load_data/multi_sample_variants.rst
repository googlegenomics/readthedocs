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

Multi-Sample Variants Format
============================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/load_data/multi_sample_variants.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs


If your source data is jointly-called (e.g., like :doc:`/use_cases/discover_public_data/1000_genomes`) it will already be in "multi-sample variants" format when it is exported from the Variants API to Google BigQuery.

If your source data is single-sample `gVCF`_ or Complete Genomics masterVar format, this page offers some solutions to convert it to multi-sample variants format.

Overview
--------

Suppose you have imported your single-sample files to the Variants API and exported them to BigQuery. Let's refer to this original table as the "genome calls" table. It contains *all* reference calls and variant calls.

To facilitate variant-centric analysis like we see in the `BigQuery 1,000 Genomes samples <https://github.com/googlegenomics/bigquery-examples/blob/master/1000genomes/README.md>`_, we can generate a second table, the "multi-sample variants" table. The multi-sample variants table resembles a multi-sample VCF file. In this table:

* every variant record includes calls for *all* callsets
* variants which contained *only reference calls for all callsets* are omitted

Motivation
----------

Data from source files in `genome VCF`_ (gVCF) format or in Complete Genomics format can be challenging to query due to the presence of non-variant segment records.

For example to lookup `rs9536314 <http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs9536314>`_ in the Klotho gene, the `WHERE` clause

.. code::

    WHERE
      reference_name = 'chr13'
      AND start = 33628137

becomes

.. code::

    WHERE
      reference_name = 'chr13'
      AND start <= 33628137
      AND end >= 33628138

to capture not only that variant, but any other records that overlap that genomic position.

Suppose we want to calculate an aggregate for a particular variant, such as the number of samples with the variant on one or both alleles and of samples that match the reference?  The WHERE clause above will do the trick. But then suppose we want to do this for all SNPs in our dataset?

Examples
--------

There are a few ways to generate the multi-sample variants table for use in variant-centric analyses such as :doc:`/use_cases/analyze_variants/gwas`:

* Use a cluster computing job to transform data with non-variant segments to variant-only data with calls from non-variant-segments merged into the variants with which they overlap. This is currently done only for SNP variants. Indels and structural variants are left as-is.

  * see the `Dataflow example <https://github.com/googlegenomics/codelabs/tree/master/Java/PlatinumGenomes-variant-transformation>`_
  * see the `Hadoop Streaming example <https://github.com/googlegenomics/codelabs/tree/master/Python/PlatinumGenomes-variant-transformation>`_

* Use BigQuery to transform the data, materialize the result to a new table

  * https://github.com/googlegenomics/bigquery-examples/tree/master/pgp/data-stories/schema-comparisons#motivation

A note about scaling: as the number of samples increases, so does the number of private and rare variants. At a certain point there are many, many rows with mostly 0/0 genotypes. We are experimenting with alternate transformations. Comment on `this issue <https://github.com/googlegenomics/codelabs/issues/52>`_ if you want a pointer to the most recent prototype.
