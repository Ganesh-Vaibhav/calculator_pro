
import pytest
from app.operation.operations import Add, Sub, Mul, Div

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (2.5, 1.5, 4.0)
])
def test_add(a, b, expected):
    op = Add()
    assert op.execute(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 5, -5),
    (-2, -3, 1)
])
def test_sub(a, b, expected):
    assert Sub().execute(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (0, 5, 0),
    (-1, 4, -4)
])
def test_mul(a, b, expected):
    assert Mul().execute(a, b) == pytest.approx(expected)

def test_div_normal():
    assert Div().execute(6, 3) == pytest.approx(2.0)

def test_div_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        Div().execute(1, 0)

