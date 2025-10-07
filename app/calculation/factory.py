"""Factory for creating calculation instances (wraps operations)."""

from app.operation.operations import Add, Sub, Mul, Div, Operation
from typing import Optional


class Calculation:
    def __init__(self, operation: Operation):
        self.operation = operation

    def execute(self, a: float, b: float) -> float:
        return self.operation.execute(a, b)


class CalculationFactory:
    """Creates Calculation instances by operation name."""

    _map = {
        "add": Add,
        "sub": Sub,
        "mul": Mul,
        "div": Div,
    }

    def create(self, name: str) -> Optional[Calculation]:
        cls = self._map.get(name)
        if cls is None:
            return None
        return Calculation(cls())
