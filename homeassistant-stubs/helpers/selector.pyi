from collections.abc import Callable as Callable
from datetime import time as time_sys
from homeassistant.const import CONF_MODE as CONF_MODE, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import split_entity_id as split_entity_id
from homeassistant.util import decorator as decorator
from typing import Any

SELECTORS: decorator.Registry[str, type[Selector]]

def _get_selector_class(config: Any) -> type[Selector]: ...
def selector(config: Any) -> Selector: ...
def validate_selector(config: Any) -> dict: ...

class Selector:
    CONFIG_SCHEMA: Callable
    config: Any
    selector_type: str
    def __init__(self, config: Any) -> None: ...
    def serialize(self) -> Any: ...

class EntitySelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> str: ...

class DeviceSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> str: ...

class AreaSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> str: ...

class NumberSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> float: ...

class AddonSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> str: ...

class BooleanSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> bool: ...

class TimeSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> time_sys: ...

class TargetSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    TARGET_SELECTION_SCHEMA: Any
    def __call__(self, data: Any) -> dict[str, list[str]]: ...

class ActionSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> Any: ...

class ObjectSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> Any: ...

class StringSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> str: ...

class SelectSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> Any: ...
