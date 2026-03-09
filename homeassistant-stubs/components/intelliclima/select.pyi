from .coordinator import IntelliClimaConfigEntry as IntelliClimaConfigEntry, IntelliClimaCoordinator as IntelliClimaCoordinator
from .entity import IntelliClimaECOEntity as IntelliClimaECOEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyintelliclima.intelliclima_types import IntelliClimaECO as IntelliClimaECO

PARALLEL_UPDATES: int
FAN_MODE_TO_INTELLICLIMA_MODE: Incomplete
INTELLICLIMA_MODE_TO_FAN_MODE: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: IntelliClimaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IntelliClimaVMCFanModeSelect(IntelliClimaECOEntity, SelectEntity):
    _attr_translation_key: str
    _attr_options: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IntelliClimaCoordinator, device: IntelliClimaECO) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
