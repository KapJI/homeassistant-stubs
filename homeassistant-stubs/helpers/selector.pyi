from homeassistant.const import CONF_MODE as CONF_MODE, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.util import decorator as decorator
from typing import Any, Callable

SELECTORS: Any

def validate_selector(config: Any) -> dict: ...

class Selector:
    CONFIG_SCHEMA: Callable

class EntitySelector(Selector):
    CONFIG_SCHEMA: Any = ...

class DeviceSelector(Selector):
    CONFIG_SCHEMA: Any = ...

class AreaSelector(Selector):
    CONFIG_SCHEMA: Any = ...

class NumberSelector(Selector):
    CONFIG_SCHEMA: Any = ...

class AddonSelector(Selector):
    CONFIG_SCHEMA: Any = ...

class BooleanSelector(Selector):
    CONFIG_SCHEMA: Any = ...

class TimeSelector(Selector):
    CONFIG_SCHEMA: Any = ...

class TargetSelector(Selector):
    CONFIG_SCHEMA: Any = ...

class ActionSelector(Selector):
    CONFIG_SCHEMA: Any = ...

class ObjectSelector(Selector):
    CONFIG_SCHEMA: Any = ...

class StringSelector(Selector):
    CONFIG_SCHEMA: Any = ...

class SelectSelector(Selector):
    CONFIG_SCHEMA: Any = ...
