from . import VistapoolConfigEntry as VistapoolConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import VistapoolDataUpdateCoordinator as VistapoolDataUpdateCoordinator
from .entity import VistapoolEntity as VistapoolEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int
_PUMP_MODE_OPTIONS: Incomplete
_PUMP_SPEED_OPTIONS: Incomplete

@dataclass(frozen=True, kw_only=True)
class VistapoolSelectEntityDescription(SelectEntityDescription):
    value_path: str
    exists_path: str | tuple[str, ...] | None = ...
    translation_placeholders: dict[str, str] | None = ...

SELECT_DESCRIPTIONS: tuple[VistapoolSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: VistapoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def _to_index(raw: Any) -> int | None: ...

class VistapoolSelect(VistapoolEntity, SelectEntity):
    entity_description: VistapoolSelectEntityDescription
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, coordinator: VistapoolDataUpdateCoordinator, description: VistapoolSelectEntityDescription) -> None: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
