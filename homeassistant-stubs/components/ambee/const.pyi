from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_CUBIC_METER as CONCENTRATION_PARTS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION
from typing import Any, Final

DOMAIN: Final[str]
LOGGER: Any
SCAN_INTERVAL: Any
DEVICE_CLASS_AMBEE_RISK: Final[str]
SERVICE_AIR_QUALITY: Final[str]
SERVICE_POLLEN: Final[str]
SERVICES: dict[str, str]
SENSORS: dict[str, list[SensorEntityDescription]]
