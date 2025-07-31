from . import LinkPlayConfigEntry as LinkPlayConfigEntry
from .entity import LinkPlayBaseEntity as LinkPlayBaseEntity, exception_wrap as exception_wrap
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from linkplay.bridge import LinkPlayBridge as LinkPlayBridge, LinkPlayPlayer as LinkPlayPlayer
from linkplay.consts import AudioOutputHwMode
from typing import Any

_LOGGER: Incomplete
AUDIO_OUTPUT_HW_MODE_MAP: dict[AudioOutputHwMode, str]
AUDIO_OUTPUT_HW_MODE_MAP_INV: dict[str, AudioOutputHwMode]

async def _get_current_option(bridge: LinkPlayBridge) -> str: ...

@dataclass(frozen=True, kw_only=True)
class LinkPlaySelectEntityDescription(SelectEntityDescription):
    set_option_fn: Callable[[LinkPlayPlayer, str], Coroutine[Any, Any, None]]
    current_option_fn: Callable[[LinkPlayPlayer], Awaitable[str]]

SELECT_TYPES_WIIM: tuple[LinkPlaySelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: LinkPlayConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LinkPlaySelect(LinkPlayBaseEntity, SelectEntity):
    entity_description: LinkPlaySelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, bridge: LinkPlayPlayer, description: LinkPlaySelectEntityDescription) -> None: ...
    _attr_current_option: Incomplete
    async def async_update(self) -> None: ...
    @exception_wrap
    async def async_select_option(self, option: str) -> None: ...
