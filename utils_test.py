import unittest
from utils import Utils

class TestUtils(unittest.TestCase):

    def test_reversed(self):
        # Test with integer
        self.assertEqual(Utils.reversed(123), 321)

        # Test with float, which should raise a TypeError
        with self.assertRaises(TypeError):
            Utils.reversed(123.45)
        
        # Test with string, which should raise a ValueError
        with self.assertRaises(ValueError):
            Utils.reversed("abc")

    def test_formatter(self):
        # Test with integer
        self.assertEqual(Utils.formatter(10), ('0b1010', '0o12'))
        
        # Test with float, which should raise a TypeError
        with self.assertRaises(TypeError):
            Utils.formatter(10.5)

        # Test with string, which should raise a TypeError
        with self.assertRaises(TypeError):
            Utils.formatter("abc")

if __name__ == "__main__":
    unittest.main()