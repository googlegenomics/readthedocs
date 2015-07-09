**Do a "dry run"** (*optional*)

The tool supports the ``DRYRUN`` environment variable.
Setting this value to 1 when launching your job will cause the queued
job to execute *without downloading or uploading* any files.

The local output files, however, will be populated with useful information
about what files *would* be copied. This can be useful for ensuring your
file list is valid and that the output path is correct.
