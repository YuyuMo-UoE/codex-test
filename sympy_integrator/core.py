"""Core symbolic integration logic."""

from sympy import Symbol, integrate, sympify


def integrate_expression(expr: str, var: str = "x") -> str:
    """Return the symbolic indefinite integral of ``expr`` with respect to ``var``.

    Args:
        expr: Expression to integrate, e.g. ``"sin(x)"``.
        var: Integration variable, default ``"x"``.

    Returns:
        String representation of integrated expression.
    """
    symbol = Symbol(var)
    parsed_expr = sympify(expr)
    result = integrate(parsed_expr, symbol)
    return str(result)
