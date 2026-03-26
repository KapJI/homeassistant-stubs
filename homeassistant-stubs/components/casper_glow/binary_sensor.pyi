from .coordinator import CasperGlowConfigEntry as CasperGlowConfigEntry, CasperGlowCoordinator as CasperGlowCoordinator
from .entity import CasperGlowEntity as CasperGlowEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pycasperglow import GlowState as GlowState

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: CasperGlowConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CasperGlowPausedBinarySensor(CasperGlowEntity, BinarySensorEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, coordinator: CasperGlowCoordinator) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_state_update(self, state: GlowState) -> None: ...
