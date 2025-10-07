
"""Entrypoint for `python -m app`."""

from app.calculator.cli import CalculatorCLI


def main():
    cli = CalculatorCLI()
    print("Welcome to the Calculator REPL. Type 'help' for instructions.")
    try:
        while True:
            try:
                line = input(cli.PROMPT)
            except EOFError:
                print()
                break
            try:
                cli.run_once(line)
            except SystemExit:
                break
    except KeyboardInterrupt:
        print("\nInterrupted.")
    print("Goodbye.")


if __name__ == "__main__":
    main()  # pragma: no cover
