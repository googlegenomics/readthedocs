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

Interval JOINs
==============

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/annotate_variants/interval_joins.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

If you want to use BigQuery to JOIN variants with other data described by genomic region intervals (overlaps), this page demonstrates the use of a complex JOIN predicate.

Example
-------

Let's use a concrete example: Suppose you have a list of gene names and you want to find all the rare SNPs overlapping those genes and also 100,000 bp on either side of the gene for all of your whole genome samples.

(1) The first thing we need to do is load or create our table of intervals.

* If you have a BED file containing your intervals of interest, you can upload that to BigQuery and use it directly.
* Alternatively, the :doc:`/use_cases/discover_public_data/tute_genomics_public_data` table has the gene positions for hg19 which we can use to create our interval table.  For example:

.. code::

  SELECT
    Gene,
    Chr,
    MIN(Start) AS gene_start,
    MAX(`End`) AS gene_end,
    MIN(Start) - 100000 AS region_start,
    MAX(`End`) + 100000 AS region_end
  FROM
    `silver-wall-555.TuteTable.hg19`
  WHERE
    Gene IN ('APC', 'ATM', 'BMPR1A', 'BRCA1', 'BRCA2', 'CDK4',
    'CDKN2A', 'CREBBP', 'EGFR', 'EP300', 'ETV6', 'FHIT', 'FLT3',
    'HRAS', 'KIT', 'MET', 'MLH1', 'NTRK1', 'PAX8', 'PDGFRA',
    'PPARG', 'PRCC', 'PRKAR1A', 'PTEN', 'RET', 'STK11',
    'TFE3', 'TGFB1', 'TGFBR2', 'TP53', 'WWOX')
  GROUP BY
    Chr,
    Gene

(2) Suppose we have materialized our interval table to ``test.myIntervalTable`` and at a minimum it contains columns ``region_start`` and ``region_end``.  Now we can run the following query to identify rare variants within our cohort that overlap the regions of interest.

.. code::

  WITH
    --
    -- Retrieve the variants in this cohort, flattening by alternate bases and
    -- counting affected alleles.
    variants AS (
    SELECT
      reference_name,
      start,
      `end`,
      reference_bases,
      alt,
      (SELECT COUNTIF(gt = alt_offset+1) FROM v.call call, call.genotype gt) AS num_variant_alleles,
      (SELECT COUNTIF(gt >= 0) FROM v.call call, call.genotype gt) AS total_num_alleles
    FROM
      `genomics-public-data.1000_genomes_phase_3.variants_20150220_release` v,
      v.alternate_bases alt WITH OFFSET alt_offset ),
    --
    -- JOIN the variants with the genomic intervals overlapping
    -- the genes of interest.
    --
    -- The JOIN criteria is complicated since we are trying to see if a SNP
    -- overlaps an interval.  With standard SQL we can use complex JOIN
    -- predicates, including arbitrary expressions.
    gene_variants AS (
    SELECT
      reference_name,
      start,
      reference_bases,
      alt,
      num_variant_alleles,
      total_num_alleles
    FROM
      variants
    JOIN
      test.myIntervalTable AS intervals ON
      variants.reference_name = intervals.Chr
      AND intervals.region_start <= variants.start
      AND intervals.region_end >= variants.`end` ),
    --
    -- Retrieve annotations for rare variants only.
    rare_variant_annotations AS (
    SELECT
      Chr,
      Start,
      Ref,
      Alt,
      Func,
      Gene,
      PopFreqMax,
      ExonicFunc
    FROM
      `silver-wall-555.TuteTable.hg19`
    WHERE
      PopFreqMax <= 0.01 )
    --
    -- And finally JOIN the variants in the regions of interest
    -- with annotations for rare variants.
  SELECT
    Chr,
    annots.Start AS Start,
    Ref,
    annots.Alt,
    Func,
    Gene,
    PopFreqMax,
    ExonicFunc,
    num_variant_alleles,
    total_num_alleles
  FROM
    rare_variant_annotations AS annots
  JOIN
    gene_variants AS vars
  ON
    vars.reference_name = annots.Chr
    AND vars.start = annots.Start
    AND vars.reference_bases = annots.Ref
    AND vars.alt = annots.Alt
  ORDER BY
    Chr,
    Start

Results
-------

A specific run of the above interval JOIN took

.. code::

  Query complete (92.1s elapsed, 3.38 TB processed)

on:

  * 2,504 samples for 84,801,867 phase 3 variants from :doc:`/use_cases/discover_public_data/1000_genomes`
  * the nearly 9 billion row :doc:`/use_cases/discover_public_data/tute_genomics_public_data` table
  * and a gene list containing 250 randomly chosen genes via the following query

  .. code::

    SELECT
      Gene,
      Chr,
      MIN(Start) AS gene_start,
      MAX(`End`) AS gene_end,
      MIN(Start) - 100000 AS region_start,
      MAX(`End`) + 100000 AS region_end
    FROM
      `silver-wall-555.TuteTable.hg19`
    WHERE
      Gene IN (SELECT Gene FROM `silver-wall-555.TuteTable.hg19` GROUP BY Gene LIMIT 250)
    GROUP BY
      Chr,
      Gene
