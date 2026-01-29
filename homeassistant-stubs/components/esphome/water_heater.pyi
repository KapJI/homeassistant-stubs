from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_float_state_property as esphome_float_state_property, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, WaterHeaterInfo, WaterHeaterMode, WaterHeaterState
from homeassistant.components.water_heater import WaterHeaterEntity as WaterHeaterEntity, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_TENTHS as PRECISION_TENTHS, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import callback as callback
from typing import Any

PARALLEL_UPDATES: int
_WATER_HEATER_MODES: EsphomeEnumMapper[WaterHeaterMode, str]

class EsphomeWaterHeater(EsphomeEntity[WaterHeaterInfo, WaterHeaterState], WaterHeaterEntity):
    _attr_temperature_unit: Incomplete
    _attr_precision = PRECISION_TENTHS
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_operation_list: Incomplete
    _attr_supported_features: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    @esphome_float_state_property
    def current_temperature(self) -> float | None: ...
    @property
    @esphome_float_state_property
    def target_temperature(self) -> float | None: ...
    @property
    @esphome_state_property
    def current_operation(self) -> str | None: ...
    @convert_api_error_ha_error
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_set_operation_mode(self, operation_mode: str) -> None: ...

async_setup_entry: Incomplete
