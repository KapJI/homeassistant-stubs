from .coordinator import JVCConfigEntry as JVCConfigEntry, JvcProjectorDataUpdateCoordinator as JvcProjectorDataUpdateCoordinator
from .entity import JvcProjectorEntity as JvcProjectorEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from jvcprojector import Command as Command
from typing import Final

@dataclass(frozen=True, kw_only=True)
class JvcProjectorSelectDescription(SelectEntityDescription):
    command: type[Command]
    snake_case_states: bool = ...

SELECTS: Final[tuple[JvcProjectorSelectDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: JVCConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class JvcProjectorSelectEntity(JvcProjectorEntity, SelectEntity):
    command: type[Command]
    entity_description: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    _options_map: dict[str, str]
    def __init__(self, coordinator: JvcProjectorDataUpdateCoordinator, description: JvcProjectorSelectDescription) -> None: ...
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
