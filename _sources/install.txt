Install
-------

.. code-block:: console

    pip install sphinxtrap


Configuration
-------------

In in the sphinx project's ``conf.py`` add ``sphinxtrap.ext.rawtoc`` to extensions, set
the html_theme to "sphinxtrap", and html_theme_path to [sphinxtrap.get_theme_dir()] 
like this:

.. code-block:: python

    import sphinxtrap 
    extensions = ["sphinxtrap.ext.rawtoc"]
    html_theme = 'sphinxtrap'
    html_theme_path = [sphinxtrap.get_theme_dir()]

.. _theme-options:

Optional settings 
.................

The following `html_theme_options <http://sphinx-doc.org/theming.html#using-a-theme>`_ keys in ``conf.py`` are allowed:

analytics:
    Adds `GA code <https://developers.google.com/analytics/devguides/collection/gajs/methods/>`_  if it is present (or not None)
blackbar:
    Adds the nabvar-inverse bootstrap class to the navbar.
new_page_external_links:
    Defaults to true, makes the theme to open external links in a new window.
css_files:
    A list with custom css styles, that will be loaded from the ``static_path`` defined in ``conf.py``.
globe_external_links:
    Appends a globe icon to the external links text.

.. note::

    If you customize the logo make sure it is a 32x32 image. 

.. code-block:: python

    html_theme_options = {'analytics':"YOUR-ANALITICS-CODE", 'inverse': False} 
    html_logo = None #will fallback to the folder icon
    new_page_external_links = true 



