Sphinxtrap
----------

    | "Yet another bootstrapped sphinx theme."

Sphinxtrap is a minimalist bootstrap2-based + fontawesome `sphinx <http://sphinx-doc.org/>`_ theme,
You can see an example `here <http://jfardello.github.io/Sphinxtrap>`_.


Install
-------

    ``pip install sphinxtrap``

Usage:
------

Configuration
.............

In in the project's ``conf.py`` add sphinxtrap.ext.rawtoc to extensions, set
the html_theme to "sphinxtrap", and html_theme_path to
[sphinxtrap.get_theme_dir()] like this:

.. code-block:: python

    import sphinxtrap 
    extensions = ["sphinxtrap.ext.rawtoc"]
    html_theme = 'sphinxtrap'
    html_theme_path = [sphinxtrap.get_theme_dir()]

FontAwesome icons
.................

You can add Font Awesome icons by using the icon role:

.. code-block:: rst

    :icon:`rocket,2x,pull-right`

Produces an ``<em>`` tag that will be changed into a ``<i>`` on a javascript
onload event:


.. code-block:: html

    <i class="icon-rocket icon-2x icon-pull-right"></i>

Bootstrap buttons:
..................
You can add bootstrap buttons via the btn role, ex:
.. code-block:: rst

    :btn:`Sphinx <https://http://sphinx-doc.org/>,btn-success,icon-globe`
    
The format is, "link <url>,html-class,html-class". 

Note that as opposed to the ``:icon:`` role, the ``:btn:`` role needs the "icon-" part to use FA icons.


Optional settings in the html_theme_options dict are:
.....................................................

analytics:
    Adds `GA code <https://developers.google.com/analytics/devguides/collection/gajs/methods/>`_  if it is present (or not None)
inverse:
    Adds the nabvar-inverse bootstrap class to the navbar.
new_page_external_links:
    Defaults to true, makes the theme to open external links in a new window.
css_files:
    A list with custom css styles, that will be loaded from the static_path defined
    in ``conf.py``

.. note::

    If you customize the logo make sure it is a 32x32 image. 

.. code-block:: python

    html_theme_options = {'analytics':"YOUR-ANALITICS-CODE", 'inverse': False} 
    html_logo = None #will fallback to the folder icon
    new_page_external_links = true 
