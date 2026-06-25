from . import setup_mysensors_platform as setup_mysensors_platform
from .const import DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY
from .entity import MySensorsChildEntity as MySensorsChildEntity
from collections.abc import Iterable
from homeassistant.components.remote import ATTR_COMMAND as ATTR_COMMAND, RemoteEntity as RemoteEntity, RemoteEntityFeature as RemoteEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MySensorsRemote(MySensorsChildEntity, RemoteEntity):
    _current_command: str | None
    @property
    @override
    def is_on(self) -> bool | None: ...
    @property
    @override
    def supported_features(self) -> RemoteEntityFeature: ...
    @override
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
    @override
    async def async_learn_command(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    @override
    def _async_update(self) -> None: ...
