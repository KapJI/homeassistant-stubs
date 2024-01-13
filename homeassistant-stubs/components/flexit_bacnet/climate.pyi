from .const import DOMAIN as DOMAIN, MAX_TEMP as MAX_TEMP, MIN_TEMP as MIN_TEMP, PRESET_TO_VENTILATION_MODE_MAP as PRESET_TO_VENTILATION_MODE_MAP, VENTILATION_TO_PRESET_MODE_MAP as VENTILATION_TO_PRESET_MODE_MAP
from _typeshed import Incomplete
from flexit_bacnet import FlexitBACnet as FlexitBACnet
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_BOOST as PRESET_BOOST, PRESET_HOME as PRESET_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_devices: AddEntitiesCallback) -> None: ...

class FlexitClimateEntity(ClimateEntity):
    _attr_name: Incomplete
    _attr_has_entity_name: bool
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_target_temperature_step = PRECISION_HALVES
    _attr_temperature_unit: Incomplete
    _attr_max_temp = MAX_TEMP
    _attr_min_temp = MIN_TEMP
    _device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device: FlexitBACnet) -> None: ...
    async def async_update(self) -> None: ...
    @property
    def current_temperature(self) -> float: ...
    @property
    def target_temperature(self) -> float: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @property
    def preset_mode(self) -> str: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
