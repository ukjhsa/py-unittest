import unittest
import mock
from mock import patch

import target
import mb

class ExampleTest(unittest.TestCase):
    @mock.patch('target.ma.Lib', side_effect=mb.Lib)
    def test_testclass(self,mock):
        self.assertEqual(target.testclass(), 1)

    @mock.patch('target.testfunc', side_effect=mb.test)
    def test_testfunc(self, mock):
        self.assertEqual(target.testfunc(), 1)
        
unittest.main()
