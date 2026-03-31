"""CLI entrypoint for sympy-integrator."""

import argparse

from .core import integrate_expression


def main() -> None:
    parser = argparse.ArgumentParser(description="Integrate an expression with SymPy.")
    parser.add_argument("expression", help='Expression like "sin(x)"')
    parser.add_argument("--var", default="x", help="Variable name to integrate by (default: x)")
    args = parser.parse_args()

    result = integrate_expression(args.expression, args.var)
    print(result)


if __name__ == "__main__":
    main()
