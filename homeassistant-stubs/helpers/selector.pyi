from collections.abc import Callable as Callable
from homeassistant.const import CONF_MODE as CONF_MODE, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import split_entity_id as split_entity_id, valid_entity_id as valid_entity_id
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

SINGLE_ENTITY_SELECTOR_CONFIG_SCHEMA: Any
SINGLE_DEVICE_SELECTOR_CONFIG_SCHEMA: Any

class ActionSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> Any: ...

class AddonSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> str: ...

class AreaSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> Union[str, list[str]]: ...

class AttributeSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> str: ...

class BooleanSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> bool: ...

class ColorRGBSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> list[int]: ...

class ColorTempSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> int: ...

class DateSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> Any: ...

class DateTimeSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> Any: ...

class DeviceSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> Union[str, list[str]]: ...

class DurationSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> dict[str, float]: ...

class EntitySelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> Union[str, list[str]]: ...

class IconSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> str: ...

class LocationSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    DATA_SCHEMA: Any
    def __call__(self, data: Any) -> dict[str, float]: ...

class MediaSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    DATA_SCHEMA: Any
    def __call__(self, data: Any) -> dict[str, float]: ...

def has_min_max_if_slider(data: Any) -> Any: ...

class NumberSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> float: ...

class ObjectSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> Any: ...

select_option: Any

class SelectSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> Any: ...

class StringSelector(Selector):
    selector_type: str
    STRING_TYPES: Any
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> str: ...

class TargetSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    TARGET_SELECTION_SCHEMA: Any
    def __call__(self, data: Any) -> dict[str, list[str]]: ...

class ThemeSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> str: ...

class TimeSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Any
    def __call__(self, data: Any) -> str: ...
