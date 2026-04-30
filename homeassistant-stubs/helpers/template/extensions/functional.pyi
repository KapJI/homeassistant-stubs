import jinja2
from .base import BaseTemplateExtension as BaseTemplateExtension, TemplateFunction as TemplateFunction
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import ServiceResponse as ServiceResponse
from homeassistant.helpers.template import TemplateEnvironment as TemplateEnvironment
from jinja2 import pass_context
from typing import Any

_SENTINEL: Incomplete

class FunctionalExtension(BaseTemplateExtension):
    def __init__(self, environment: TemplateEnvironment) -> None: ...
    @staticmethod
    def apply(value: Any, fn: Any, *args: Any, **kwargs: Any) -> Any: ...
    @staticmethod
    def as_function(macro: jinja2.runtime.Macro) -> Callable[..., Any]: ...
    @staticmethod
    def iif(value: Any, if_true: Any = True, if_false: Any = False, if_none: Any = ...) -> Any: ...
    @staticmethod
    def merge_response(value: ServiceResponse) -> list[Any]: ...
    @staticmethod
    def combine(*args: Any, recursive: bool = False) -> dict[Any, Any]: ...
    @staticmethod
    def typeof(value: Any) -> Any: ...
    @staticmethod
    def fail_when_undefined(value: Any) -> Any: ...

@pass_context
def _random_every_time(context: Any, values: Any) -> Any: ...
