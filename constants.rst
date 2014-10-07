Important constants
-------------------

There are currently four providers of the API:

=============== =========================================== ==================================================
API Providers   Base url                                    Documentation
=============== =========================================== ==================================================
Google          https://www.googleapis.com/genomics/v1beta  http://developers.google.com/genomics
NCBI            http://trace.ncbi.nlm.nih.gov/Traces/gg     http://trace.ncbi.nlm.nih.gov/Traces/gg/index.html
EBI             http://193.62.52.16
Local readstore See the `README file`_
=============== =========================================== ==================================================

Each one has certain `datasets <https://developers.google.com/genomics/v1beta/reference/datasets>`_ 
exposed to the public. It will eventually be possible to list all available datasets from the API directly. 
For now, there are some common public values that can be used (in addition to private datasets):

==================== =================== ============
Public Dataset IDs   Name                API Provider
==================== =================== ============
10473108253681171589 1000 Genomes        Google
383928317087         PGP                 Google
461916304629         Simons Foundation   Google
337315832689         DREAM SMC Challenge Google
SRP034507            SRP034507           NCBI
SRP029392            SRP029392           NCBI
(Any NCBI Study)                         NCBI
data                 All data at EBI     EBI
==================== =================== ============

Within a dataset, the API has 
`a call <https://developers.google.com/genomics/v1beta/reference/readsets/search>`_ 
for getting all the readsets. The IDs that come back have different 
values based on the provider. They are always strings.

========================= ============ ===========================  
Example Readset IDs       API Provider Description
========================= ============ ===========================  
CMvnhpKTFhD04eLE-q2yxnU   Google       Google generated ID
SRR960599 or SRR960599.1  NCBI         NCBI Experiment Run or Read
10                        EBI          EBI generated ID
========================= ============ ===========================  

.. _README file: https://github.com/googlegenomics/api-provider-local-java
