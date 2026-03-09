from .const import DOMAIN as DOMAIN
from .coordinator import XboxConfigEntry as XboxConfigEntry
from .entity import XboxConsoleBaseEntity as XboxConsoleBaseEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine, Iterable
from homeassistant.components.remote import ATTR_DELAY_SECS as ATTR_DELAY_SECS, ATTR_NUM_REPEATS as ATTR_NUM_REPEATS, DEFAULT_DELAY_SECS as DEFAULT_DELAY_SECS, RemoteEntity as RemoteEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pythonxbox.api.provider.smartglass import SmartglassProvider as SmartglassProvider
from typing import Any, Concatenate

_LOGGER: Incomplete
PARALLEL_UPDATES: int
MAP_COMMAND: dict[str, Callable[[SmartglassProvider], Callable]]

async def async_setup_entry(hass: HomeAssistant, entry: XboxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def exception_handler[**_P, _R](func: Callable[Concatenate[XboxRemote, _P], Awaitable[_R]]) -> Callable[Concatenate[XboxRemote, _P], Coroutine[Any, Any, _R]]: ...

class XboxRemote(XboxConsoleBaseEntity, RemoteEntity):
    @property
    def is_on(self) -> bool: ...
    @exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @exception_handler
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
