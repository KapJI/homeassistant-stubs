from .const import ATTR_LOCKED as ATTR_LOCKED, ATTR_OFFSET as ATTR_OFFSET, ATTR_VALVE as ATTR_VALVE
from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import DeconzGateway as DeconzGateway, get_gateway_from_config_entry as get_gateway_from_config_entry
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, DOMAIN as DOMAIN
from homeassistant.components.climate.const import ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, FAN_OFF as FAN_OFF, FAN_ON as FAN_ON, HVACMode as HVACMode, PRESET_BOOST as PRESET_BOOST, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.models.sensor.thermostat import Thermostat
from typing import Any

DECONZ_FAN_SMART: str
FAN_MODE_TO_DECONZ: Incomplete
DECONZ_TO_FAN_MODE: Incomplete
HVAC_MODE_TO_DECONZ: dict[HVACMode, str]
DECONZ_PRESET_AUTO: str
DECONZ_PRESET_COMPLEX: str
DECONZ_PRESET_HOLIDAY: str
DECONZ_PRESET_MANUAL: str
PRESET_MODE_TO_DECONZ: Incomplete
DECONZ_TO_PRESET_MODE: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzThermostat(DeconzDevice, ClimateEntity):
    TYPE: Incomplete
    _device: Thermostat
    _attr_temperature_unit: Incomplete
    _attr_hvac_modes: Incomplete
    _deconz_to_hvac_mode: Incomplete
    _attr_supported_features: Incomplete
    _attr_fan_modes: Incomplete
    _attr_preset_modes: Incomplete
    def __init__(self, device: Thermostat, gateway: DeconzGateway) -> None: ...
    @property
    def fan_mode(self) -> str: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    def preset_mode(self) -> Union[str, None]: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @property
    def current_temperature(self) -> float: ...
    @property
    def target_temperature(self) -> Union[float, None]: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Union[bool, int]]: ...
