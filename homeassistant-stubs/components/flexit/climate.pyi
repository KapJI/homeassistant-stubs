from . import FlexitConfigEntry as FlexitConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import FlexitDataCoordinator as FlexitDataCoordinator
from .entity import FlexitEntity as FlexitEntity
from _typeshed import Incomplete
from flexit_modbus import MAX_TEMPERATURE, MIN_TEMPERATURE
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.components.modbus import ModbusHub as ModbusHub, get_hub as get_hub
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_NAME as CONF_NAME, CONF_SLAVE as CONF_SLAVE, DEVICE_DEFAULT_NAME as DEVICE_DEFAULT_NAME, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, override

_LOGGER: Incomplete
PARALLEL_UPDATES: int
CALL_TYPE_REGISTER_HOLDING: str
CALL_TYPE_REGISTER_INPUT: str
CALL_TYPE_WRITE_REGISTER: str
DEFAULT_HUB: str
CONF_HUB: str
PLATFORM_SCHEMA: Incomplete
FLEXIT_TO_HA_FAN_MODE: Incomplete
HA_TO_FLEXIT_FAN_MODE: Incomplete
FLEXIT_TO_HA_HVAC_ACTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: FlexitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class Flexit(ClimateEntity):
    _attr_fan_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _hub: Incomplete
    _attr_name: Incomplete
    _slave: Incomplete
    _attr_fan_mode: Incomplete
    _filter_hours: int | None
    _filter_alarm: int | None
    _heat_recovery: int | None
    _heater_enabled: int | None
    _heating: int | None
    _cooling: int | None
    _alarm: bool
    _outdoor_air_temp: float | None
    def __init__(self, hub: ModbusHub, modbus_slave: int | None, name: str | None) -> None: ...
    _attr_target_temperature: Incomplete
    _attr_current_temperature: Incomplete
    _attr_hvac_action: Incomplete
    async def async_update(self) -> None: ...
    @property
    @override
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @override
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def _async_read_int16_from_register(self, register_type: str, register: int) -> int: ...
    async def _async_read_temp_from_register(self, register_type: str, register: int) -> float: ...
    async def _async_write_int16_to_register(self, register: int, value: int) -> bool: ...

class FlexitClimate(FlexitEntity, ClimateEntity):
    _attr_name: Incomplete
    _attr_fan_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_min_temp = MIN_TEMPERATURE
    _attr_max_temp = MAX_TEMPERATURE
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FlexitDataCoordinator) -> None: ...
    @override
    def _handle_coordinator_update(self) -> None: ...
    _attr_target_temperature: Incomplete
    _attr_current_temperature: Incomplete
    _attr_fan_mode: Incomplete
    _attr_hvac_action: Incomplete
    def _set_attr(self) -> None: ...
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @override
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
