from .const import DOMAIN as DOMAIN
from .coordinator import LiebherrConfigEntry as LiebherrConfigEntry, LiebherrCoordinator as LiebherrCoordinator
from .entity import LiebherrEntity as LiebherrEntity, ZONE_POSITION_MAP as ZONE_POSITION_MAP
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyliebherrhomeapi import ToggleControl
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LiebherrSwitchEntityDescription(SwitchEntityDescription):
    control_name: str

@dataclass(frozen=True, kw_only=True)
class LiebherrZoneSwitchEntityDescription(LiebherrSwitchEntityDescription):
    set_fn: Callable[[LiebherrCoordinator, int, bool], Awaitable[None]]

@dataclass(frozen=True, kw_only=True)
class LiebherrDeviceSwitchEntityDescription(LiebherrSwitchEntityDescription):
    set_fn: Callable[[LiebherrCoordinator, bool], Awaitable[None]]

ZONE_SWITCH_TYPES: dict[str, LiebherrZoneSwitchEntityDescription]
DEVICE_SWITCH_TYPES: dict[str, LiebherrDeviceSwitchEntityDescription]

def _create_switch_entities(coordinators: list[LiebherrCoordinator]) -> list[LiebherrDeviceSwitch | LiebherrZoneSwitch]: ...
async def async_setup_entry(hass: HomeAssistant, entry: LiebherrConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LiebherrDeviceSwitch(LiebherrEntity, SwitchEntity):
    entity_description: LiebherrSwitchEntityDescription
    _zone_id: int | None
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LiebherrCoordinator, description: LiebherrSwitchEntityDescription) -> None: ...
    @property
    def _toggle_control(self) -> ToggleControl | None: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def available(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_call_set_fn(self, value: bool) -> None: ...
    async def _async_set_value(self, value: bool) -> None: ...

class LiebherrZoneSwitch(LiebherrDeviceSwitch):
    entity_description: LiebherrZoneSwitchEntityDescription
    _zone_id: int
    _attr_unique_id: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, coordinator: LiebherrCoordinator, description: LiebherrZoneSwitchEntityDescription, zone_id: int, has_multiple_zones: bool) -> None: ...
    async def _async_call_set_fn(self, value: bool) -> None: ...
