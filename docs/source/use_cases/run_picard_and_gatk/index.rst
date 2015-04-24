Run Picard and GATK tools over genomics data from the cloud
===========================================================
Picard and GATK tools are popular utilities used for genomics analysis and 
processing pipelines.

They usually work with BAM files but we are working on teaching them to work 
with the genomics data in the cloud.

If your dataset is loaded into a cloud provider supporting GA4GH API 
(e.g. Google Genomics) or you want to use one of 
the available `public datasets <https://cloud.google.com/genomics/public-data>`_,
you can check out `gatk-tools-java <https://github.com/googlegenomics/gatk-tools-java>`_
library that makes it possible to run some Picard tools against genomics data 
in the cloud.

It is now also possible to make a special build of Picard tools 
that will have this support built in by default.

See https://github.com/broadinstitute/picard/blob/master/README.md for details.