from .models import ForecastSolarSensorEntityDescription as ForecastSolarSensorEntityDescription
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower

DOMAIN: str
LOGGER: Incomplete
CONF_DECLINATION: str
CONF_AZIMUTH: str
CONF_MODULES_POWER: str
CONF_DAMPING: str
CONF_INVERTER_SIZE: str
SENSORS: tuple[ForecastSolarSensorEntityDescription, ...]
