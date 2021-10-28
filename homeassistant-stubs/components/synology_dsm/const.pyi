from homeassistant.components.binary_sensor import BinarySensorEntityDescription as BinarySensorEntityDescription, DEVICE_CLASS_SAFETY as DEVICE_CLASS_SAFETY, DEVICE_CLASS_UPDATE as DEVICE_CLASS_UPDATE
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntityDescription as SensorEntityDescription
from homeassistant.components.switch import SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import DATA_MEGABYTES as DATA_MEGABYTES, DATA_RATE_KILOBYTES_PER_SECOND as DATA_RATE_KILOBYTES_PER_SECOND, DATA_TERABYTES as DATA_TERABYTES, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, ENTITY_CATEGORY_CONFIG as ENTITY_CATEGORY_CONFIG, ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC, PERCENTAGE as PERCENTAGE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from typing import Any

DOMAIN: str
PLATFORMS: Any
COORDINATOR_CAMERAS: str
COORDINATOR_CENTRAL: str
COORDINATOR_SWITCHES: str
SYSTEM_LOADED: str
EXCEPTION_DETAILS: str
EXCEPTION_UNKNOWN: str
SYNO_API: str
UNDO_UPDATE_LISTENER: str
CONF_SERIAL: str
CONF_VOLUMES: str
CONF_DEVICE_TOKEN: str
DEFAULT_USE_SSL: bool
DEFAULT_VERIFY_SSL: bool
DEFAULT_PORT: int
DEFAULT_PORT_SSL: int
DEFAULT_SCAN_INTERVAL: int
DEFAULT_TIMEOUT: int
ENTITY_UNIT_LOAD: str
SERVICE_REBOOT: str
SERVICE_SHUTDOWN: str
SERVICES: Any

class SynologyDSMRequiredKeysMixin:
    api_key: str

class SynologyDSMEntityDescription(EntityDescription, SynologyDSMRequiredKeysMixin): ...
class SynologyDSMBinarySensorEntityDescription(BinarySensorEntityDescription, SynologyDSMEntityDescription): ...
class SynologyDSMSensorEntityDescription(SensorEntityDescription, SynologyDSMEntityDescription): ...
class SynologyDSMSwitchEntityDescription(SwitchEntityDescription, SynologyDSMEntityDescription): ...

UPGRADE_BINARY_SENSORS: tuple[SynologyDSMBinarySensorEntityDescription, ...]
SECURITY_BINARY_SENSORS: tuple[SynologyDSMBinarySensorEntityDescription, ...]
STORAGE_DISK_BINARY_SENSORS: tuple[SynologyDSMBinarySensorEntityDescription, ...]
UTILISATION_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
STORAGE_VOL_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
STORAGE_DISK_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
INFORMATION_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
SURVEILLANCE_SWITCH: tuple[SynologyDSMSwitchEntityDescription, ...]
