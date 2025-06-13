import pycalc.calculator as calc


def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0


def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 4) == -4
    assert calc.subtract(-3, -3) == 0
