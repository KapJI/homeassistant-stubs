from .const import BinarySensorType as BinarySensorType, DHW_TEMP as DHW_TEMP, DOMAIN as DOMAIN, LOWER_BOUND as LOWER_BOUND, UPPER_BOUND as UPPER_BOUND, WaterHeaterType as WaterHeaterType
from .coordinator import PlugwiseConfigEntry as PlugwiseConfigEntry, PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from .entity import PlugwiseEntity as PlugwiseEntity
from .util import plugwise_command as plugwise_command
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.water_heater import STATE_GAS as STATE_GAS, STATE_HEAT_PUMP as STATE_HEAT_PUMP, WaterHeaterEntity as WaterHeaterEntity, WaterHeaterEntityDescription as WaterHeaterEntityDescription, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, STATE_OFF as STATE_OFF, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from typing import Any, Final, override

PARALLEL_UPDATES: int
FAIL_SET_TEMP: Final[str]
OPERATION_LIST: Final[list[str]]

@dataclass(frozen=True, kw_only=True)
class PlugwiseWaterHeaterEntityDescription(WaterHeaterEntityDescription):
    key: WaterHeaterType
    state_key: BinarySensorType

WATERHEATER_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PlugwiseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PlugwiseWaterHeaterEntity(PlugwiseEntity, WaterHeaterEntity):
    entity_description: PlugwiseWaterHeaterEntityDescription
    _attr_max_temp: Incomplete
    _attr_min_temp: Incomplete
    _attr_operation_list: Incomplete
    _attr_supported_features: Incomplete
    _attr_target_temperature_step: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str, description: PlugwiseWaterHeaterEntityDescription) -> None: ...
    @property
    @override
    def current_operation(self) -> str: ...
    @property
    @override
    def current_temperature(self) -> float | None: ...
    @property
    @override
    def target_temperature(self) -> float | None: ...
    @plugwise_command
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
