from .models import DSMRSensorEntityDescription as DSMRSensorEntityDescription
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorStateClass as SensorStateClass
from homeassistant.const import Platform as Platform
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from typing import Any

DOMAIN: str
LOGGER: Any
PLATFORMS: Any
CONF_DSMR_VERSION: str
CONF_RECONNECT_INTERVAL: str
CONF_PRECISION: str
CONF_TIME_BETWEEN_UPDATE: str
CONF_SERIAL_ID: str
CONF_SERIAL_ID_GAS: str
DEFAULT_DSMR_VERSION: str
DEFAULT_PORT: str
DEFAULT_PRECISION: int
DEFAULT_RECONNECT_INTERVAL: int
DEFAULT_TIME_BETWEEN_UPDATE: int
DATA_TASK: str
DEVICE_NAME_ENERGY: str
DEVICE_NAME_GAS: str
DSMR_VERSIONS: Any
SENSORS: tuple[DSMRSensorEntityDescription, ...]
