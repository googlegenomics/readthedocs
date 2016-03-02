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

If you want to use BigQuery to JOIN variants with other data described by genomic region intervals (overlaps), this page offers a technique to reduce the cross-product and speed up the query by applying `Google BigQuery user-defined functions`_.

Example
-------

Let's use a concrete example: *Suppose you have a list of genes names and you want to find all the rare SNPs overlapping those genes and also 100,000 bp on either side of the gene for all of your whole genome samples.*

(1) Upload the tab-separated value gene list to BigQuery as ``myGeneListTable``.

(2) The :doc:`/use_cases/discover_public_data/tute_genomics_public_data` table has the gene positions for hg19. Then create your interval table and materialize it to ``myIntervalTable``.

.. code::

  SELECT
    Gene,
    Chr,
    MIN(Start) AS gene_start,
    MAX(END) AS gene_end,
    MIN(Start) - 100000 AS region_start,
    MAX(END) + 100000 AS region_end,
  FROM
    [silver-wall-555:TuteTable.hg19]
  WHERE
    Gene IN (
    SELECT
      gene
    FROM
      [myGeneListTable])
  GROUP BY
    Chr,
    Gene

Alternatively, upload a BED file to BigQuery containing your intervals of interest.

(3) We'll need a user-defined function (UDF) to "bin" our intervals to reduce the cross-product of the JOIN.

Enter this query in the "UDF Editor":

.. code::

  function binIntervals(row, emit) {
    var binSize = 50000;  // Make sure this matches the value in the SQL
    var startBin = Math.floor(row.region_start / binSize);
    var endBin = Math.floor(row.region_end / binSize);
    // Since an interval can span multiple bins, emit
    // a record for each bin it spans.
    for(var bin = startBin; bin <= endBin; bin++) {
      emit({gene: row.gene,
            Chr: row.Chr,
            region_start: row.region_start,
            region_end: row.region_end,
            bin: bin,
           });
    }
  }

  bigquery.defineFunction(
    'binIntervals',                                // Name of the function exported to SQL
    ['gene', 'Chr', 'region_start', 'region_end'], // Names of input columns
    [{'name': 'gene', 'type': 'string'},           // Output schema
     {'name': 'Chr', 'type': 'string'},
     {'name': 'region_start', 'type': 'integer'},
     {'name': 'region_end', 'type': 'integer'},
     {'name': 'bin', 'type': 'integer'}],
    binIntervals                                   // Reference to JavaScript UDF
  );

(4) Run the query.

Enter this query in the "Query Editor":

.. code::

  SELECT
    Chr,
    annots.Start AS Start,
    Ref,
    Alt,
    Func,
    Gene,
    PopFreqMax,
    ExonicFunc,
    SUM(num_variant_alleles) AS num_variant_alleles,
    SUM(total_num_alleles) AS total_num_alleles
  FROM (
    SELECT
      Chr,
      Start,
      Ref,
      Alt,
      Func,
      Gene,
      PopFreqMax,
      ExonicFunc,
    FROM
      [silver-wall-555:TuteTable.hg19]
    WHERE
      PopFreqMax <= 0.01 ) AS annots
  JOIN EACH (
    SELECT
      reference_name,
      start,
      reference_bases,
      alternate_bases,
      num_variant_alleles,
      total_num_alleles,
      vars.bin,
    FROM (
      SELECT
        reference_name,
        start,
        END,
        reference_bases,
        NTH(1, alternate_bases) WITHIN RECORD AS alternate_bases,
        SUM(call.genotype = 1) WITHIN RECORD AS num_variant_alleles,
        SUM(call.genotype >= 0) WITHIN RECORD AS total_num_alleles,
        # This must match the bin size in the UDF.
        INTEGER(FLOOR(start / 50000)) AS bin,
      FROM
        [genomics-public-data:1000_genomes_phase_3.variants_20150220_release]) AS vars
    JOIN (
      SELECT
        gene,
        Chr,
        region_start,
        region_end,
        bin,
      FROM (binIntervals([myIntervalTable]))) AS intervals
      # The JOIN criteria is complicated since we are trying to see if a SNP
      # overlaps an interval.
    ON
      vars.reference_name = intervals.Chr
      AND vars.bin = intervals.bin
    WHERE
      intervals.region_start <= vars.start
      AND intervals.region_end >= vars.END) AS s_vars
  ON
    s_vars.reference_name = annots.Chr
    AND s_vars.start = annots.Start
    AND s_vars.reference_bases = annots.Ref
    AND s_vars.alternate_bases = annots.Alt
  GROUP BY
    Chr,
    Start,
    Ref,
    Alt,
    Func,
    Gene,
    PopFreqMax,
    ExonicFunc,
  ORDER BY
    Chr,
    Start

