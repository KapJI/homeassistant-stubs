from . import BesenConfigEntry as BesenConfigEntry
from .coordinator import BesenCoordinator as BesenCoordinator
from .entity import BesenEntity as BesenEntity
from _typeshed import Incomplete
from besen.models import BesenData as BesenData
from collections.abc import Awaitable, Callable as Callable, Mapping
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final, override

PARALLEL_UPDATES: int
TEMPERATURE_UNIT_OPTIONS: Final[Incomplete]
TEMPERATURE_UNIT_VALUES: Final[Incomplete]

def _option_value(value: str | None, options: Mapping[str, str]) -> str | None: ...

@dataclass(frozen=True, kw_only=True)
class BesenSelectEntityDescription(SelectEntityDescription):
    current_option_fn: Callable[[BesenData], str | None]
    option_values: dict[str, str]
    select_option_fn: Callable[[BesenCoordinator, str], Awaitable[None]]

SELECT_DESCRIPTIONS: tuple[BesenSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: BesenConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BesenSelect(BesenEntity, SelectEntity):
    entity_description: BesenSelectEntityDescription
    def __init__(self, coordinator: BesenCoordinator, description: BesenSelectEntityDescription) -> None: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
