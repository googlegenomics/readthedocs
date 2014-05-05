Setting up the python client on Windows
---------------------------------------

* In order to setup Python 2.7 for Windows, first download it from 
  https://www.python.org/downloads/

* After installing Python, add to your ``PATH`` the location of the Python 
  directory and the Scripts directory within it. 

  For example, if Python is installed in ``C:\Python27``, 
  proceed by right-clicking on My Computer on the Start Menu and select "Properties". 
  Select "Advanced system settings" and then click on the "Environment Variables" button. 
  In the window that comes up, append the following to the system variable ``PATH`` 
  (if you chose a different installation location, change this path accordingly)::

  ;C:\Python27\;C:\Python27\Scripts\


Running the client with App Engine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Only follow the instructions in this section if you want to run the python client with App Engine.

* Download the "Google App Engine SDK for Python" for Windows from 
  https://developers.google.com/appengine/downloads and install it.

* Open up the ``main.py`` file inside of your ``api-client-python`` directory and set the following value to True::

    USE_APPENGINE = True
  
* From within the ``api-client-python`` directory, you then need to run the dev_appserver.py script. 
  If we assume the installation directory for your app engine SDK was ``C:\Google\google_appengine``, 
  then you would run the following command::
  
    python C:\Google\google_appengine\dev_appserver.py .

  If you get an error like ``google.appengine.tools.devappserver2.wsgi_server.BindError: Unable to bind localhost:8000``, 
  try specifying a specific port with this command::
  
    python C:\Google\google_appengine\dev_appserver.py --admin_port=12000 .
 
* To view your running server, open your browser to ``localhost:8080``.

Enabling OAuth
..............

If you want to support OAuth requests (used by the Google API provider), 
you will need to be running your server with App Engine. 

* First, follow the `authentication instructions 
  <https://developers.google.com/genomics#authenticate>`_ to generate a valid
  ``client_secrets.json`` file. However, for this application you want to generate
  secrets for a *Web Application* rather than a *Native Application*.

* Be sure to add ``http://localhost:8080/oauth2callback`` as an ``Authorized redirect URI`` 
  when configuring the client ID.

* Replace the ``client_secrets.json`` file in the api-client-python directory 
  with your newly downloaded file. 

* Then, enable OAuth in the code by editing ``main.py`` again to set the 
  following value to True::

    REQUIRE_OAUTH = True
  
* Run your App Engine server as before, and view your server at ``localhost:8080``.

* You should then be prompted to grant OAuth access to your local server, 
  and Google will show up in the Readset choosing dialog.

* If you see an ``Error: redirect_uri_mismatch`` message when trying to grant OAuth access to 
  your local server that means you need to `update the Authorized redirect URIs <http://stackoverflow.com/questions/20732266/authenticate-with-google-oauth-2-0-did-not-match-a-registered-redirect-uri>`_ 
  for your Client ID.

Running the client without App Engine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Only follow the instructions in this section if you do *not* want to use App Engine. 
See the section above for App Engine instructions.

* First you will need to download Pip from https://raw.github.com/pypa/pip/master/contrib/get-pip.py
  
* To install Pip, open up a cmd.exe window by selecting Start->Run->cmd and type the following
  (*replace directory_of_get-pip.py with the location of where get-pip.py resides*)::

    cd directory_of_get-pip.py
    python get-pip.py

* Afterwards in the same command window, type the following command to update 
  your Python environment with the required modules::

    pip install WebOb Paste webapp2 jinja2
  
* You should then be able to run the localserver with the following commands::
  
    cd api-client-python
    python localserver.py

