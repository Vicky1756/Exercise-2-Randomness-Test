import unittest
from random_balls import random_balls

val = random_balls()
val2 = list(set(val))


class TestCase(unittest.TestCase):

    # check if returned element are sorted in ascending order
    def test_easy1(self):
        self.assertEqual(len(val), len(val2))

    # check if there are 10 returned element
    def test_easy2(self):
        self.assertEqual(len(val), 10)

    # check if every element is an integer
    def test_easy3(self):
        for n in val:
            self.assertEqual(n, int(n))
      # check if every element is within the range of 1  to 50 both inclusive

    def test_easy4(self):
        for n in val:
            self.assertTrue(1 <= n <= 50)


if __name__ == '__main__':
    unittest.main()
