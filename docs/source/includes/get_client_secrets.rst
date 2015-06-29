Get your ``client_secrets.json`` file by visiting the following page:

  https://console.developers.google.com/project/_/apiui/credential

#. Select your project.  If a "Client ID for native application" is listed on this page, skip to step 7.
#. Under the OAuth section, click "Create new Client ID".
#. Select "Installed Application".
#. If prompted, click "Configure consent screen" and follow the instructions to set a "product name" to identify your Cloud project in the consent screen.
#. In the Create Client ID dialog, be sure the following are selected:

   .. image:: /_static/create_client_id.png
      :alt: Create Client ID Dialog
      :align: right
      :height: 100px
      :width: 200px

   * **Application type**: Installed application
   * **Installed application type**: Other

#. Click the "Create Client ID" button.
#. You'll see your Client ID and Client secret listed under "Client ID for native application".
#. Under Client ID for native application, click "Download JSON".

Throughout this documentation we refer to this file as ``client_secrets.json`` even though upon download it has a much longer filename.  You might rename the file or add a symlink to it with the shorter name.
