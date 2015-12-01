Migrating from v1beta to v1beta2
--------------------------------

The v1beta2 version of the Google Genomics API is now available and all client 
code should migrate to it by the end of 2014.

**If you are using the genomics-tools-client-java jar from the command line** - 
upgrading is as easy as `downloading a new jar <https://cloud.google.com/genomics#install>`_. 
(Or running ``git pull; mvn package`` from your git client)

For all other integrations: 
v1beta2 matches the `GA4GH API v0.5.1 <http://ga4gh.org/#/api>`_, which means that there are quite
a few method and field renames to deal with. This page summarizes all the
changes necessary to move to the latest API.

new version notes
~~~~~~~~~~~~~~~~~
General
  * ``maxResults`` is now ``pageSize``, and is an integer

Datasets and Jobs
  * All usages of ``projectId`` should be replaced by ``projectNumber``
  * ``job.description`` is now ``job.detailedStatus``

Variants
  * The variant objects have not changed.
  * The import and export methods have slightly different URLs. 
    ``/variants/import`` is now ``/variantsets/<variantSetId>/importVariants`` and 
    ``/variants/export`` is ``/variantsets/<variantSetId>/export``.
    These affect the generated client libraries slightly.

Readsets/Readgroupsets
  * ``readset`` has now been renamed to ``readgroupset``. This is mostly a straightforward replacement of the term. 
  * ``readset.fileData[0].fileUri`` is now ``readgroupset.filename``
  * ``readset.fileData[0].refSequences`` is replaced by ``readgroupset.referenceSetId``
  * The rest of the ``readset.fileData`` field has been replaced by information within 
    the ``readgroupset.readgroups`` array.
  
Reads
  * All read positions are now 0-based longs, just like the variant positions.
  * ``originalBases`` is now ``alignedSequence``
  * ``alignedBases`` (``originalBases`` with the cigar applied) has been removed
  * ``baseQuality`` is now an int array called ``alignedQuality``. You no longer 
    need to subtract 33 or deal with ASCII conversion.
  * ``name`` is now ``fragmentName``
  * ``templateLength`` is now ``fragmentLength``
  * ``tags`` is now ``info``
  * ``position`` is now ``alignment.position.position``. The alignment object now contains
    all alignment-related information - including the cigar, reference name, 
    and whether the read is on the reverse strand.
  * The old ``cigar`` string is now the structured field ``alignment.cigar``. To get 
    an old-style cigar string, iterate over each element in the array, and
    concat the ``operationLength`` with a mapped version of ``operation``. pseudocode::
    
      cigar_enums = {ALIGNMENT_MATCH: "M", CLIP_HARD: "H", CLIP_SOFT: "S", DELETE: "D",
          INSERT: "I", PAD: "P", SEQUENCE_MATCH: "=", SEQUENCE_MISMATCH: "X", SKIP: "N"}

      cigar_string = [c.operationLength + cigar_enums[c.operation] for c in read.alignment.cigar].join('')
     
     
  * The old ``flags`` integer is now represented by many different first class fields.
    To reconstruct a flags value, you need code similar to this pseudocode::
    
      flags = 0
      flags += read.numberReads == 2 ? 1 : 0 #read_paired
      flags += read.properPlacement ? 2 : 0 #read_proper_pair
      flags += read.alignment == null ? 4 : 0 #read_unmapped
      flags += read.nextMatePosition == null ? 8 : 0 #mate_unmapped
      flags += read.alignment.position.reverseStrand ? 16 : 0 #read_reverse_strand
      flags += read.nextMatePosition.reverseStrand ? 32 : 0 #mate_reverse_strand
      flags += read.readNumber == 0 ? 64 : 0 #first_in_pair
      flags += read.readNumber == 1 ? 128 : 0 #second_in_pair
      flags += read.secondaryAlignment ? 256 : 0 #secondary_alignment
      flags += read.failedVendorQualityChecks ? 512 : 0 #failed_quality_check
      flags += read.duplicateFragment ? 1024 : 0 #duplicate_read
      flags += read.supplementaryAlignment ? 2048 : 0 #supplementary_alignment
      

reads/search
  * ``sequenceName`` is now ``referenceName``
  * ``sequenceStart`` is now ``start``
  * ``sequenceEnd`` is now ``end``
  * The response from reads/search now returns a field called ``alignments`` rather than ``reads``
