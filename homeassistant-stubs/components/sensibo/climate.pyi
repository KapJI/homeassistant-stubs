from .const import DOMAIN as DOMAIN
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity, async_handle_api_call as async_handle_api_call
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_STATE as ATTR_STATE, ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_TENTHS as PRECISION_TENTHS, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from typing import Any

SERVICE_ASSUME_STATE: str
SERVICE_ENABLE_TIMER: str
ATTR_MINUTES: str
SERVICE_ENABLE_PURE_BOOST: str
SERVICE_DISABLE_PURE_BOOST: str
ATTR_AC_INTEGRATION: str
ATTR_GEO_INTEGRATION: str
ATTR_INDOOR_INTEGRATION: str
ATTR_OUTDOOR_INTEGRATION: str
ATTR_SENSITIVITY: str
BOOST_INCLUSIVE: str
PARALLEL_UPDATES: int
FIELD_TO_FLAG: Incomplete
SENSIBO_TO_HA: Incomplete
HA_TO_SENSIBO: Incomplete
AC_STATE_TO_DATA: Incomplete

def _find_valid_target_temp(target: int, valid_targets: list[int]) -> int: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensiboClimate(SensiboDeviceBaseEntity, ClimateEntity):
    _attr_unique_id: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_supported_features: Incomplete
    _attr_precision: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str) -> None: ...
    def get_features(self) -> int: ...
    @property
    def current_humidity(self) -> Union[int, None]: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_modes(self) -> list[HVACMode]: ...
    @property
    def current_temperature(self) -> Union[float, None]: ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def target_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature_step(self) -> Union[float, None]: ...
    @property
    def fan_mode(self) -> Union[str, None]: ...
    @property
    def fan_modes(self) -> Union[list[str], None]: ...
    @property
    def swing_mode(self) -> Union[str, None]: ...
    @property
    def swing_modes(self) -> Union[list[str], None]: ...
    @property
    def min_temp(self) -> float: ...
    @property
    def max_temp(self) -> float: ...
    @property
    def available(self) -> bool: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_assume_state(self, state: str) -> None: ...
    async def async_enable_timer(self, minutes: int) -> None: ...
    async def async_enable_pure_boost(self, ac_integration: Union[bool, None] = ..., geo_integration: Union[bool, None] = ..., indoor_integration: Union[bool, None] = ..., outdoor_integration: Union[bool, None] = ..., sensitivity: Union[str, None] = ...) -> None: ...
    async def async_send_api_call(self, key: str, value: Any, name: str, assumed_state: bool = ...) -> bool: ...
    async def api_call_custom_service_timer(self, key: str, value: Any, data: dict) -> bool: ...
    async def api_call_custom_service_pure_boost(self, key: str, value: Any, data: dict) -> bool: ...
