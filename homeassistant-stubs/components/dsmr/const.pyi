from .models import DSMRSensor as DSMRSensor
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT
from homeassistant.const import DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_VOLTAGE as DEVICE_CLASS_VOLTAGE
from homeassistant.util import dt as dt
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
SENSORS: list[DSMRSensor]