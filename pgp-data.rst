Google is hosting a copy of the PGP Harvard data in Google Cloud Storage. 
All of the data is in this bucket: ``gs://pgp-harvard-data-public``

If you wish to browse the data you will need to 
`install gsutil <https://developers.google.com/storage/docs/gsutil_install>`_.

Once installed, you can run the ``ls`` command on the pgp bucket::

  $ gsutil ls gs://pgp-harvard-data-public
  gs://pgp-harvard-data-public/cgi_disk_20130601_00C68/
  gs://pgp-harvard-data-public/hu011C57/
  gs://pgp-harvard-data-public/hu016B28/
  ....lots more....

The sub folders are PGP IDs, so if we ``ls`` a specific one::

  $ gsutil ls gs://pgp-harvard-data-public/hu011C57/
  gs://pgp-harvard-data-public/hu011C57/GS000018120-DID/

And then keep diving down through the structure, you can end up here::

  $ gsutil ls gs://pgp-harvard-data-public/hu011C57/GS000018120-DID/GS000015172-ASM/GS01669-DNA_B05/ASM/
  gs://pgp-harvard-data-public/hu011C57/GS000018120-DID/GS000015172-ASM/GS01669-DNA_B05/ASM/dbSNPAnnotated-GS000015172-ASM.tsv.bz2
  gs://pgp-harvard-data-public/hu011C57/GS000018120-DID/GS000015172-ASM/GS01669-DNA_B05/ASM/gene-GS000015172-ASM.tsv.bz2
  ... and more ...


Your genome data is located at:
gs://pgp-harvard-data-public/{YOUR_PGP_ID}

If you do not see the data you are looking for, you should contact 
PGP directly through `your web profile <https://my.pgp-hms.org/message/new>`_.
