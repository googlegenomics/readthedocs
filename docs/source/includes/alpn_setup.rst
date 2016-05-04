If you want to run a small pipeline locally before running it in parallel on the cloud, you will need `ALPN`_ since many of these pipelines require it.  When running locally, this must be provided on the boot classpath but when running on Google Cloud this is already configured for you. You can download the correct version from `here <http://mvnrepository.com/artifact/org.mortbay.jetty.alpn/alpn-boot>`__.  For example::

  wget -O alpn-boot.jar \
    http://central.maven.org/maven2/org/mortbay/jetty/alpn/alpn-boot/8.1.8.v20160420/alpn-boot-8.1.8.v20160420.jar

