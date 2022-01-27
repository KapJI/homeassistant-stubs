from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.components.switch import SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import DATA_MEGABYTES as DATA_MEGABYTES, DATA_RATE_KILOBYTES_PER_SECOND as DATA_RATE_KILOBYTES_PER_SECOND, DATA_TERABYTES as DATA_TERABYTES, PERCENTAGE as PERCENTAGE, Platform as Platform, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.helpers.entity import EntityCategory as EntityCategory, EntityDescription as EntityDescription
from synology_dsm.api.surveillance_station.const import SNAPSHOT_PROFILE_BALANCED
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
CONF_SNAPSHOT_QUALITY: str
DEFAULT_USE_SSL: bool
DEFAULT_VERIFY_SSL: bool
DEFAULT_PORT: int
DEFAULT_PORT_SSL: int
DEFAULT_SCAN_INTERVAL: int
DEFAULT_TIMEOUT: int
DEFAULT_SNAPSHOT_QUALITY = SNAPSHOT_PROFILE_BALANCED
ENTITY_UNIT_LOAD: str
SERVICE_REBOOT: str
SERVICE_SHUTDOWN: str
SERVICES: Any

class SynologyDSMRequiredKeysMixin:
    api_key: str
    def __init__(self, api_key) -> None: ...

class SynologyDSMEntityDescription(EntityDescription, SynologyDSMRequiredKeysMixin):
    def __init__(self, api_key, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

class SynologyDSMBinarySensorEntityDescription(BinarySensorEntityDescription, SynologyDSMEntityDescription):
    def __init__(self, api_key, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

class SynologyDSMSensorEntityDescription(SensorEntityDescription, SynologyDSMEntityDescription):
    def __init__(self, api_key, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

class SynologyDSMSwitchEntityDescription(SwitchEntityDescription, SynologyDSMEntityDescription):
    def __init__(self, api_key, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

UPGRADE_BINARY_SENSORS: tuple[SynologyDSMBinarySensorEntityDescription, ...]
SECURITY_BINARY_SENSORS: tuple[SynologyDSMBinarySensorEntityDescription, ...]
STORAGE_DISK_BINARY_SENSORS: tuple[SynologyDSMBinarySensorEntityDescription, ...]
UTILISATION_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
STORAGE_VOL_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
STORAGE_DISK_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
INFORMATION_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
SURVEILLANCE_SWITCH: tuple[SynologyDSMSwitchEntityDescription, ...]
