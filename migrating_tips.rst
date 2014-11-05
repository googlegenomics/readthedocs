Migrating from v1beta to v1beta2
--------------------------------

The v1beta2 version of the Google Genomics API is now available and all client 
code should migrate to it by the end of 2014.

v1beta2 matches the `GA4GH API v0.5.1 <http://ga4gh.org/#/api>`_, which means that there are quite
a few method and field renames to deal with. This page summarizes all the
changes necessary to move to the latest API.

new version notes
~~~~~~~~~~~~~~~~~
General
  * `maxResults` is now `pageSize`, and is an integer

Datasets and Jobs
  * All usages of `projectId` should be replaced by `projectNumber`
  * `job.description` is now `job.detailedStatus`

Variants
  * The variant related API calls have not changed. No code modifications are necessary.

Readsets/Readgroupsets
  * `readset` has now been renamed to `readgroupset`. This is mostly a straightforward replacement of the term. 
  * `readset.fileData[0].fileUri` is now `readgroupset.filename`
  * The rest of the `readset.fileData` field has been replaced by information within 
    the `readgroupset.readgroups` array.
  
Reads
  * All read positions are now 0-based longs, just like the variant positions.
  * `originalBases` is now `alignedSequence`
  * `alignedBases` (`originalBases` with the cigar applied) has been removed
  * `position` is now `alignment.position.position`. The alignment object now contains
    all alignment-related information - the cigar, reference name, etc
  * The old `cigar` string is now the structured field `alignment.cigar`. To get 
    an old-style cigar string, iterate over each element in the array, and
    concat the `operationLength` with a mapped version of `operation`. pseudocode::
    
      cigar_enums = {ALIGNMENT_MATCH: "M", CLIP_HARD: "H", CLIP_SOFT: "S", DELETE: "D",
          INSERT: "I", PAD: "P", SEQUENCE_MATCH: "=", SEQUENCE_MISMATCH: "X", SKIP: "N"}

      cigar_string = [c.operationLength + cigar_enums[c.operation] for c in read.alignment.cigar].join('')

reads/search
  * `sequenceName` is now `referenceName`
  * `sequenceStart` is now `start`
  * `sequenceEnd` is now `end`
  * The response from reads/search now returns a field called `alignments` rather than `reads`
