# -*- coding: utf-8 -*-
import os
import unittest
from nose.plugins.skip import Skip
from nose.plugins import PluginTester

support = os.path.join(os.path.dirname(__file__), 'support')

class TestSkipEnabled(PluginTester, unittest.TestCase):
    activate = ''
    args = ['-v']
    plugins = [Skip()]
    suitepath = os.path.join(support, 'issue889')

    def runTest(self):
        print str(self.output)
        assert 'SKIP=1' in self.output


class TestSkipDisabled(PluginTester, unittest.TestCase):
    activate = '--no-skip'
    args = ['-v']
    plugins = [Skip()]
    suitepath = os.path.join(support, 'issue889')

    def runTest(self):
        print str(self.output)
        assert 'SKIP=1' in self.output
