from . import PooldoseConfigEntry as PooldoseConfigEntry
from .const import UNIT_MAPPING as UNIT_MAPPING
from .coordinator import PooldoseCoordinator as PooldoseCoordinator
from .entity import PooldoseEntity as PooldoseEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PooldoseSelectEntityDescription(SelectEntityDescription):
    use_unit_conversion: bool = ...

SELECT_DESCRIPTIONS: tuple[PooldoseSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: PooldoseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PooldoseSelect(PooldoseEntity, SelectEntity):
    entity_description: PooldoseSelectEntityDescription
    def __init__(self, coordinator: PooldoseCoordinator, serial_number: str, device_info: Any, description: PooldoseSelectEntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    _attr_current_option: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
