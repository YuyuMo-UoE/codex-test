"""Core symbolic integration logic."""

from __future__ import annotations

import re


def _integrate_without_sympy(expr: str, var: str) -> str:
    """Very small fallback integrator used when SymPy is unavailable.

    Supported forms (for quick demos):
    - sin(x) -> -cos(x)
    - cos(x) -> sin(x)
    - x -> x**2/2
    - integer constants like 3 -> 3*x
    """
    cleaned = expr.replace(" ", "")

    if cleaned == f"sin({var})":
        return f"-cos({var})"
    if cleaned == f"cos({var})":
        return f"sin({var})"
    if cleaned == var:
        return f"{var}**2/2"
    if re.fullmatch(r"[+-]?\d+", cleaned):
        return f"{cleaned}*{var}"

    raise ValueError(
        "SymPy is not installed and fallback integrator does not support this expression. "
        "Install sympy for full functionality."
    )


def integrate_expression(expr: str, var: str = "x") -> str:
    """Return the symbolic indefinite integral of ``expr`` with respect to ``var``."""
    try:
        from sympy import Symbol, integrate, sympify

        symbol = Symbol(var)
        parsed_expr = sympify(expr)
        result = integrate(parsed_expr, symbol)
        return str(result)
    except ModuleNotFoundError:
        return _integrate_without_sympy(expr, var)
