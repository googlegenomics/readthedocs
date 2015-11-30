Calculate Coverage
==================

.. comment: begin: goto-read-the-docs

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/use_cases/analyze_reads/calculate_coverage.html

__ RenderedVersion_

.. comment: end: goto-read-the-docs

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

.. include:: /includes/collapsible_dataflow_setup_instructions.rst

Your project must be whitelisted to use gRPC in order to run this pipeline, as it makes use of
gRPC streaming to retrieve data.  `Contact us`_ if you are interested in being whitelisted to test this pipeline and other gRPC tools.

Create Output Dataset
---------------------

In order to run this pipeline, you must create a dataset using the Genomics API that the pipeline
can output its AnnotationSet and Annotations to.  If you already have a dataset in which you have
write access, you may use it.  If not, you can do the following to create one:

#. Go to `this link <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.datasets.create>`_ in the Genomics API Explorer for creating datasets.
#. Put your Google Cloud Platform project ID in the ``projectId`` field of the request body.
#. Give your dataset a name in the ``name`` field of the request body.
#. Press the `Authorize and Execute` button.

The ``id`` that is generated in the response output is the output dataset id you should use when running
the pipeline.

Download ALPN
-------------

Running this pipeline locally requires that you have the ALPN jar that matches your JRE version
on your computer.  See the `ALPN documentation <http://www.eclipse.org/jetty/documentation/9.2.10.v20150310/alpn-chapter.html>`_ for a table of which ALPN jar to use.

You will not need to provide the ALPN jar if you run the pipeline on Google Cloud instead of locally.

Run the pipeline
----------------

The following command will calculate the mean coverage as described above for a given genomic
region, using a bucket width of 1024 (in this case one bucket output) on the :doc:`/use_cases/discover_public_data/platinum_genomes` dataset:

.. code-block:: shell

  java -Xbootclasspath/p:PATH/TO/YOUR/alpn-boot-YOUR-ALPN-JAR-VERSION.jar \
    -cp /PATH/TO/google-genomics-dataflow*runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.CalculateCoverage \
    --secretsFile=/PATH/TO/YOUR/client_secrets.json \
    --references=chr1:552960:553984 \
    --bucketWidth=1024 \
    --inputDatasetId=3049512673186936334 \
    --outputDatasetId=YOUR-OUTPUT-DATASET-ID

This can take several minutes to run.  You can check your results by using the Genomics API Explorer:

1. First go to the `AnnotationSets search request page <https://developers.google.com/apis-explorer/#p/genomics/v1beta2/genomics.annotationSets.search>`_ to determine what your newly created AnnotationSetId is.

  a. Put your output dataset id in the ``datasetIds`` field.
  b. Press the `Authorize and Execute` button.

2. Then go to the `Annotations search request page <https://developers.google.com/apis-explorer/#p/genomics/v1beta2/genomics.annotations.search>`_ to be able to see your newly created Annotation.

  a. Put the AnnotationSetId you just found in the ``annotationSetIds`` field.
  b. Select ``info`` and ``position`` in the fields editor.
  c. Press the `Authorize and Execute` button.

3. Your Annotation should look like this:

.. code-block:: shell

 {
  "annotations": [
   {
    "position": {
     "referenceId": "CNfS6aHAoved2AEQy9ao_KOKwa43",
     "referenceName": "chr1",
     "start": "552960",
     "end": "553984"
    },
    "info": {
     "A": [
      "26.623047",
      "28.424805",
      "35.042969",
      "35.083984",
      "36.039063",
      "39.678711",
      "46.819336",
      "52.219727",
      "52.681641",
      "56.575195",
      "62.339844"
     ],
     "H": [
      "0.196289",
      "0.196289",
      "0.197266",
      "0.393555",
      "0.59082",
      "0.59082",
      "0.788086",
      "0.956055",
      "1.27832",
      "1.345703",
      "1.772461"
     ],
     "L": [
      "16.304688",
      "17.844727",
      "21.004883",
      "23.180664",
      "24.850586",
      "24.894531",
      "26.427734",
      "29.884766",
      "29.933594",
      "32.101563",
      "32.962891"
     ],
     "M": [
      "9.96875",
      "10.036133",
      "10.12207",
      "10.383789",
      "12.661133",
      "13.644531",
      "14.201172",
      "22.845703",
      "24.141602",
      "25.765625",
      "27.604492"
     ]
    }
   }
  ]
 }

The following command will also calculate the mean coverage in the same manner as the previous
command, but will use a select number of read group sets from the :doc:`/use_cases/discover_public_data/platinum_genomes` instead of the entire dataset, namely those for NA12883, NA12884, and NA12885.  To do this, we must change the number of quantiles we are computing, as we now have
fewer read group sets then the default requirement of 11:

.. code-block:: shell

  java -Xbootclasspath/p:PATH/TO/YOUR/alpn-boot-YOUR-ALPN-JAR-VERSION.jar \
    -cp /PATH/TO/google-genomics-dataflow*runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.CalculateCoverage \
    --secretsFile=/PATH/TO/YOUR/client_secrets.json \
    --references=chr1:552960:553984 \
    --bucketWidth=1024 \
    --numQuantiles=3 \
    --readGroupSetIds=CMvnhpKTFhCAv6TKo6Dglgg,CMvnhpKTFhDw8e3V6aCB-Q8,CMvnhpKTFhDo08GNkfe-jxo \
    --outputDatasetId=YOUR_OUTPUT_DATASET_ID

This command should run a bit faster then the above command.  You can check your results the same way as
described above, except now your Annotation should look like this:

.. code-block:: shell

 {
  "annotations": [
   {
    "position": {
     "referenceId": "CNfS6aHAoved2AEQy9ao_KOKwa43",
     "referenceName": "chr1",
     "start": "552960",
     "end": "553984"
    },
    "info": {
     "A": [
      "35.042969",
      "51.039063",
      "56.575195"
     ],
     "H": [
      "0.393555",
      "0.956055",
      "1.345703"
     ],
     "L": [
      "21.004883",
      "25.59375",
      "31.087891"
     ],
     "M": [
      "13.644531",
      "24.141602",
      "24.489258"
     ]
    }
   }
  ]
 }

The above command lines run the pipeline over a small portion of the genome, only taking a few minutes.
If modified to run over a larger portion of the genome or the entire genome, it may take a few hours
depending upon how many machines are configured to run concurrently via ``--numWorkers``.

To run this pipeline over a large portion of the genome:

* Add the following additional command line parameters to run the pipeline on Google Cloud instead of locally::

  --runner=DataflowPipelineRunner \
  --project=YOUR-GOOGLE-CLOUD-PLATFORM-PROJECT-ID \
  --stagingLocation=gs://YOUR-BUCKET/dataflow-staging

* Add ``--numWorkers=#`` for faster processing that will shard the data.
* Add more references:

  * Use a comma-separated list to run over multiple disjoint regions.  For example to run over `BRCA1`_ and `BRCA2`_ ``--references=13:32889610:32973808,17:41196311:41277499``
  * Or use ``--allReferences`` instead of ``--references=1:552960:557056`` to run over the entire genome.

To run the pipeline on a different dataset, change the ``--inputDatasetId`` parameter.

To run the pipeline on a different group of read group sets, change the ``--readGroupSetIds`` parameter.

To run the pipeline with a different bucket width, change the ``--bucketWidth`` parameter.

To run the pipeline with a different number of output quantiles, change the ``--numQuantiles`` parameter.


Additional details
------------------

.. include:: /includes/dataflow_details.rst
