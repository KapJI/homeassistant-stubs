from .coordinator import HotSpringConfigEntry as HotSpringConfigEntry, HotSpringDataUpdateCoordinator as HotSpringDataUpdateCoordinator
from .entity import HotSpringEntity as HotSpringEntity
from .helpers import hotspring_exception_handler as hotspring_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from hotspring import HeatingMode, HotSpring as HotSpring, Jet as Jet, JetSpeed, Spa
from typing import override

PARALLEL_UPDATES: int
OPTION_OFF: str
OPTION_LOW: str
OPTION_HIGH: str
JET_SPEED_TO_OPTION: dict[JetSpeed, str]
OPTION_TO_JET_SPEED: dict[str, JetSpeed]
DUAL_SPEED_OPTIONS: Incomplete
SINGLE_SPEED_OPTIONS: Incomplete
OPTION_HEAT_SAVER: str
OPTION_HEAT_WITH_BOOST: str
OPTION_AUTO_SAVER: str
OPTION_AUTO_WITH_BOOST: str
OPTION_CHILL: str
HEATING_MODE_TO_OPTION: dict[HeatingMode, str]
OPTION_TO_HEATING_MODE: dict[str, HeatingMode]

@dataclass(frozen=True, kw_only=True)
class HotSpringJetSelectEntityDescription(SelectEntityDescription):
    current_option_fn: Callable[[Jet], str | None]
    select_option_fn: Callable[[HotSpring, int, str], Awaitable[None]]
    options_fn: Callable[[Jet], list[str]]
    exists_fn: Callable[[Jet], bool] = ...

@dataclass(frozen=True, kw_only=True)
class HotSpringHeatingModeSelectEntityDescription(SelectEntityDescription):
    current_option_fn: Callable[[Spa], str | None]
    select_option_fn: Callable[[HotSpring, str], Awaitable[None]]
    options_fn: Callable[[Spa], list[str]]
    exists_fn: Callable[[Spa], bool] = ...

def _heating_mode_options(spa: Spa) -> list[str]: ...

JET_DESCRIPTIONS: tuple[HotSpringJetSelectEntityDescription, ...]
HEATING_MODE_DESCRIPTIONS: tuple[HotSpringHeatingModeSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: HotSpringConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HotSpringJetSelectEntity(HotSpringEntity, SelectEntity):
    entity_description: HotSpringJetSelectEntityDescription
    _jet_id: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, coordinator: HotSpringDataUpdateCoordinator, description: HotSpringJetSelectEntityDescription, jet_id: int) -> None: ...
    @property
    def _jet(self) -> Jet: ...
    @property
    @override
    def options(self) -> list[str]: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @hotspring_exception_handler
    @override
    async def async_select_option(self, option: str) -> None: ...

class HotSpringHeatingModeSelectEntity(HotSpringEntity, SelectEntity):
    entity_description: HotSpringHeatingModeSelectEntityDescription
    def __init__(self, coordinator: HotSpringDataUpdateCoordinator, description: HotSpringHeatingModeSelectEntityDescription) -> None: ...
    @property
    @override
    def options(self) -> list[str]: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @hotspring_exception_handler
    @override
    async def async_select_option(self, option: str) -> None: ...
