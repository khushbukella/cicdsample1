import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add_integers(self):
        result = calc.add2(1, 2)
        self.assertEqual(result, 3)
    
    def test_sub_integers(self):
        result = calc.sub2(5, 2)
        self.assertEqual(result, 3)

    def test_prod_integers(self):
        result = calc.pro2(1, 2)
        self.assertEqual(result, 2)
    

    

if __name__ == '__main__':
    unittest.main()
