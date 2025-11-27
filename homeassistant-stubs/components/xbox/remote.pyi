from .coordinator import XboxConfigEntry as XboxConfigEntry
from .entity import XboxConsoleBaseEntity as XboxConsoleBaseEntity
from collections.abc import Callable as Callable, Iterable
from homeassistant.components.remote import ATTR_DELAY_SECS as ATTR_DELAY_SECS, ATTR_NUM_REPEATS as ATTR_NUM_REPEATS, DEFAULT_DELAY_SECS as DEFAULT_DELAY_SECS, RemoteEntity as RemoteEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pythonxbox.api.provider.smartglass import SmartglassProvider as SmartglassProvider
from typing import Any

PARALLEL_UPDATES: int
MAP_COMMAND: dict[str, Callable[[SmartglassProvider], Callable]]

async def async_setup_entry(hass: HomeAssistant, entry: XboxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class XboxRemote(XboxConsoleBaseEntity, RemoteEntity):
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
