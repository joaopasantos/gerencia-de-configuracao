import unittest

from routes import *

class Tests(unittest.TestCase):
        def test_index(self):
                self.assertEqual(index(), "Flask!")
        
        def test_hello(self):
                self.assertEqual(hello(), "Hello!")

        def test_hello_with_name(self):
                self.assertEqual(helloName("Pedro"), "Hello, Pedro!")

if __name__ == '__main__':
        unittest.main()