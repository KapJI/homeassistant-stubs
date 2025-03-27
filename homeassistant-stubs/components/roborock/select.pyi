from .const import MAP_SLEEP as MAP_SLEEP
from .coordinator import RoborockConfigEntry as RoborockConfigEntry, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from roborock.roborock_message import RoborockDataProtocol
from roborock.roborock_typing import DeviceProp as DeviceProp, RoborockCommand

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RoborockSelectDescription(SelectEntityDescription):
    api_command: RoborockCommand
    value_fn: Callable[[DeviceProp], str | None]
    options_lambda: Callable[[DeviceProp], list[str] | None]
    parameter_lambda: Callable[[str, DeviceProp], list[int]]
    protocol_listener: RoborockDataProtocol | None = ...
    is_dock_entity: bool = ...

SELECT_DESCRIPTIONS: list[RoborockSelectDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

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
    async def async_select_option(self, option: str) -> None: ...
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> str | None: ...
