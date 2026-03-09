from . import VeluxConfigEntry as VeluxConfigEntry
from .entity import VeluxEntity as VeluxEntity, wrap_pyvlx_call_exceptions as wrap_pyvlx_call_exceptions
from _typeshed import Incomplete
from homeassistant.components.number import NumberEntity as NumberEntity
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyvlx import ExteriorHeating

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: VeluxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VeluxExteriorHeatingNumber(VeluxEntity, NumberEntity):
    _attr_native_min_value: int
    _attr_native_max_value: int
    _attr_native_step: int
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_name: Incomplete
    node: ExteriorHeating
    @property
    def native_value(self) -> float | None: ...
    @wrap_pyvlx_call_exceptions
    async def async_set_native_value(self, value: float) -> None: ...
