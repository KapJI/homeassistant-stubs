from .const import DOMAIN as DOMAIN
from .coordinator import LiebherrConfigEntry as LiebherrConfigEntry, LiebherrCoordinator as LiebherrCoordinator
from .entity import LiebherrEntity as LiebherrEntity, ZONE_POSITION_MAP as ZONE_POSITION_MAP
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyliebherrhomeapi import BioFreshPlusControl, HydroBreezeControl, IceMakerControl
from typing import Any

PARALLEL_UPDATES: int
type SelectControl = IceMakerControl | HydroBreezeControl | BioFreshPlusControl

@dataclass(frozen=True, kw_only=True)
class LiebherrSelectEntityDescription(SelectEntityDescription):
    control_type: type[SelectControl]
    mode_enum: type[StrEnum]
    current_mode_fn: Callable[[SelectControl], StrEnum | str | None]
    options_fn: Callable[[SelectControl], list[str]]
    set_fn: Callable[[LiebherrCoordinator, int, StrEnum], Coroutine[Any, Any, None]]

def _ice_maker_options(control: SelectControl) -> list[str]: ...
def _hydro_breeze_options(control: SelectControl) -> list[str]: ...
def _bio_fresh_plus_options(control: SelectControl) -> list[str]: ...

SELECT_TYPES: list[LiebherrSelectEntityDescription]

def _create_select_entities(coordinators: list[LiebherrCoordinator]) -> list[LiebherrSelectEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: LiebherrConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LiebherrSelectEntity(LiebherrEntity, SelectEntity):
    entity_description: LiebherrSelectEntityDescription
    _zone_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, coordinator: LiebherrCoordinator, description: LiebherrSelectEntityDescription, zone_id: int, has_multiple_zones: bool) -> None: ...
    @property
    def _select_control(self) -> SelectControl | None: ...
    @property
    def current_option(self) -> str | None: ...
    @property
    def available(self) -> bool: ...
    async def async_select_option(self, option: str) -> None: ...
