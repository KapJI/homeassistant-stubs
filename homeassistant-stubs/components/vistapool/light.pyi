from . import VistapoolConfigEntry as VistapoolConfigEntry
from .const import DOMAIN as DOMAIN, SIGNAL_NEW_POOL as SIGNAL_NEW_POOL
from .coordinator import VistapoolDataUpdateCoordinator as VistapoolDataUpdateCoordinator
from .entity import VistapoolEntity as VistapoolEntity
from _typeshed import Incomplete
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int
_VALUE_PATH: str

async def async_setup_entry(hass: HomeAssistant, entry: VistapoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VistapoolLight(VistapoolEntity, LightEntity):
    _attr_translation_key: str
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VistapoolDataUpdateCoordinator) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_set_value(self, value: int) -> None: ...
