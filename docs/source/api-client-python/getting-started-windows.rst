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
Setting up the Python client on Windows
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

* Get the api-client-python code onto your machine by cloning the repository::

    git clone https://github.com/googlegenomics/api-client-python.git


Running the client with App Engine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Only follow the instructions in this section if you want to run the Python client with App Engine.

* Download the "Google App Engine SDK for Python" for Windows from
  https://cloud.google.com/appengine/downloads and install it.

* From within the ``api-client-python`` directory that you clones, run the dev_appserver.py script.
  If we assume the installation directory for your app engine SDK was ``C:\Google\google_appengine``,
  then you would run the following command::

    python C:\Google\google_appengine\dev_appserver.py .

  If you get an error like ``google.appengine.tools.devappserver2.wsgi_server.BindError: Unable to bind localhost:8000``,
  try specifying a specific port with this command::

    python C:\Google\google_appengine\dev_appserver.py --admin_port=12000 .

* To view your running server, open your browser to ``localhost:8080``.


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


Enabling the Google API provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to pull in data from Google Genomics API you will need to set
``API_KEY`` in ``main.py`` to a valid Google API key.

* First apply for access to the Genomics API by following the instructions at
  https://cloud.google.com/genomics/

* Then create a project in the
  `Google Cloud Platform Console`_
  or select an existing one.

* On the **APIs & auth** tab, select APIs and turn the Genomics API to ON

* On the **Credentials** tab, click **create new key** under
  the Public API access section.

* Select **Server key** in the dialog that pops up, and then click **Create**.
  (You don't need to enter anything in the text box)

* Copy the **API key** field value that now appears in the Public API access
  section into the top of the ``main.py`` file inside of your api-client-python directory.
  It should look something like this::

    API_KEY = "abcdef12345abcdef"


  Note: You can also reuse an existing API key if you have one.
  Just make sure the Genomics API is turned on.

* Run your server as before, and view your server at ``localhost:8080``.

* Google should now show up as an option in the Readset choosing dialog.
