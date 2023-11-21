import unittest
from operations.divide import divide


class TestDivision(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(divide(8, 4), 2)
        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == '__main__':
    unittest.main()
