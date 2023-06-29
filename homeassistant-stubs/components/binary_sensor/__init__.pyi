from _typeshed import Incomplete
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Literal

_LOGGER: Incomplete
DOMAIN: str
SCAN_INTERVAL: Incomplete
ENTITY_ID_FORMAT: Incomplete

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

DEVICE_CLASSES_SCHEMA: Incomplete
DEVICE_CLASSES: Incomplete
DEVICE_CLASS_BATTERY: Incomplete
DEVICE_CLASS_BATTERY_CHARGING: Incomplete
DEVICE_CLASS_CO: Incomplete
DEVICE_CLASS_COLD: Incomplete
DEVICE_CLASS_CONNECTIVITY: Incomplete
DEVICE_CLASS_DOOR: Incomplete
DEVICE_CLASS_GARAGE_DOOR: Incomplete
DEVICE_CLASS_GAS: Incomplete
DEVICE_CLASS_HEAT: Incomplete
DEVICE_CLASS_LIGHT: Incomplete
DEVICE_CLASS_LOCK: Incomplete
DEVICE_CLASS_MOISTURE: Incomplete
DEVICE_CLASS_MOTION: Incomplete
DEVICE_CLASS_MOVING: Incomplete
DEVICE_CLASS_OCCUPANCY: Incomplete
DEVICE_CLASS_OPENING: Incomplete
DEVICE_CLASS_PLUG: Incomplete
DEVICE_CLASS_POWER: Incomplete
DEVICE_CLASS_PRESENCE: Incomplete
DEVICE_CLASS_PROBLEM: Incomplete
DEVICE_CLASS_RUNNING: Incomplete
DEVICE_CLASS_SAFETY: Incomplete
DEVICE_CLASS_SMOKE: Incomplete
DEVICE_CLASS_SOUND: Incomplete
DEVICE_CLASS_TAMPER: Incomplete
DEVICE_CLASS_UPDATE: Incomplete
DEVICE_CLASS_VIBRATION: Incomplete
DEVICE_CLASS_WINDOW: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class BinarySensorEntityDescription(EntityDescription):
    device_class: BinarySensorDeviceClass | None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class BinarySensorEntity(Entity):
    entity_description: BinarySensorEntityDescription
    _attr_device_class: BinarySensorDeviceClass | None
    _attr_is_on: bool | None
    _attr_state: None
    def _default_to_device_class_name(self) -> bool: ...
    @property
    def device_class(self) -> BinarySensorDeviceClass | None: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def state(self) -> Literal['on', 'off'] | None: ...
