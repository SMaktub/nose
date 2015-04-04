import unittest

class MyTestCase(unittest.TestCase):
    @unittest.skip("skipping this one")
    def test_foo(self):
        pass
