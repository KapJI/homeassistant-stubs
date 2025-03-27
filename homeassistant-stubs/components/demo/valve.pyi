from _typeshed import Incomplete
from homeassistant.components.valve import ValveEntity as ValveEntity, ValveEntityFeature as ValveEntityFeature, ValveState as ValveState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

OPEN_CLOSE_DELAY: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DemoValve(ValveEntity):
    _attr_should_poll: bool
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _state: Incomplete
    _moveable: Incomplete
    def __init__(self, name: str, state: str, moveable: bool = True) -> None: ...
    @property
    def is_open(self) -> bool: ...
    @property
    def is_opening(self) -> bool: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def is_closed(self) -> bool: ...
    @property
    def reports_position(self) -> bool: ...
    async def async_open_valve(self, **kwargs: Any) -> None: ...
    async def async_close_valve(self, **kwargs: Any) -> None: ...
