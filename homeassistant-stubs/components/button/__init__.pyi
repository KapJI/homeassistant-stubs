from .const import DOMAIN as DOMAIN, SERVICE_PRESS as SERVICE_PRESS
from _typeshed import Incomplete
from enum import StrEnum
from functools import cached_property as cached_property
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
MIN_TIME_BETWEEN_SCANS: Incomplete

class ButtonDeviceClass(StrEnum):
    IDENTIFY: str
    RESTART: str
    UPDATE: str

DEVICE_CLASSES_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class ButtonEntityDescription(EntityDescription, frozen_or_thawed=True):
    device_class: ButtonDeviceClass | None
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement) -> None: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class ButtonEntity(RestoreEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: ButtonEntityDescription
    _attr_should_poll: bool
    _attr_device_class: ButtonDeviceClass | None
    _attr_state: None
    __last_pressed_isoformat: str | None
    def _default_to_device_class_name(self) -> bool: ...
    @cached_property
    def device_class(self) -> ButtonDeviceClass | None: ...
    @cached_property
    def state(self) -> str | None: ...
    def __set_state(self, state: str | None) -> None: ...
    async def _async_press_action(self) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    def press(self) -> None: ...
    async def async_press(self) -> None: ...
