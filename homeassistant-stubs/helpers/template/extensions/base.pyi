from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.helpers.template import TemplateEnvironment as TemplateEnvironment
from jinja2.ext import Extension
from jinja2.nodes import Node as Node
from jinja2.parser import Parser as Parser
from typing import Any

@dataclass
class TemplateFunction:
    name: str
    func: Callable[..., Any] | Any
    as_global: bool = ...
    as_filter: bool = ...
    as_test: bool = ...
    limited_ok: bool = ...

class BaseTemplateExtension(Extension):
    environment: TemplateEnvironment
    def __init__(self, environment: TemplateEnvironment, *, functions: list[TemplateFunction] | None = None) -> None: ...
    def parse(self, parser: Parser) -> Node | list[Node]: ...
