
"""CLI for the calculator REPL."""

from app.calculation.factory import CalculationFactory
from typing import List


class CalculatorCLI:
    PROMPT = "> "

    def __init__(self):
        self.factory = CalculationFactory()
        self.history = []

    def print_help(self):
        help_text = """
Simple Calculator REPL
Commands:
  help                 Show this help message
  history              Show calculation history for this session
  exit                 Exit the REPL
Usage:
  <operation> <num1> <num2>
Operations:
  add, sub, mul, div
Example:
  add 5 3
"""
        print(help_text.strip())

    def parse_input(self, line: str):
        """Parse input line into (cmd, args)."""
        parts = line.strip().split()
        if not parts:
            return None, []
        cmd = parts[0].lower()
        args = parts[1:]
        return cmd, args

    def validate_numbers_lbyl(self, args: List[str]):
        """LBYL validation: check length and numeric format before running."""
        if len(args) != 2:
            raise ValueError("Expected two numeric arguments.")
        try:
            a = float(args[0])
            b = float(args[1])
        except ValueError:
            raise ValueError("Arguments must be numbers.")
        return a, b

    def run_once(self, line: str):
        cmd, args = self.parse_input(line)
        if cmd is None:
            return
        if cmd in ("exit", "quit"):
            raise SystemExit
        if cmd == "help":
            self.print_help()
            return
        if cmd == "history":
            if not self.history:
                print("No history yet.")
            else:
                for idx, entry in enumerate(self.history, start=1):
                    print(f"{idx}: {entry}")
            return

        # Command is an operation
        # Use factory to construct calculation and execute.
        # Use LBYL for argument count and numeric types, then EAFP for execution errors (like div by zero).
        try:
            a, b = self.validate_numbers_lbyl(args)
        except ValueError as exc:
            print(f"Input error: {exc}")
            return

        calculation = self.factory.create(cmd)
        if calculation is None:
            print(f"Unknown operation '{cmd}'. Type 'help'.")
            return

        # EAFP: try the operation and catch runtime exceptions
        try:
            result = calculation.execute(a, b)
        except Exception as exc:
            print(f"Error: {exc}")
            return

        record = f"{cmd} {a:g} {b:g} = {result}"
        self.history.append(record)
        print(result)

