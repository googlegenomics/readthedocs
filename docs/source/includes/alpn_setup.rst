If you want to run a small pipeline on your machine before running it in parallel on Compute Engine, you will need `ALPN`_ since many of these pipelines require it.  When running locally, this must be provided on the boot classpath but when running on Compute Engine Dataflow workers this is already configured for you. You can download it from `here <http://mvnrepository.com/artifact/org.mortbay.jetty.alpn/alpn-boot>`__.  For example::

  wget -O alpn-boot.jar \
    http://central.maven.org/maven2/org/mortbay/jetty/alpn/alpn-boot/8.1.8.v20160420/alpn-boot-8.1.8.v20160420.jar

