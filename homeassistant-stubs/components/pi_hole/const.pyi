from _typeshed import Incomplete
from collections.abc import Callable as Callable
from hole import Hole as Hole
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription
from homeassistant.const import PERCENTAGE as PERCENTAGE
from typing import Any

DOMAIN: str
CONF_STATISTICS_ONLY: str
DEFAULT_LOCATION: str
DEFAULT_METHOD: str
DEFAULT_NAME: str
DEFAULT_SSL: bool
DEFAULT_VERIFY_SSL: bool
DEFAULT_STATISTICS_ONLY: bool
SERVICE_DISABLE: str
SERVICE_DISABLE_ATTR_DURATION: str
ATTR_BLOCKED_DOMAINS: str
MIN_TIME_BETWEEN_UPDATES: Incomplete
DATA_KEY_API: str
DATA_KEY_COORDINATOR: str

class PiHoleSensorEntityDescription(SensorEntityDescription):
    icon: str
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSOR_TYPES: tuple[PiHoleSensorEntityDescription, ...]

class RequiredPiHoleBinaryDescription:
    state_value: Callable[[Hole], bool]
    def __init__(self, state_value) -> None: ...

class PiHoleBinarySensorEntityDescription(BinarySensorEntityDescription, RequiredPiHoleBinaryDescription):
    extra_value: Callable[[Hole], Union[dict[str, Any], None]]
    def __init__(self, state_value, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, extra_value) -> None: ...

BINARY_SENSOR_TYPES: tuple[PiHoleBinarySensorEntityDescription, ...]
BINARY_SENSOR_TYPES_STATISTICS_ONLY: tuple[PiHoleBinarySensorEntityDescription, ...]