The Tute table is for SNP annotation.  If a different table were used to annotate both SNPs and INDELs, you may wish to apply a similar UDF to also "bin" the rows from the variants table, since INDELs may span multiple bins.

.. sidebar:: Bin Size

  Notice the bin size of 50,000 base pairs.  This value can be changed, but be sure to change it in both the UDF and the SQL.

Results
-------

A specific run of the above interval JOIN took `Query complete (223.9s elapsed, 3.38 TB processed)` on:

  * 2,504 samples for 84,801,867 phase 3 variants from :doc:`/use_cases/discover_public_data/1000_genomes`
  * the nearly 9 billion row :doc:`/use_cases/discover_public_data/tute_genomics_public_data` table
  * and a gene list containing 240 genes.

This second version of the query is a little faster.  It applies the intervals to the annotations first (whereas the other query applied the intervals to the variants first).  They are pretty comparable though, so either is fine.  The goal is to just filter as soon as possible (e.g., within inner queries).

.. code::

  SELECT
    Chr,
    rare_snps.Start AS Start,
    Ref,
    Alt,
    Func,
    Gene,
    PopFreqMax,
    ExonicFunc,
    SUM(num_variant_alleles) AS num_variant_alleles,
    SUM(total_num_alleles) AS total_num_alleles
  FROM (
    SELECT
      reference_name,
      start,
      END,
      reference_bases,
      NTH(1, alternate_bases) WITHIN RECORD AS alternate_bases,
      SUM(call.genotype = 1) WITHIN RECORD AS num_variant_alleles,
      SUM(call.genotype >= 0) WITHIN RECORD AS total_num_alleles,
    FROM
      [genomics-public-data:1000_genomes_phase_3.variants_20150220_release]) AS vars
  JOIN EACH (
    SELECT
      annots.Chr AS Chr,
      Start,
      Ref,
      Alt,
      Func,
      annots.Gene AS Gene,
      PopFreqMax,
      ExonicFunc,
    FROM (
      SELECT
        Chr,
        Start,
        Ref,
        Alt,
        Func,
        Gene,
        PopFreqMax,
        ExonicFunc,
        INTEGER(FLOOR(start / 50000)) AS bin,
      FROM
        [silver-wall-555:TuteTable.hg19]
      WHERE
        PopFreqMax <= 0.01) AS annots
    JOIN (
      SELECT
        Chr,
        region_start,
        region_end,
        bin,
      FROM (binIntervals([myIntervalTable]))) AS intervals
      # The JOIN criteria is complicated since we are trying to see if a SNP
      # overlaps an interval.
    ON
      annots.Chr = intervals.Chr
      AND annots.bin = intervals.bin
    WHERE
      intervals.region_start <= annots.start
      AND intervals.region_end >= annots.start + 1) AS rare_snps
  ON
    vars.reference_name = rare_snps.Chr
    AND vars.start = rare_snps.Start
    AND vars.reference_bases = rare_snps.Ref
    AND vars.alternate_bases = rare_snps.Alt
  GROUP BY
    Chr,
    Start,
    Ref,
    Alt,
    Func,
    Gene,
    PopFreqMax,
    ExonicFunc,
  ORDER BY
    Chr,
    Start
