from . import get_hub as get_hub
from .base_platform import BaseStructPlatform as BaseStructPlatform
from .const import CALL_TYPE_REGISTER_HOLDING as CALL_TYPE_REGISTER_HOLDING, CALL_TYPE_WRITE_REGISTER as CALL_TYPE_WRITE_REGISTER, CALL_TYPE_WRITE_REGISTERS as CALL_TYPE_WRITE_REGISTERS, CONF_CLIMATES as CONF_CLIMATES, CONF_MAX_TEMP as CONF_MAX_TEMP, CONF_MIN_TEMP as CONF_MIN_TEMP, CONF_STEP as CONF_STEP, CONF_TARGET_TEMP as CONF_TARGET_TEMP, DataType as DataType
from .modbus import ModbusHub as ModbusHub
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.climate import ClimateEntity as ClimateEntity
from homeassistant.components.climate.const import ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_NAME as CONF_NAME, CONF_TEMPERATURE_UNIT as CONF_TEMPERATURE_UNIT, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class ModbusThermostat(BaseStructPlatform, RestoreEntity, ClimateEntity):
    _attr_hvac_mode: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    _target_temperature_register: Incomplete
    _unit: Incomplete
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_precision: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_target_temperature_step: Incomplete
    def __init__(self, hub: ModbusHub, config: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    _attr_available: Incomplete
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    _call_active: bool
    async def async_update(self, now: Union[datetime, None] = ...) -> None: ...
    _lazy_errors: Incomplete
    _value: Incomplete
    async def _async_read_register(self, register_type: str, register: int) -> Union[float, None]: ...
