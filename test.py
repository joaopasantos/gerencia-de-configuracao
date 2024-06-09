import unittest

from routes import *

class Tests(unittest.TestCase):
        def test_index(self):
                self.assertEqual(index(), "Flask!")

if __name__ == '__main__':
        unittest.main()