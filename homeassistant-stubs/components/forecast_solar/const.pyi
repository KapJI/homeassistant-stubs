from .models import ForecastSolarSensorEntityDescription as ForecastSolarSensorEntityDescription
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT
from homeassistant.const import DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, POWER_WATT as POWER_WATT
from typing import Final

DOMAIN: str
CONF_DECLINATION: str
CONF_AZIMUTH: str
CONF_MODULES_POWER: str
CONF_DAMPING: str
ATTR_ENTRY_TYPE: Final[str]
ENTRY_TYPE_SERVICE: Final[str]
SENSORS: tuple[ForecastSolarSensorEntityDescription, ...]
