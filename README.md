[![CI](https://github.com/KapJI/homeassistant-stubs/actions/workflows/ci.yaml/badge.svg)](https://github.com/KapJI/homeassistant-stubs/actions/workflows/ci.yaml)
[![PyPI version](https://img.shields.io/pypi/v/homeassistant-stubs)](https://pypi.org/project/homeassistant-stubs/)

# PEP 484 stubs for Home Assistant Core

This is unofficial stub-only package generated from [Home Assistant Core](https://github.com/home-assistant/core) sources.
You can use it to enable type checks against Home Assistant code in your custom component or AppDaemon app.

## How to use

Add it to dev dependencies of your project.
I recommend to use [uv](https://docs.astral.sh/uv/) for managing dependencies:

```shell
uv add --dev homeassistant-stubs
```

Please note that only stubs from strictly typed modules are added in this package.
This includes all core modules and some components.
Generic components like `sensor`, `light` or `media_player` are already typed.

If your project imports not yet typed components, `mypy` will be unable to find that module.
The best thing you can do to fix this is to submit PR to HA Core which adds type hints for these components.
After that stubs for these components will become available in this package.

## Motivation

Home Assistant maintainers don't want to distribute typing information with `homeassistant` package
([[1]](https://github.com/home-assistant/core/pull/28866),
[[2]](https://github.com/home-assistant/core/pull/47796)).
The reason is that [PEP 561](https://www.python.org/dev/peps/pep-0561/#packaging-type-information)
says that `py.typed` marker is applied recursively and the whole package must support type checking.
But many of the Home Assistant components are currently not type checked.

## How it works

- `update_stubs.py` script extracts list of strictly typed modules from Home Assistant configs.
- Then it runs `stubgen` which is shipped with `mypy` to generate typing stubs.
- New versions are generated and published automatically every 12 hours.
