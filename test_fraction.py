import pytest
from fraction import Fraction


def test_init_stores_values():
    f = Fraction(3, 4)
    assert f.numerator == 3
    assert f.denominator == 4


def test_init_non_integer_raises():
    with pytest.raises(TypeError):
        Fraction(1.5, 2)


def test_str():
    assert str(Fraction(1, 2)) == "1/2"


def test_eq_equivalent_fractions():
    assert Fraction(1, 2) == Fraction(2, 4)


def test_lt():
    assert Fraction(1, 2) < Fraction(2, 3)

    