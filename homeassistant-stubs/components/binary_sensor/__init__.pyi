from _typeshed import Incomplete
from enum import StrEnum
from functools import cached_property as cached_property
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Literal

_LOGGER: Incomplete
DOMAIN: str
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete

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
_DEPRECATED_DEVICE_CLASS_BATTERY: Incomplete
_DEPRECATED_DEVICE_CLASS_BATTERY_CHARGING: Incomplete
_DEPRECATED_DEVICE_CLASS_CO: Incomplete
_DEPRECATED_DEVICE_CLASS_COLD: Incomplete
_DEPRECATED_DEVICE_CLASS_CONNECTIVITY: Incomplete
_DEPRECATED_DEVICE_CLASS_DOOR: Incomplete
_DEPRECATED_DEVICE_CLASS_GARAGE_DOOR: Incomplete
_DEPRECATED_DEVICE_CLASS_GAS: Incomplete
_DEPRECATED_DEVICE_CLASS_HEAT: Incomplete
_DEPRECATED_DEVICE_CLASS_LIGHT: Incomplete
_DEPRECATED_DEVICE_CLASS_LOCK: Incomplete
_DEPRECATED_DEVICE_CLASS_MOISTURE: Incomplete
_DEPRECATED_DEVICE_CLASS_MOTION: Incomplete
_DEPRECATED_DEVICE_CLASS_MOVING: Incomplete
_DEPRECATED_DEVICE_CLASS_OCCUPANCY: Incomplete
_DEPRECATED_DEVICE_CLASS_OPENING: Incomplete
_DEPRECATED_DEVICE_CLASS_PLUG: Incomplete
_DEPRECATED_DEVICE_CLASS_POWER: Incomplete
_DEPRECATED_DEVICE_CLASS_PRESENCE: Incomplete
_DEPRECATED_DEVICE_CLASS_PROBLEM: Incomplete
_DEPRECATED_DEVICE_CLASS_RUNNING: Incomplete
_DEPRECATED_DEVICE_CLASS_SAFETY: Incomplete
_DEPRECATED_DEVICE_CLASS_SMOKE: Incomplete
_DEPRECATED_DEVICE_CLASS_SOUND: Incomplete
_DEPRECATED_DEVICE_CLASS_TAMPER: Incomplete
_DEPRECATED_DEVICE_CLASS_UPDATE: Incomplete
_DEPRECATED_DEVICE_CLASS_VIBRATION: Incomplete
_DEPRECATED_DEVICE_CLASS_WINDOW: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class BinarySensorEntityDescription(EntityDescription, frozen_or_thawed=True):
    device_class: BinarySensorDeviceClass | None
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement) -> None: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class BinarySensorEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: BinarySensorEntityDescription
    _attr_device_class: BinarySensorDeviceClass | None
    _attr_is_on: bool | None
    _attr_state: None
    async def async_internal_added_to_hass(self) -> None: ...
    def _default_to_device_class_name(self) -> bool: ...
    @cached_property
    def device_class(self) -> BinarySensorDeviceClass | None: ...
    @cached_property
    def is_on(self) -> bool | None: ...
    @property
    def state(self) -> Literal['on', 'off'] | None: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
