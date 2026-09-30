from . import NoboHubConfigEntry as NoboHubConfigEntry
from .const import ATTR_OVERRIDE_ALLOWED as ATTR_OVERRIDE_ALLOWED, DOMAIN as DOMAIN
from .entity import NoboBaseEntity as NoboBaseEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import ATTR_NAME as ATTR_NAME, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pynobo import nobo
from typing import Any, override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: NoboHubConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NoboDisableGlobalOverrideSwitch(NoboBaseEntity, SwitchEntity):
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    _id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, hass: HomeAssistant, zone_id: str, hub: nobo, entry_id: str) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _set_override_allowed(self, override_allowed: str) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    _attr_is_on: Incomplete
    @callback
    @override
    def _read_state(self) -> None: ...
