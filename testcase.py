import unittest
from random_balls import random_balls

val = random_balls()
val2 = list(set(val))


class TestCase(unittest.TestCase):
    def test_easy1(self):
        self.assertEqual(len(val), len(val2))

    def test_easy2(self):
        self.assertEqual(len(val), 10)


if __name__ == '__main__':
    unittest.main()
