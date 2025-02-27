from .coordinator import PeblarConfigEntry as PeblarConfigEntry, PeblarDataUpdateCoordinator as PeblarDataUpdateCoordinator
from .entity import PeblarEntity as PeblarEntity
from .helpers import peblar_exception_handler as peblar_exception_handler
from _typeshed import Incomplete
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntityDescription as NumberEntityDescription, RestoreNumber as RestoreNumber
from homeassistant.const import EntityCategory as EntityCategory, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfElectricCurrent as UnitOfElectricCurrent
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: PeblarConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PeblarChargeCurrentLimitNumberEntity(PeblarEntity[PeblarDataUpdateCoordinator], RestoreNumber):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_native_min_value: int
    _attr_native_step: int
    _attr_native_unit_of_measurement: Incomplete
    _attr_translation_key: str
    _attr_native_max_value: Incomplete
    def __init__(self, entry: PeblarConfigEntry, coordinator: PeblarDataUpdateCoordinator) -> None: ...
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @peblar_exception_handler
    async def async_set_native_value(self, value: float) -> None: ...
