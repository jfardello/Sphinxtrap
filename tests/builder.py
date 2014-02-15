import os
try:
    from StringIO  import StringIO
except ImportError:
    from io import StringIO
import tempfile
from shutil import rmtree

from sphinx import cmdline

from . mocking import unittest, mock


global cache 
cache = {'tmp_file':'/tmp/__sphinxtrap__',
        'index_html': None} 


class BuildProject(unittest.TestCase):

    index_html = None

    def test_1_build(self):
        cache['old_pwd'] = os.getcwd() 
        path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(os.path.join(path, "testprj"))
        cache['tmp_file'] = tempfile.mkdtemp()

        args = ['sphinx-build', '-b', 'html', '-d', 
                cache['tmp_file'] + '/doctrees', 'source', 
                cache['tmp_file'] + '/build/html']
        with mock.patch('sys.stdout', new=StringIO()) as fake_out: 
            retv = cmdline.main(args)
        self.assertEqual(retv, 0)

    def read(self):
        if cache['index_html'] is None:
            fname = cache['tmp_file'] + '/build/html/index.html'
            with open(fname, 'rt') as fd:
                cache['index_html'] = fd.read()
        return cache['index_html']


    def test_2_icon_role(self):
        btn = '<p><em class="icon-bullhorn icon-holder"></em></p>'
        self.assertIn(btn, self.read())

    def test_2_btn_role(self):
        btn = '<a class="btn reference external" ''href="http://sphinx-doc.or'
        'g/"><em class="icon-globe icon-holder"></em> Sphinx </a>'
        self.assertIn(btn, self.read())

    def test_3_tear_down(self):
        rmtree(cache['tmp_file'])
        os.chdir(cache['old_pwd'])


