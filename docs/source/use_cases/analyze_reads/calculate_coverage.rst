+--------------------------------------------------------------------------------------------------------------+
| Note: Google Genomics is now Cloud Life Sciences.                                                            |       
| The Google Genomics Cookbook on Read the Docs is not actively                                                |
| maintained and may contain incorrect or outdated information.                                                |
| The cookbook is only available for historical reference. For                                                 |
| the most up to date documentation, view the official Cloud                                                   |
| Life Sciences documentation at https://cloud.google.com/life-sciences.                                       |
|                                                                                                              |
| Also note that much of the Genomics v1 API surface has been                                                  |
| superseded by `Variant Transforms <https://cloud.google.com/life-sciences/docs/how-tos/variant-transforms>`_ |
| and `htsget <https://cloud.google.com/life-sciences/docs/how-tos/reading-data-htsget>`_.                     |
+--------------------------------------------------------------------------------------------------------------+
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

Create Output Dataset
---------------------

In order to run this pipeline, you must have a Google Genomics dataset to which the pipeline
can output its AnnotationSet and Annotations.

* If you already have a dataset in which you have write access, you may use it.  Click here to see your datasets: https://console.cloud.google.com/project/_/genomics/datasets
* If not, you can click on the following link to use the Cloud Platform Console to create one: https://console.cloud.google.com/project/_/genomics/datasets/create.

In either case, the ``ID`` of the dataset is the output dataset id you should use when running
the pipeline.

Run the pipeline
----------------

The following command will calculate the mean coverage as described above for a given genomic
region, using a bucket width of 1024 (in this case one bucket output) on the :doc:`/use_cases/discover_public_data/platinum_genomes` dataset:

.. code-block:: shell

  java -Xbootclasspath/p:alpn-boot.jar \
    -cp google-genomics-dataflow-runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.CalculateCoverage \
    --references=chr1:552960:553984 \
    --bucketWidth=1024 \
    --inputDatasetId=3049512673186936334 \
    --outputDatasetId=YOUR-OUTPUT-DATASET-ID

This can take several minutes to run.  You can check your results by using the Genomics API Explorer:

1. First go to the `AnnotationSets search request page <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.annotationsets.search>`_ to determine what your newly created AnnotationSetId is.

  a. Put your output dataset id in the ``datasetIds`` field.
  b. Press the `Authorize and Execute` button.

2. Then go to the `Annotations search request page <https://developers.google.com/apis-explorer/#p/genomics/v1/genomics.annotations.search>`_ to be able to see your newly created Annotation.

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

  java -Xbootclasspath/p:alpn-boot.jar \
    -cp google-genomics-dataflow-runnable.jar \
    com.google.cloud.genomics.dataflow.pipelines.CalculateCoverage \
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

.. include:: /includes/dataflow_on_gce_run.rst

|dataflowSomeRefs|

|dataflowAllRefs|

To run the pipeline on a different dataset, change the ``--inputDatasetId`` parameter.

To run the pipeline on a different group of read group sets, change the ``--readGroupSetIds`` parameter.

To run the pipeline with a different bucket width, change the ``--bucketWidth`` parameter.

To run the pipeline with a different number of output quantiles, change the ``--numQuantiles`` parameter.

Additional details
------------------

.. include:: /includes/dataflow_details.rst
