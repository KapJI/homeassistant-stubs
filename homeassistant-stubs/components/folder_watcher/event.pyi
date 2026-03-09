from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FolderWatcherEventEntity(EventEntity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _attr_event_types: Incomplete
    _attr_name: Incomplete
    _attr_translation_key = DOMAIN
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _entry: Incomplete
    def __init__(self, entry: ConfigEntry) -> None: ...
    @callback
    def _async_handle_event(self, event: str, _extra: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
