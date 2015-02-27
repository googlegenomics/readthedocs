Clearing stored credentials
---------------------------

The first time the Java client makes an API request, it authenticates the caller 
with OAuth and stores the resulting credentials for all future API calls.

If you wish to remove these stored credentials (to authenticate with a different 
client secrets file, or as a different user, etc), you will need to remove the 
storage directory with this command::

  rm ~/.store/genomics_java_client/StoredCredential
  
The next request made to the Java client will then require a browser to open the OAuth pages.
