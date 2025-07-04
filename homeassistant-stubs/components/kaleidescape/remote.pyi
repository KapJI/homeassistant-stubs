from . import KaleidescapeConfigEntry as KaleidescapeConfigEntry
from .entity import KaleidescapeEntity as KaleidescapeEntity
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.remote import RemoteEntity as RemoteEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: KaleidescapeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

VALID_COMMANDS: Incomplete

class KaleidescapeRemote(KaleidescapeEntity, RemoteEntity):
    _attr_name: Incomplete
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
