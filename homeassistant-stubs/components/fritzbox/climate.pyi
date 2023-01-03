from . import FritzBoxDeviceEntity as FritzBoxDeviceEntity, FritzboxDataUpdateCoordinator as FritzboxDataUpdateCoordinator
from .const import ATTR_STATE_BATTERY_LOW as ATTR_STATE_BATTERY_LOW, ATTR_STATE_HOLIDAY_MODE as ATTR_STATE_HOLIDAY_MODE, ATTR_STATE_SUMMER_MODE as ATTR_STATE_SUMMER_MODE, ATTR_STATE_WINDOW_OPEN as ATTR_STATE_WINDOW_OPEN, CONF_COORDINATOR as CONF_COORDINATOR
from .model import ClimateExtraAttributes as ClimateExtraAttributes
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

OPERATION_LIST: Incomplete
MIN_TEMPERATURE: int
MAX_TEMPERATURE: int
PRESET_MANUAL: str
ON_API_TEMPERATURE: float
OFF_API_TEMPERATURE: float
ON_REPORT_SET_TEMPERATURE: float
OFF_REPORT_SET_TEMPERATURE: float

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzboxThermostat(FritzBoxDeviceEntity, ClimateEntity):
    _attr_precision: Incomplete
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    @property
    def current_temperature(self) -> float: ...
    @property
    def target_temperature(self) -> float: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @property
    def hvac_mode(self) -> str: ...
    @property
    def hvac_modes(self) -> list[HVACMode]: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    def preset_mode(self) -> Union[str, None]: ...
    @property
    def preset_modes(self) -> list[str]: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @property
    def min_temp(self) -> int: ...
    @property
    def max_temp(self) -> int: ...
    @property
    def extra_state_attributes(self) -> ClimateExtraAttributes: ...
