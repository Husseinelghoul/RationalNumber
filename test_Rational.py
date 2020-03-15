import unittest
from RationalNumber import Rational

class TestRationalMethods(unittest.TestCase):
    #Testing Equal
    def test_equal(self):
        bool1 = Rational(3,4)==Rational(3,4)
        bool2 = Rational(3,4)!=Rational(7,4)
        bool3 = Rational(3,4)==Rational(7,4)
        bool4 = Rational(3,4)!=Rational(3,4)
        self.assertEqual(bool1,True,"Error in equal")
        self.assertEqual(bool2,True,"Error in equal")
        self.assertEqual(bool3,False,"Error in equal")
        self.assertEqual(bool4,False,"Error in equal")

    #Testing Addition
    def test_add_pos(self):
        result = Rational(2,5)+Rational(2,5)
        self.assertEqual(result,Rational(4,5),"Error in Adding Positive Fractions")

    def test_add_neg(self):
        result = Rational(4,5)-Rational(3,5)
        self.assertEqual(result,Rational(1,5),"Error in Adding Negative Fractions")

    #Testing Substraction
    def test_sub_pos(self):
        result = Rational(4,5)-Rational(2,5)
        self.assertEqual(result,Rational(2,5),"Error in Substracting Positive Fractions")

    def test_sub_neg(self):
        result = Rational(2,5)-Rational(-2,5)
        self.assertEqual(result,Rational(4,5),"Error in Substracting Negative Fractions")

    #Testing Multiplication
    def test_mult_pos(self):
        result = Rational(2,5)*Rational(2,5)
        self.assertEqual(result,Rational(4,25),"Error multiplying Positive fractions")

    def test_mult_neg(self):
        result = Rational(2,5)*Rational(-2,5)
        self.assertEqual(result,Rational(-4,25),"Error in multiplying Negative fractions")

    #Testing Division
    def test_div_pos(self):
        result = Rational(2,3)/Rational(5,7)
        self.assertEqual(result,Rational(14,15),"Error in dividing Positive fractions")

    def test_div_neg(self):
        result = Rational(2,3)/Rational(-5,7)
        self.assertEqual(result,Rational(-14,15),"Error in dividing Negative fractions")

class TestRationalBRs(unittest.TestCase):
    # def test_BR1(self):
    #      x = Rational(5,0)
    #      self.assertRaises(ZeroDivisionError,0,"IllegalArgumentException")

    # def test_BR2(self):
    #      x = Rational(5,0)
    #      self.assertNotEqual(x.denomirator,0,"IllegalArgumentException")

    def test_BR3(self):
        x = Rational(3,6);
        y = Rational(1,2)
        self.assertEqual(x,y,"Error in B3")

    def test_BR4(self):
        x = Rational(-3,4)
        y = Rational(3,-4)
        self.assertEqual(x,y,"Error in BR4")
        

if __name__ == '__main__':
    unittest.main()