from .models import ForecastSolarSensorEntityDescription as ForecastSolarSensorEntityDescription
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorStateClass as SensorStateClass
from homeassistant.const import ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, POWER_WATT as POWER_WATT

DOMAIN: str
CONF_DECLINATION: str
CONF_AZIMUTH: str
CONF_MODULES_POWER: str
CONF_DAMPING: str
SENSORS: tuple[ForecastSolarSensorEntityDescription, ...]
