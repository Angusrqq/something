import pytest
from glib.shapes import Circle, Triangle
from glib.utils import get_area
from math import isclose, pi, sqrt

def test_circle_area():
    c = Circle(1)
    assert isclose(c.area(), pi)

def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(0)
    with pytest.raises(ValueError):
        Circle(-1)

def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert isclose(t.area(), 6.0)
    
def test_triangle_invalid_sides():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)
    with pytest.raises(ValueError):
        Triangle(-1, 2, 3)
    with pytest.raises(ValueError):
        Triangle(1, -2, 3)
    with pytest.raises(ValueError):
        Triangle(1, 2, -3)

def test_triangle_right():
    t = Triangle(3, 4, 5)
    assert t.is_right()

def test_get_area():
    shapes = [Circle(2), Triangle(3, 4, 5)]
    areas = [get_area(shape) for shape in shapes]
    assert isclose(areas[0], 4*pi), isclose(areas[1], 6.0)