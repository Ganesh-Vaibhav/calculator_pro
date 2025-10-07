Professional Command-Line Calculator (Python)
A modular, well-tested command-line calculator implementing a REPL with arithmetic operations, robust error handling (LBYL & EAFP), calculation history, and a factory-based design. Includes tests (pytest) and a GitHub Actions CI workflow that enforces 100% coverage.
Project layout
.
├── .github/
│   └── workflows/
│       └── python-app.yml
├── app/
│   ├── __main__.py
│   ├── calculator/
│   │   ├── __init__.py
│   │   └── cli.py
│   ├── calculation/
│   │   ├── __init__.py
│   │   └── factory.py
│   └── operation/
│       ├── __init__.py
│       └── operations.py
├── tests/
│   ├── test_operations.py
│   └── test_calculations.py
├── pyproject.toml   # or requirements.txt
└── README.md
Quick setup (local)
Clone repo and create virtualenv:
git clone <repo-url>
cd repo
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows (PowerShell)
pip install -U pip
pip install -r requirements.txt
If using pyproject.toml/poetry or pipenv, adapt accordingly.
Run the REPL:
python -m app
Run tests and coverage locally:
pytest --cov=app tests/
coverage report --fail-under=100
Features
REPL interface with help, history, and exit commands.
Arithmetic operations: add, sub, mul, div.
Input validation and clear user prompts.
Demonstrates both LBYL and EAFP error-handling patterns.
CalculationFactory to create calculation instances.
History of calculations within session.
Comprehensive unit tests with parametrization.
CI: GitHub Actions to run tests and enforce 100% coverage.
Usage (REPL examples)
> help
> add 3 4
7.0
> mul 2 5
10.0
> div 5 0
Error: division by zero
> history
1: add 3 4 = 7.0
2: mul 2 5 = 10.0
> exit