# tests/test_add.py
import unittest

from operations.sum import sum


class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(sum(3, 4), 7)


if __name__ == '__main__':
    unittest.main()
