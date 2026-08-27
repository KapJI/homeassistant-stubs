from .const import DOMAIN as DOMAIN
from .coordinator import VizioConfigEntry as VizioConfigEntry
from .entity import VizioEntity as VizioEntity
from .helpers import async_device_command as async_device_command
from collections.abc import Iterable
from homeassistant.components.remote import ATTR_DELAY_SECS as ATTR_DELAY_SECS, ATTR_NUM_REPEATS as ATTR_NUM_REPEATS, DEFAULT_DELAY_SECS as DEFAULT_DELAY_SECS, RemoteEntity as RemoteEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int
REMOTE_KEY_ALIASES: dict[str, list[str]]
_ALIAS_LOOKUP: dict[str, str]

async def async_setup_entry(hass: HomeAssistant, config_entry: VizioConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VizioRemote(VizioEntity, RemoteEntity):
    _command_map: dict[str, str]
    def __init__(self, config_entry: VizioConfigEntry) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
    def _resolve_command(self, command: str) -> str: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @override
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
