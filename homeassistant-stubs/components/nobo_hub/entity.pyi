from .const import ATTR_SERIAL as ATTR_SERIAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import Entity as Entity
from pynobo import nobo as nobo
from typing import override

class NoboBaseEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _nobo: Incomplete
    _attr_available: Incomplete
    _hub_device_id: Incomplete
    def __init__(self, hass: HomeAssistant, hub: nobo, entry_id: str) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_will_remove_from_hass(self) -> None: ...
    @callback
    def _handle_hub_update(self, _hub: nobo) -> None: ...
    @callback
    def _handle_hub_connection(self, _hub: nobo, connected: bool) -> None: ...
    @callback
    def _read_state(self) -> None: ...
