
"""Operation implementations."""

from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass


class Add(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b


class Sub(Operation):
    def execute(self, a: float, b: float) -> float:
        return a - b


class Mul(Operation):
    def execute(self, a: float, b: float) -> float:
        return a * b


class Div(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b
