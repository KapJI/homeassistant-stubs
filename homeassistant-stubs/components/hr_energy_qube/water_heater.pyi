from . import QubeConfigEntry as QubeConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import QubeCoordinator as QubeCoordinator
from .entity import QubeEntity as QubeEntity
from _typeshed import Incomplete
from homeassistant.components.water_heater import STATE_HEAT_PUMP as STATE_HEAT_PUMP, STATE_PERFORMANCE as STATE_PERFORMANCE, WaterHeaterEntity as WaterHeaterEntity, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
DHW_BOOST_KEY: str
DHW_SETPOINT_KEY: str
DHW_MIN_TEMP: int
DHW_MAX_TEMP: int
OPERATION_MODES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: QubeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class QubeWaterHeater(QubeEntity, WaterHeaterEntity):
    _attr_temperature_unit: Incomplete
    _attr_min_temp = DHW_MIN_TEMP
    _attr_max_temp = DHW_MAX_TEMP
    _attr_operation_list = OPERATION_MODES
    _attr_supported_features: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: QubeCoordinator, entry: QubeConfigEntry) -> None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def current_operation(self) -> str | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_operation_mode(self, operation_mode: str) -> None: ...
