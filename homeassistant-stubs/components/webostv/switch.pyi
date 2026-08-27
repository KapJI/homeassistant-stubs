from .coordinator import WebOsTvConfigEntry as WebOsTvConfigEntry
from .entity import WebOsTvEntity as WebOsTvEntity, cmd as cmd
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: WebOsTvConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LgWebOSScreenSwitchEntity(WebOsTvEntity, SwitchEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, entry: WebOsTvConfigEntry) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def is_on(self) -> bool: ...
    @cmd
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @cmd
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
