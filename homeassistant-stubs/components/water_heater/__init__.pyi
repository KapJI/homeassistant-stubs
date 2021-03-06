from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from typing import Any

DEFAULT_MIN_TEMP: int
DEFAULT_MAX_TEMP: int
DOMAIN: str
ENTITY_ID_FORMAT: Any
SCAN_INTERVAL: Any
SERVICE_SET_AWAY_MODE: str
SERVICE_SET_TEMPERATURE: str
SERVICE_SET_OPERATION_MODE: str
STATE_ECO: str
STATE_ELECTRIC: str
STATE_PERFORMANCE: str
STATE_HIGH_DEMAND: str
STATE_HEAT_PUMP: str
STATE_GAS: str
SUPPORT_TARGET_TEMPERATURE: int
SUPPORT_OPERATION_MODE: int
SUPPORT_AWAY_MODE: int
ATTR_MAX_TEMP: str
ATTR_MIN_TEMP: str
ATTR_AWAY_MODE: str
ATTR_OPERATION_MODE: str
ATTR_OPERATION_LIST: str
ATTR_TARGET_TEMP_HIGH: str
ATTR_TARGET_TEMP_LOW: str
ATTR_CURRENT_TEMPERATURE: str
CONVERTIBLE_ATTRIBUTE: Any
_LOGGER: Any
ON_OFF_SERVICE_SCHEMA: Any
SET_AWAY_MODE_SCHEMA: Any
SET_TEMPERATURE_SCHEMA: Any
SET_OPERATION_MODE_SCHEMA: Any

async def async_setup(hass, config): ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class WaterHeaterEntityEntityDescription(EntityDescription): ...

class WaterHeaterEntity(Entity):
    entity_description: WaterHeaterEntityEntityDescription
    _attr_current_operation: Union[str, None]
    _attr_current_temperature: Union[float, None]
    _attr_is_away_mode_on: Union[bool, None]
    _attr_max_temp: float
    _attr_min_temp: float
    _attr_operation_list: Union[list[str], None]
    _attr_precision: float
    _attr_state: None
    _attr_supported_features: int
    _attr_target_temperature_high: Union[float, None]
    _attr_target_temperature_low: Union[float, None]
    _attr_target_temperature: Union[float, None]
    _attr_temperature_unit: str
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def precision(self) -> float: ...
    @property
    def capability_attributes(self): ...
    @property
    def state_attributes(self): ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def current_operation(self) -> Union[str, None]: ...
    @property
    def operation_list(self) -> Union[list[str], None]: ...
    @property
    def current_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature_high(self) -> Union[float, None]: ...
    @property
    def target_temperature_low(self) -> Union[float, None]: ...
    @property
    def is_away_mode_on(self) -> Union[bool, None]: ...
    def set_temperature(self, **kwargs) -> None: ...
    async def async_set_temperature(self, **kwargs) -> None: ...
    def set_operation_mode(self, operation_mode) -> None: ...
    async def async_set_operation_mode(self, operation_mode) -> None: ...
    def turn_away_mode_on(self) -> None: ...
    async def async_turn_away_mode_on(self) -> None: ...
    def turn_away_mode_off(self) -> None: ...
    async def async_turn_away_mode_off(self) -> None: ...
    @property
    def min_temp(self): ...
    @property
    def max_temp(self): ...

async def async_service_away_mode(entity, service) -> None: ...
async def async_service_temperature_set(entity, service) -> None: ...

class WaterHeaterDevice(WaterHeaterEntity):
    def __init_subclass__(cls, **kwargs) -> None: ...
