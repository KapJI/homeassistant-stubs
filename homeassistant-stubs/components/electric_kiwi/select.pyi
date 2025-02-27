from .const import ATTRIBUTION as ATTRIBUTION
from .coordinator import ElectricKiwiConfigEntry as ElectricKiwiConfigEntry, ElectricKiwiHOPDataCoordinator as ElectricKiwiHOPDataCoordinator
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int
_LOGGER: Incomplete
ATTR_EK_HOP_SELECT: str
HOP_SELECT: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ElectricKiwiConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ElectricKiwiSelectHOPEntity(CoordinatorEntity[ElectricKiwiHOPDataCoordinator], SelectEntity):
    entity_description: SelectEntityDescription
    _attr_has_entity_name: bool
    _attr_attribution = ATTRIBUTION
    values_dict: dict[str, int]
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: ElectricKiwiHOPDataCoordinator, description: SelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
