Calculate Coverage
===========

.. toctree::
   :maxdepth: 2

.. contents::

This pipeline calculates mean read depth coverage for a given dataset or set of read group sets
and writes the results to Annotations in a new AnnotationSet using the Genomics API.

For each "bucket" in the given input references, this computes the average coverage (rounded to
six decimal places) across the bucket that 10%, 20%, 30%, etc. of the input read group sets have
for each mapping quality of the reads (<10:Low(L), 10-29:Medium(M), >=30:High(H)) as well as
these same percentiles of read group sets for all reads regardless of mapping quality (Mapping
quality All(A)).

There is also the option to change the number of quantiles accordingly (numQuantiles = 5 would
give you the minimum read group set mean coverage for each and across all mapping qualities, the
25th, 50th, and 75th percentiles, and the maximum of these values).

The pipeline is implemented on `Google Cloud Dataflow`_.

Setup Dataflow
--------------

.. include:: ../../includes/dataflow_setup.rst

.. include:: ../../includes/dataflow_on_gce_setup.rst

Your project must be whitelisted to use gRPC in order to run this pipeline, as it makes use of 
gRPC streaming to retrieve data.  Contact us `here <google-genomics-contact@googlegroups.com>`_ if you are interested in being whitelisted to test this pipeline and other gRPC tools.

Create Output Dataset
---------------------

In order to run this pipeline, you must create a dataset using the Genomics API that the pipeline
can output its AnnotationSet and Annotations to.  If you already have a dataset in which you have
write access, you may use it.  If not, you can do the following to create one:

#. Go to `this link <https://developers.google.com/apis-explorer/#p/genomics/v1beta2/genomics.datasets.create>`_ in the Genomics API Explorer for creating datasets.
#. Put your Google Cloud Platform project number in the ``projectNumber`` field of the request body.
#. Decide whether or not to make your dataset public by selecting or deselecting the ``isPublic`` field.
#. Give your dataset a name in the ``name`` field.
#. Turn on authorizing requests in the upper right corner of the window.
#. Press Execute.

The ``id`` that is generated in the response output is the output dataset id you should use when running
the pipeline.

Download ALPN
-------------

Running this pipeline locally requires that you have the ALPN jar that matches your JRE version
on your computer.  See the `ALPN documentation <http://www.eclipse.org/jetty/documentation/9.2.10.v20150310/alpn-chapter.html>`_ for a table of which ALPN jar to use.

You will not need to provide the ALPN flag or jar if you run the pipeline on Google cloud instead of locally.

Run the pipeline
----------------

The following command will calculate the mean coverage as described above for a given genomic
region, using a bucket width of 1024 (in this case one bucket output) and the 1000 Genomes
dataset id:

.. code-block:: shell

  java -Xbootclasspath/p:PATH/TO/YOUR/alpn-boot-YOUR-ALPN-JAR-VERSION.jar \
    -cp /PATH/TO/google-genomics-dataflow*runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.CalculateCoverage \
    --project=YOUR-GOOGLE-CLOUD-PLATFORM-PROJECT-ID \
    --stagingLocation=gs://YOUR-BUCKET/dataflow-staging \
    --secretsFile=/PATH/TO/YOUR/client_secrets.json \
    --references=1:552960:553984 \
    --bucketWidth=1024 \
    --inputDatasetId=10473108253681171589 \
    --outputDatasetId=YOUR_OUTPUT_DATASET_ID

This can take several minutes to run.  You can check your results by using the Genomics API Explorer:

1. First go to the `AnnotationSets search request page <https://developers.google.com/apis-explorer/#p/genomics/v1beta2/genomics.annotationSets.search>`_ to determine what your newly created AnnotationSetId is.
  a. Put your output dataset id in the ``datasetIds`` field.
  b. Turn on authorizing requests in the upper right corner of the window.
  c. Press Execute.
2. Then go to the `Annotations search request page <https://developers.google.com/apis-explorer/#p/genomics/v1beta2/genomics.annotations.search>`_ to be able to see your newly created Annotation.
  a. Put the AnnotationSetId you just found in the ``annotationSetIds`` field.
  b. Select ``info`` and ``position`` in the fields editor.
  c. Turn on authorizing requests in the upper right corner of the window.
  d. Press Execute.
3. Your Annotation should look like this:

