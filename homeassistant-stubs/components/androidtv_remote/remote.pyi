from .const import DOMAIN as DOMAIN
from .entity import AndroidTVRemoteBaseEntity as AndroidTVRemoteBaseEntity
from _typeshed import Incomplete
from androidtvremote2 import AndroidTVRemote as AndroidTVRemote
from collections.abc import Iterable
from homeassistant.components.remote import ATTR_ACTIVITY as ATTR_ACTIVITY, ATTR_DELAY_SECS as ATTR_DELAY_SECS, ATTR_HOLD_SECS as ATTR_HOLD_SECS, ATTR_NUM_REPEATS as ATTR_NUM_REPEATS, DEFAULT_DELAY_SECS as DEFAULT_DELAY_SECS, DEFAULT_HOLD_SECS as DEFAULT_HOLD_SECS, DEFAULT_NUM_REPEATS as DEFAULT_NUM_REPEATS, RemoteEntity as RemoteEntity, RemoteEntityFeature as RemoteEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AndroidTVRemoteEntity(AndroidTVRemoteBaseEntity, RemoteEntity):
    _attr_supported_features: Incomplete
    _attr_current_activity: Incomplete
    def _current_app_updated(self, current_app: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
