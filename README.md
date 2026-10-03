[![PyPI version](https://img.shields.io/pypi/v/homeassistant-stubs)](https://pypi.org/project/homeassistant-stubs/)

# PEP 484 stubs for Home Assistant Core

**This package is deprecated and no longer updated.**

Home Assistant Core ships a `py.typed` marker since 2024.5.0, so type checkers read type information directly from the `homeassistant` package.
Stubs from this package take precedence over it and are less precise, because they only cover strictly typed modules and lose every type that is inferred rather than annotated.

## What to do

Replace `homeassistant-stubs` in your dev dependencies with `homeassistant`:

```shell
uv remove --dev homeassistant-stubs
uv add --dev homeassistant
```

Type checks may become stricter after that: errors that the stubs were hiding behind `Any` will show up, and `# type: ignore` comments for modules missing from the stubs are no longer needed.

## Releases

`2026.10.0` is the final release. It contains no stubs and only depends on `homeassistant`, so projects which still install it get the type information from Home Assistant Core.

Earlier releases still contain stubs and stay available for Home Assistant versions older than 2024.5.0.
