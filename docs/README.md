docs
====

The documentation for all of the repositories in googlegenomics is hosted on readthedocs at http://googlegenomics.readthedocs.org.

The text on that site is automatically pushed from this repo's 
[reStructuredText](http://sphinx-doc.org/rest.html) files. See [this quick tutorial](http://rest-sphinx-memo.readthedocs.org/en/latest/ReST.html) or [Read The Doc's documentation](https://docs.readthedocs.org/en/latest/index.html) for more info.

Please help us improve these docs by [contributing](https://github.com/googlegenomics/docs/blob/master/CONTRIBUTING.rst)!

For documentation about the Google Genomics APIs themselves, see 
https://cloud.google.com/genomics/what-is-google-genomics and http://ga4gh.org

### Tips for local development

If you want to render and view documentation on your local machine using the same theme
as ReadTheDocs:

(1) [Install the Sphinx RTD Theme](https://github.com/snide/sphinx_rtd_theme).

(2) Locally modify conf.py.  Do not check this in.
```
diff --git a/docs/source/conf.py b/docs/source/conf.py
index c109c7f..61a0f27 100644
--- a/docs/source/conf.py
+++ b/docs/source/conf.py
@@ -98,13 +98,13 @@ pygments_style = 'sphinx'

 # The theme to use for HTML and HTML Help pages.  See the documentation for
 # a list of builtin themes.
-html_theme = 'default'
+#html_theme = 'default'

 #------------[ For Local Development ] -------------------------------------
 # See https://github.com/snide/sphinx_rtd_theme for theme install instructions.
-#import sphinx_rtd_theme
-#html_theme = "sphinx_rtd_theme"
-#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
+import sphinx_rtd_theme
+html_theme = "sphinx_rtd_theme"
+html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

 # Theme options are theme-specific and customize the look and feel of a theme
 # further.  For a list of options available for each theme, see the
```

(3) Build the docs.

```
cd start-here/docs/source
make html
```

(4) View the local files in your browser!
