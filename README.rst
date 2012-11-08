Sphinxtrap
----------

    | "Yet another bootstrapped sphinx theme."

Sphinxtrap is a minimalist bootstrap-based `sphinx <http://sphinx-doc.org/>`_ theme,
You can see an example `here <http://jfardello.github.com/Dardrive/>`_.

Install
-------

    easy_install sphinxtrap

Usage:
------
Add to sphinx's conf.py::

    import sphinxtrap as st

    html_theme = 'sphinxtrap'
    html_theme_path = [st.get_theme_dir()]
    #html_theme_options = {'analytics':"YOUR-ANALITICS-CODE "} #this is optional!
    #html_logo = None #will fallback to the folder icon
    #If you customize the logo, make sure it is a 32x32 image.
