from .const import CONFIG_STEAMER as CONFIG_STEAMER, CONFIG_STEAMER_AND_LIGHT as CONFIG_STEAMER_AND_LIGHT
from .coordinator import HuumConfigEntry as HuumConfigEntry, HuumDataUpdateCoordinator as HuumDataUpdateCoordinator
from .entity import HuumBaseEntity as HuumBaseEntity
from _typeshed import Incomplete
from homeassistant.components.number import NumberEntity as NumberEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: HuumConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HuumSteamer(HuumBaseEntity, NumberEntity):
    _attr_translation_key: str
    _attr_native_max_value: int
    _attr_native_min_value: int
    _attr_native_step: int
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: HuumDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
