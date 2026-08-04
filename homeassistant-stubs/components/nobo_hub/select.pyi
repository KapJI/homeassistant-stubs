from . import NoboHubConfigEntry as NoboHubConfigEntry
from .const import ATTR_HARDWARE_VERSION as ATTR_HARDWARE_VERSION, ATTR_SOFTWARE_VERSION as ATTR_SOFTWARE_VERSION, CONF_OVERRIDE_TYPE as CONF_OVERRIDE_TYPE, DOMAIN as DOMAIN, NOBO_MANUFACTURER as NOBO_MANUFACTURER, OVERRIDE_TYPE_NOW as OVERRIDE_TYPE_NOW
from .entity import NoboBaseEntity as NoboBaseEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.const import ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pynobo import nobo
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: NoboHubConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NoboGlobalSelector(NoboBaseEntity, SelectEntity):
    _attr_translation_key: str
    _modes: Incomplete
    _attr_options: Incomplete
    _attr_current_option: str | None
    _attr_unique_id: Incomplete
    _override_type: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, hass: HomeAssistant, hub: nobo, override_type: str, entry_id: str) -> None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
    async def async_update(self) -> None: ...
    @callback
    @override
    def _read_state(self) -> None: ...

class NoboProfileSelector(NoboBaseEntity, SelectEntity):
    _attr_translation_key: str
    _attr_current_option: str | None
    _id: Incomplete
    _profiles: dict[str, str]
    _attr_options: list[str]
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, hass: HomeAssistant, zone_id: str, hub: nobo, entry_id: str) -> None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
    async def async_update(self) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @callback
    @override
    def _read_state(self) -> None: ...
