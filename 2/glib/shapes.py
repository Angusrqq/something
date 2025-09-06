from abc import ABC, abstractmethod
from math import pi, sqrt, isclose

class Base(ABC):
    
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Base):
    def __init__(self, radius: float):
        if radius <= 0: raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2

class Triangle(Base):
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def is_right(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
    