.. code-block:: shell

  {
   "annotations": [
    {
     "position": {
      "referenceId": "EIaSo62VtfXT4AE",
      "referenceName": "1",
      "start": "552960",
      "end": "553984"
     },
     "info": {
      "A": [
       "0.458984",
       "2.77832",
       "3.584961",
       "4.275391",
       "4.881836",
       "5.521484",
       "6.251953",
       "7.06543",
       "8.048828",
       "9.681641",
       "41.395508"
      ],
      "L": [
       "0.296875",
       "1.942383",
       "2.462891",
       "2.939453",
       "3.357422",
       "3.787109",
       "4.266602",
       "4.806641",
       "5.514648",
       "6.586914",
       "27.857422"
      ],
      "M": [
       "0.006836",
       "0.4375",
       "0.764648",
       "1.042969",
       "1.31543",
       "1.59082",
       "1.948242",
       "2.299805",
       "2.836914",
       "3.655273",
       "15.15625"
      ],
      "H": [
       "0.041016",
       "0.175781",
       "0.194336",
       "0.195313",
       "0.195313",
       "0.197266",
       "0.351563",
       "0.390625",
       "0.421875",
       "0.588867",
       "2.931641"
      ]
     }
    }
   ]
  }

The following command will also calculate the mean coverage in the same manner as the previous
command, but will use a select number of read group sets from 1000 Genomes instead of the entire
dataset.  To do this, we must change the number of quantiles we are computing, as we now have
fewer read group sets then the default requirement of 11:

.. code-block:: shell

  java -Xbootclasspath/p:PATH/TO/YOUR/alpn-boot-YOUR-ALPN-JAR-VERSION.jar \
    -cp /PATH/TO/google-genomics-dataflow*runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.CalculateCoverage \
    --project=YOUR-GOOGLE-CLOUD-PLATFORM-PROJECT-ID \
    --stagingLocation=gs://YOUR-BUCKET/dataflow-staging \
    --secretsFile=/PATH/TO/YOUR/client_secrets.json \
    --references=1:552960:553984 \
    --bucketWidth=1024 \
    --numQuantiles=3 \
    --readGroupSetIds=CMvnhpKTFhDq9e2Yy9G-Bg,CMvnhpKTFhCEmf_d_o_JCQ,CMvnhpKTFhCjz9_25e_lCw \
    --outputDatasetId=YOUR_OUTPUT_DATASET_ID

This command should run much faster then the above command.  You can check your results the same way as
described above, except now your Annotation should look like this:

.. code-block:: shell

  {
   "annotations": [
    {
     "position": {
      "referenceId": "EIaSo62VtfXT4AE",
      "referenceName": "1",
      "start": "552960",
      "end": "553984"
     },
     "info": {
      "A": [
       "4.135742",
       "4.661133",
       "9.693359"
      ],
      "L": [
       "1.631836",
       "4.075195",
       "7.200195"
      ],
      "M": [
       "0.585938",
       "2.327148",
       "2.493164"
      ],
      "H": [
       "0.176758",
       "0.176758",
       "0.176758"
      ]
     }
    }
   ]
  }

The above command lines run the pipeline over a small portion of the genome, only taking a few minutes.
If modified to run over a larger portion of the genome or the entire genome, it may take a few hours
depending upon how many machines are configured to run concurrently via ``--numWorkers``.

To run this pipeline over a large portion of the genome:

* Add ``--runner=DataflowPipelineRunner`` and remove the ALPN jar from the command line to run the pipeline on Google Cloud instead of locally.
* Add ``--numWorkers=#`` for faster processing that will shard the data.
* Add more references:

  #. Use a comma-separated list to run over multiple disjoint regions.  For example to run over `BRCA1`_ and `BRCA2`_ ``--references=13:32889610:32973808,17:41196311:41277499``
  #. Use ``--allReferences`` instead of ``--references=1:552960:557056`` to run over the entire genome.

To run the pipeline on a different dataset, change the ``--inputDatasetId`` parameter.

To run the pipeline on a different group of read group sets, change the ``--readGroupSetIds`` parameter.

To run the pipeline with a different bucket width, change the ``--bucketWidth`` parameter.

To run the pipeline with a different number of output quantiles, change the ``--numQuantiles`` parameter.


Additional details
------------------

.. include:: ../../includes/dataflow_details.rst
