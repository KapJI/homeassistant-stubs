from .coordinator import BraviaTVConfigEntry as BraviaTVConfigEntry
from .entity import BraviaTVEntity as BraviaTVEntity
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.remote import ATTR_NUM_REPEATS as ATTR_NUM_REPEATS, RemoteEntity as RemoteEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

async def async_setup_entry(hass: HomeAssistant, config_entry: BraviaTVConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BraviaTVRemote(BraviaTVEntity, RemoteEntity):
    _attr_name: Incomplete
    @property
    @override
    def is_on(self) -> bool: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @override
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
