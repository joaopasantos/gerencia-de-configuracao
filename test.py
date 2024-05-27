import unittest

from routes import hello

class Tests(unittest.TestCase):
        def test_func(self):
                self.assertEqual(hello(), "Flask?")

if __name__ == '__main__':
        unittest.main()