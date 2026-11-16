# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle
import math

from geometry import Point, Circle

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)

    assert p1.distance_to(p2) == 5.0
    assert p2.distance_to(p1) == 5.0

def test_circle_constructor():
    c = Circle(5)

    assert c.radius == 5
    assert c.centre.x == 0
    assert c.centre.y == 0

    c2 = Circle(3, Point(2, 4))

    assert c2.radius == 3
    assert c2.centre.x == 2
    assert c2.centre.y == 4

def test_circle_area():
    c = Circle(5)

    assert math.isclose(c.area(), 25 * math.pi)

def test_circle_perimeter():
    c = Circle(5)

    assert math.isclose(c.perimeter(), 10 * math.pi)

    # complete the implementation for
    # testing distance_to()
    

# Write test functions to test the __init__(), 
# area() and perimeter() methods in Circle class
# you can use the default value for centre coordinates
