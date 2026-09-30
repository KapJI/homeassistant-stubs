from .coordinator import HotSpringConfigEntry as HotSpringConfigEntry, HotSpringDataUpdateCoordinator as HotSpringDataUpdateCoordinator
from .entity import HotSpringEntity as HotSpringEntity
from .helpers import hotspring_exception_handler as hotspring_exception_handler
from _typeshed import Incomplete
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
MIN_TEMP_FAHRENHEIT: float
MAX_TEMP_FAHRENHEIT: float
STEP_FAHRENHEIT: float
MIN_TEMP_CELSIUS: float
MAX_TEMP_CELSIUS: float
STEP_CELSIUS: float
TARGET_TEMPERATURE_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: HotSpringConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HotSpringNumberEntity(HotSpringEntity, NumberEntity):
    entity_description: NumberEntityDescription
    def __init__(self, coordinator: HotSpringDataUpdateCoordinator, description: NumberEntityDescription) -> None: ...
    @property
    def _is_celsius(self) -> bool: ...
    @property
    @override
    def native_unit_of_measurement(self) -> str: ...
    @property
    @override
    def native_min_value(self) -> float: ...
    @property
    @override
    def native_max_value(self) -> float: ...
    @property
    @override
    def native_step(self) -> float: ...
    @property
    @override
    def native_value(self) -> float | None: ...
    @hotspring_exception_handler
    @override
    async def async_set_native_value(self, value: float) -> None: ...
