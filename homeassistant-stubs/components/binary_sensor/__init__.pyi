from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Literal

_LOGGER: Any
DOMAIN: str
SCAN_INTERVAL: Any
ENTITY_ID_FORMAT: Any

class BinarySensorDeviceClass(StrEnum):
    BATTERY: str
    BATTERY_CHARGING: str
    CO: str
    COLD: str
    CONNECTIVITY: str
    DOOR: str
    GARAGE_DOOR: str
    GAS: str
    HEAT: str
    LIGHT: str
    LOCK: str
    MOISTURE: str
    MOTION: str
    MOVING: str
    OCCUPANCY: str
    OPENING: str
    PLUG: str
    POWER: str
    PRESENCE: str
    PROBLEM: str
    RUNNING: str
    SAFETY: str
    SMOKE: str
    SOUND: str
    TAMPER: str
    UPDATE: str
    VIBRATION: str
    WINDOW: str

DEVICE_CLASSES_SCHEMA: Any
DEVICE_CLASSES: Any
DEVICE_CLASS_BATTERY: Any
DEVICE_CLASS_BATTERY_CHARGING: Any
DEVICE_CLASS_CO: Any
DEVICE_CLASS_COLD: Any
DEVICE_CLASS_CONNECTIVITY: Any
DEVICE_CLASS_DOOR: Any
DEVICE_CLASS_GARAGE_DOOR: Any
DEVICE_CLASS_GAS: Any
DEVICE_CLASS_HEAT: Any
DEVICE_CLASS_LIGHT: Any
DEVICE_CLASS_LOCK: Any
DEVICE_CLASS_MOISTURE: Any
DEVICE_CLASS_MOTION: Any
DEVICE_CLASS_MOVING: Any
DEVICE_CLASS_OCCUPANCY: Any
DEVICE_CLASS_OPENING: Any
DEVICE_CLASS_PLUG: Any
DEVICE_CLASS_POWER: Any
DEVICE_CLASS_PRESENCE: Any
DEVICE_CLASS_PROBLEM: Any
DEVICE_CLASS_RUNNING: Any
DEVICE_CLASS_SAFETY: Any
DEVICE_CLASS_SMOKE: Any
DEVICE_CLASS_SOUND: Any
DEVICE_CLASS_TAMPER: Any
DEVICE_CLASS_UPDATE: Any
DEVICE_CLASS_VIBRATION: Any
DEVICE_CLASS_WINDOW: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class BinarySensorEntityDescription(EntityDescription):
    device_class: Union[BinarySensorDeviceClass, str, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

class BinarySensorEntity(Entity):
    entity_description: BinarySensorEntityDescription
    _attr_device_class: Union[BinarySensorDeviceClass, str, None]
    _attr_is_on: Union[bool, None]
    _attr_state: None
    @property
    def device_class(self) -> Union[BinarySensorDeviceClass, str, None]: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
    @property
    def state(self) -> Union[Literal['on', 'off'], None]: ...
