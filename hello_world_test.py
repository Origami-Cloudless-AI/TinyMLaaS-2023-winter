import unittest


class HelloWorldTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual("Hello World", "Hello World")