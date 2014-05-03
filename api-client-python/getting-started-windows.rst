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

  *Note:* For this instance we will assume the installation directory to be ``C:\Google\google_appengine_python``
  
* Once installed proceed to the 


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

