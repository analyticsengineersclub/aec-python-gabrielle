import unittest 
from calc import aec_divide 


class TestDivision(unittest.TestCase):
    def test_division(self):
        arg_ints = [20, 5]
        division_results = aec_divide(arg_ints)
        self.assertEqual(division_results, 4)
    
    def test_division_by_0(self):
        arg_ints = [20, 0]
        division_results = aec_divide(arg_ints)
        self.assertEqual(division_results, 0)    

if __name__ == '__main__':
    unittest.main()