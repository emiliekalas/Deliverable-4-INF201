class Fraction:
    def __init__(self, numerator: int, denominator: int = 1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")
        if denominator <= 0:
            raise ValueError("Denominator must be strictly positive")

        self.numerator = numerator
        self.denominator = denominator

   
    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    
    def __float__(self):
        return self.numerator / self.denominator

    
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __abs__(self):
        return Fraction(abs(self.numerator), self.denominator)

 
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator != other.numerator * self.denominator

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator >= other.numerator * self.denominator
