.. code::

  # Install BiocInstaller.
  source("http://bioconductor.org/biocLite.R")
  # See http://www.bioconductor.org/developers/how-to/useDevel/
  useDevel()
  # Install devtools which is needed for the special use of biocLite() below.
  biocLite("devtools")
  # Install the workshop material.
  biocLite("googlegenomics/bioconductor-workshop-r", build_vignettes=TRUE, dependencies=TRUE)
