import sys, os
from .mocking import unittest, TestSphinxtrap
from .builder import BuildProject

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestSphinxtrap))
    suite.addTests(unittest.makeSuite(BuildProject))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=1).run(suite())
