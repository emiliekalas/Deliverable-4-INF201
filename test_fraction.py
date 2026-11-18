import pytest
from fraction import Fraction


def test_init_values():
    f = Fraction(3, 4)
    assert f.numerator == 3
    assert f.denominator == 4


def test_init_type_error():
    with pytest.raises(TypeError):
        Fraction(1.5, 2)


def test_str():
    assert str(Fraction(1, 2)) == "1/2"


def test_equal_fractions():
    assert Fraction(1, 2) == Fraction(2, 4)


def test_lt():
    assert Fraction(1, 2) < Fraction(2, 3)

def test_denominator():
    with pytest.raises(ValueError):
        Fraction(1, 0)  

def test_repr():
    f = Fraction(3, 4)
    assert repr(f) == "Fraction(3, 4)"

def test_float():  
    f = Fraction(1, 2)
    assert float(f) == 0.5

def test_neg():
    f = Fraction(1, 2)
    neg_f = -f
    assert neg_f.numerator == -1
    assert neg_f.denominator == 2

def test_abs():
    f = Fraction(-1, 2)
    abs_f = abs(f)
    assert abs_f.numerator == 1
    assert abs_f.denominator == 2

def test_comparison_with_non_fraction():
    a = Fraction(1, 2)
    b = Fraction(2, 3)
    assert a != b
    assert a < b
    assert a <= b
    assert b > a
    assert b >= a

def test_precision():
    assert Fraction(10**17 + 1, 10**17) != Fraction(1, 1)


def test_not_implemented_comparison():
    a = Fraction(1, 2)
    assert a.__eq__(1) is NotImplemented
    assert a.__ne__(1) is NotImplemented
    assert a.__lt__(1) is NotImplemented
    assert a.__le__(1) is NotImplemented
    assert a.__gt__(1) is NotImplemented
    assert a.__ge__(1) is NotImplemented

