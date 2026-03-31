# sympy-integrator

A minimal Python package for symbolic integration.

- If `sympy` is installed, it uses full SymPy integration.
- If `sympy` is not installed, it falls back to a tiny built-in demo mode that supports:
  - `sin(x)`
  - `cos(x)`
  - `x`
  - integer constants (e.g. `3`)

## Install

```bash
pip install -e .
```

## Example

```bash
python -m sympy_integrator.cli "sin(x)"
```

Expected output:

```text
-cos(x)
```
