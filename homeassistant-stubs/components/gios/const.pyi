from .model import GiosSensorEntityDescription as GiosSensorEntityDescription
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
from typing import Any, Final

ATTRIBUTION: Final[str]
CONF_STATION_ID: Final[str]
DEFAULT_NAME: Final[str]
SCAN_INTERVAL: Final[Any]
DOMAIN: Final[str]
MANUFACTURER: Final[str]
API_TIMEOUT: Final[int]
ATTR_INDEX: Final[str]
ATTR_STATION: Final[str]
ATTR_C6H6: Final[str]
ATTR_CO: Final[str]
ATTR_NO2: Final[str]
ATTR_O3: Final[str]
ATTR_PM10: Final[str]
ATTR_PM25: Final[str]
ATTR_SO2: Final[str]
ATTR_AQI: Final[str]
SENSOR_TYPES: Final[tuple[GiosSensorEntityDescription, ...]]
