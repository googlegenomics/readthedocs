The above command line runs the pipeline locally over a small portion of the genome, only taking a few minutes.  If modified to run over a larger portion of the genome or the entire genome, it may take a few hours depending upon how many virtual machines are configured to run concurrently via ``--numWorkers``.  Add the following additional command line parameters to run the pipeline on Google Cloud instead of locally::

  --runner=DataflowPipelineRunner \
  --project=YOUR-GOOGLE-CLOUD-PLATFORM-PROJECT-ID \
  --stagingLocation=gs://YOUR-BUCKET/dataflow-staging \
  --numWorkers=#
