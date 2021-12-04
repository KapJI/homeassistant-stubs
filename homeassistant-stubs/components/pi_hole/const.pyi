from collections.abc import Callable as Callable
from hole import Hole as Hole
from homeassistant.components.binary_sensor import BinarySensorEntityDescription as BinarySensorEntityDescription, DEVICE_CLASS_UPDATE as DEVICE_CLASS_UPDATE
from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription
from homeassistant.const import PERCENTAGE as PERCENTAGE
from typing import Any

DOMAIN: str
CONF_LOCATION: str
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
MIN_TIME_BETWEEN_UPDATES: Any
DATA_KEY_API: str
DATA_KEY_COORDINATOR: str

class PiHoleSensorEntityDescription(SensorEntityDescription):
    icon: str

SENSOR_TYPES: tuple[PiHoleSensorEntityDescription, ...]

class RequiredPiHoleBinaryDescription:
    state_value: Callable[[Hole], bool]

class PiHoleBinarySensorEntityDescription(BinarySensorEntityDescription, RequiredPiHoleBinaryDescription):
    extra_value: Callable[[Hole], Union[dict[str, Any], None]]

BINARY_SENSOR_TYPES: tuple[PiHoleBinarySensorEntityDescription, ...]
BINARY_SENSOR_TYPES_STATISTICS_ONLY: tuple[PiHoleBinarySensorEntityDescription, ...]
