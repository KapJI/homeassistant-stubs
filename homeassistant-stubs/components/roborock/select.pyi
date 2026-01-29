from .const import DOMAIN as DOMAIN, MAP_SLEEP as MAP_SLEEP
from .coordinator import RoborockB01Q7UpdateCoordinator as RoborockB01Q7UpdateCoordinator, RoborockConfigEntry as RoborockConfigEntry, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockCoordinatedEntityB01 as RoborockCoordinatedEntityB01, RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from roborock import B01Props as B01Props
from roborock.devices.traits.b01 import Q7PropertiesApi as Q7PropertiesApi
from roborock.devices.traits.v1 import PropertiesApi as PropertiesApi
from roborock.devices.traits.v1.home import HomeTrait as HomeTrait
from roborock.devices.traits.v1.maps import MapsTrait as MapsTrait
from roborock.roborock_typing import RoborockCommand
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RoborockSelectDescription(SelectEntityDescription):
    api_command: RoborockCommand
    value_fn: Callable[[PropertiesApi], str | None]
    options_lambda: Callable[[PropertiesApi], list[str] | None]
    parameter_lambda: Callable[[str, PropertiesApi], list[int]]
    is_dock_entity: bool = ...

@dataclass(frozen=True, kw_only=True)
class RoborockB01SelectDescription(SelectEntityDescription):
    api_fn: Callable[[Q7PropertiesApi, str], Awaitable[Any]]
    value_fn: Callable[[B01Props], str | None]
    options_lambda: Callable[[Q7PropertiesApi], list[str] | None]

B01_SELECT_DESCRIPTIONS: list[RoborockB01SelectDescription]
SELECT_DESCRIPTIONS: list[RoborockSelectDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RoborockB01SelectEntity(RoborockCoordinatedEntityB01, SelectEntity):
    entity_description: RoborockB01SelectDescription
    coordinator: RoborockB01Q7UpdateCoordinator
    _attr_options: Incomplete
    def __init__(self, coordinator: RoborockB01Q7UpdateCoordinator, entity_description: RoborockB01SelectDescription, options: list[str]) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    @property
    def current_option(self) -> str | None: ...

class RoborockSelectEntity(RoborockCoordinatedEntityV1, SelectEntity):
    entity_description: RoborockSelectDescription
    _attr_options: Incomplete
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockSelectDescription, options: list[str]) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    @property
    def current_option(self) -> str | None: ...

class RoborockCurrentMapSelectEntity(RoborockCoordinatedEntityV1, SelectEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _home_trait: Incomplete
    _maps_trait: Incomplete
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinator, home_trait: HomeTrait, maps_trait: MapsTrait) -> None: ...
    @property
    def _available_map_names(self) -> dict[int, str]: ...
    async def async_select_option(self, option: str) -> None: ...
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> str | None: ...
