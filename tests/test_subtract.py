import unittest
from calc import aec_subtract


class TestSubstract(unittest.TestCase):
    def test_subtract(self):
        arg_ints = [20, 5]
        sub_results = aec_subtract(arg_ints)
        self.assertEqual(sub_results, 15)


if __name__ == "__main__":
    unittest.main()
