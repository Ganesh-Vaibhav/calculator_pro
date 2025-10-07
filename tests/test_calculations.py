
import pytest
from app.calculation.factory import CalculationFactory, Calculation
from app.calculator.cli import CalculatorCLI

@pytest.mark.parametrize("name,expected_type", [
    ("add", "Calculation"),
    ("sub", "Calculation"),
    ("mul", "Calculation"),
    ("div", "Calculation"),
])
def test_factory_creates(name, expected_type):
    factory = CalculationFactory()
    calc = factory.create(name)
    assert isinstance(calc, Calculation)
    # ensure execute returns a float
    res = calc.execute(2, 1)
    assert isinstance(res, float) or isinstance(res, int)

def test_factory_returns_none_for_unknown():
    factory = CalculationFactory()
    assert factory.create("unknown") is None

def test_cli_parse_and_history(tmp_path, capsys):
    cli = CalculatorCLI()
    # help command
    cli.run_once("help")
    # simple add
    cli.run_once("add 3 4")
    captured = capsys.readouterr()
    assert "7.0" in captured.out
    # history shows the record
    cli.run_once("history")
    captured = capsys.readouterr()
    assert "add 3 4 = 7" in captured.out

def test_cli_bad_input(capsys):
    cli = CalculatorCLI()
    # wrong arg count
    cli.run_once("add 5")
    captured = capsys.readouterr()
    assert "Input error" in captured.out
    # non-numeric
    cli.run_once("mul five two")
    captured = capsys.readouterr()
    assert "Input error" in captured.out

def test_cli_div_by_zero(capsys):
    cli = CalculatorCLI()
    cli.run_once("div 1 0")
    captured = capsys.readouterr()
    assert "Error: division by zero" in captured.out
