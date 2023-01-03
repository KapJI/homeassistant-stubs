from aioairzone.common import TemperatureUnit
from homeassistant.const import TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from typing import Final

DOMAIN: Final[str]
MANUFACTURER: Final[str]
AIOAIRZONE_DEVICE_TIMEOUT_SEC: Final[int]
API_TEMPERATURE_STEP: Final[float]
TEMP_UNIT_LIB_TO_HASS: Final[dict[TemperatureUnit, str]]
