from .const import DOMAIN as DOMAIN, SERVICE_PRESS as SERVICE_PRESS
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType

SCAN_INTERVAL: Incomplete
ENTITY_ID_FORMAT: Incomplete
MIN_TIME_BETWEEN_SCANS: Incomplete
_LOGGER: Incomplete

class ButtonDeviceClass(StrEnum):
    IDENTIFY: str
    RESTART: str
    UPDATE: str

DEVICE_CLASSES_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

@dataclass
class ButtonEntityDescription(EntityDescription):
    device_class: ButtonDeviceClass | None = ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class ButtonEntity(RestoreEntity):
    entity_description: ButtonEntityDescription
    _attr_should_poll: bool
    _attr_device_class: ButtonDeviceClass | None
    _attr_state: None
    __last_pressed: datetime | None
    def _default_to_device_class_name(self) -> bool: ...
    @property
    def device_class(self) -> ButtonDeviceClass | None: ...
    @property
    def state(self) -> str | None: ...
    async def _async_press_action(self) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    def press(self) -> None: ...
    async def async_press(self) -> None: ...
