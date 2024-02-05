from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from enum import StrEnum
from functools import cached_property as cached_property
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass

SCAN_INTERVAL: Incomplete
ENTITY_ID_FORMAT: Incomplete
MIN_TIME_BETWEEN_SCANS: Incomplete
_LOGGER: Incomplete

class SwitchDeviceClass(StrEnum):
    OUTLET: str
    SWITCH: str

DEVICE_CLASSES_SCHEMA: Incomplete
DEVICE_CLASSES: Incomplete
_DEPRECATED_DEVICE_CLASS_OUTLET: Incomplete
_DEPRECATED_DEVICE_CLASS_SWITCH: Incomplete

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SwitchEntityDescription(ToggleEntityDescription, frozen_or_thawed=True):
    device_class: SwitchDeviceClass | None
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement) -> None: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class SwitchEntity(ToggleEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: SwitchEntityDescription
    _attr_device_class: SwitchDeviceClass | None
    @cached_property
    def device_class(self) -> SwitchDeviceClass | None: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
