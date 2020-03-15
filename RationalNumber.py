#Helper function to matain rational numbers in reduced form [BR-3]
def computeGCD(x, y): 
   while(y): 
       x, y = y, x % y 
   return x 

class Rational:
    def __init__(self,numerator=0,denomirator=1):
        if denomirator==0:
            raise ZeroDivisionError("IllegalArgumentException")
        factor = computeGCD(numerator,denomirator)
        self.numerator = numerator//factor
        self.denomirator = denomirator//factor
    def __str__(self):
        if (self.denomirator==1):
            return str(self.numerator)
        else:
            return str(self.numerator) + "/" + str(self.denomirator)
    def getDenominator(self):
        return self.denomirator
    def getNumerator(self):
        return self.numerator
    def __add__(self, other):
        return Rational(self.numerator*other.denomirator + other.numerator*self.denomirator, self.denomirator * other.denomirator)
    def __sub__(self,other):
        return Rational(self.numerator*other.denomirator - other.numerator*self.denomirator, self.denomirator * other.denomirator)
    def __mul__(self,other):
        return Rational(self.numerator * other.numerator, self.denomirator * other.denomirator)
    #dividing a fraction by another is the same as multiplying it by it's inverse
    def __div__(self,other):
        #y = inverse other
        y = Rational(other.denomirator,other.numerator)
        return self*y
    def __eq__(self, other):
        return (self.numerator == other.numerator and self.denomirator == other.denomirator)
    def __ne__(self,other):
        return  not self==other
    
#Testing
# x = Rational(3,-5)
# y = Rational(3,6)
# print(x)#Should print -3/5
# print(y)#Should print 3/6
# print(x+y)#Should print -1/10
# print(x-y)#Should print -11/10
# print(x*y)#Should print -3/10
# print(x/y)#Should print -6/5
