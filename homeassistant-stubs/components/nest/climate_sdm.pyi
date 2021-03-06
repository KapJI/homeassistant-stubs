from .const import DATA_SUBSCRIBER as DATA_SUBSCRIBER, DOMAIN as DOMAIN
from .device_info import NestDeviceInfo as NestDeviceInfo
from google_nest_sdm.device import Device as Device
from google_nest_sdm.thermostat_traits import ThermostatHeatCoolTrait as ThermostatHeatCoolTrait
from homeassistant.components.climate import ClimateEntity as ClimateEntity
from homeassistant.components.climate.const import ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, CURRENT_HVAC_COOL as CURRENT_HVAC_COOL, CURRENT_HVAC_HEAT as CURRENT_HVAC_HEAT, CURRENT_HVAC_OFF as CURRENT_HVAC_OFF, FAN_OFF as FAN_OFF, FAN_ON as FAN_ON, HVAC_MODE_AUTO as HVAC_MODE_AUTO, HVAC_MODE_COOL as HVAC_MODE_COOL, HVAC_MODE_FAN_ONLY as HVAC_MODE_FAN_ONLY, HVAC_MODE_HEAT as HVAC_MODE_HEAT, HVAC_MODE_HEAT_COOL as HVAC_MODE_HEAT_COOL, HVAC_MODE_OFF as HVAC_MODE_OFF, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE, SUPPORT_FAN_MODE as SUPPORT_FAN_MODE, SUPPORT_PRESET_MODE as SUPPORT_PRESET_MODE, SUPPORT_TARGET_TEMPERATURE as SUPPORT_TARGET_TEMPERATURE, SUPPORT_TARGET_TEMPERATURE_RANGE as SUPPORT_TARGET_TEMPERATURE_RANGE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

THERMOSTAT_MODE_MAP: dict[str, str]
THERMOSTAT_INV_MODE_MAP: Any
THERMOSTAT_ECO_MODE: str
THERMOSTAT_HVAC_STATUS_MAP: Any
THERMOSTAT_RANGE_MODES: Any
PRESET_MODE_MAP: Any
PRESET_INV_MODE_MAP: Any
FAN_MODE_MAP: Any
FAN_INV_MODE_MAP: Any
MAX_FAN_DURATION: int

async def async_setup_sdm_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ThermostatEntity(ClimateEntity):
    _device: Any
    _device_info: Any
    _supported_features: int
    def __init__(self, device: Device) -> None: ...
    @property
    def should_poll(self) -> bool: ...
    @property
    def unique_id(self) -> Union[str, None]: ...
    @property
    def name(self) -> Union[str, None]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def current_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature_high(self) -> Union[float, None]: ...
    @property
    def target_temperature_low(self) -> Union[float, None]: ...
    @property
    def _target_temperature_trait(self) -> Union[ThermostatHeatCoolTrait, None]: ...
    @property
    def hvac_mode(self) -> str: ...
    @property
    def hvac_modes(self) -> list[str]: ...
    @property
    def _get_device_hvac_modes(self) -> set[str]: ...
    @property
    def hvac_action(self) -> Union[str, None]: ...
    @property
    def preset_mode(self) -> str: ...
    @property
    def preset_modes(self) -> list[str]: ...
    @property
    def fan_mode(self) -> str: ...
    @property
    def fan_modes(self) -> list[str]: ...
    @property
    def supported_features(self) -> int: ...
    def _get_supported_features(self) -> int: ...
    async def async_set_hvac_mode(self, hvac_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
