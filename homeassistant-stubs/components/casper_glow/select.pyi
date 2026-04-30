from .const import DIMMING_TIME_OPTIONS as DIMMING_TIME_OPTIONS
from .coordinator import CasperGlowConfigEntry as CasperGlowConfigEntry, CasperGlowCoordinator as CasperGlowCoordinator
from .entity import CasperGlowEntity as CasperGlowEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from pycasperglow import GlowState as GlowState

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: CasperGlowConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CasperGlowDimmingTimeSelect(CasperGlowEntity, SelectEntity, RestoreEntity):
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    _attr_options: Incomplete
    _attr_unit_of_measurement: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: CasperGlowCoordinator) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_state_update(self, state: GlowState) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
