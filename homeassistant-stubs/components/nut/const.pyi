from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, FREQUENCY_HERTZ as FREQUENCY_HERTZ, PERCENTAGE as PERCENTAGE, POWER_VOLT_AMPERE as POWER_VOLT_AMPERE, POWER_WATT as POWER_WATT, Platform as Platform, TEMP_CELSIUS as TEMP_CELSIUS, TIME_SECONDS as TIME_SECONDS
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from typing import Final

DOMAIN: str
PLATFORMS: Incomplete
DEFAULT_NAME: str
DEFAULT_HOST: str
DEFAULT_PORT: int
KEY_STATUS: str
KEY_STATUS_DISPLAY: str
COORDINATOR: str
DEFAULT_SCAN_INTERVAL: int
PYNUT_DATA: str
PYNUT_UNIQUE_ID: str
SENSOR_TYPES: Final[dict[str, SensorEntityDescription]]
STATE_TYPES: Incomplete
