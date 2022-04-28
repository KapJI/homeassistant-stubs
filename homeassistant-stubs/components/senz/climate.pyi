from . import SENZDataUpdateCoordinator as SENZDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from aiosenz import Thermostat as Thermostat
from homeassistant.components.climate import ClimateEntity as ClimateEntity
from homeassistant.components.climate.const import ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_TENTHS as PRECISION_TENTHS, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SENZClimate(CoordinatorEntity, ClimateEntity):
    _attr_temperature_unit: Any
    _attr_precision: Any
    _attr_hvac_modes: Any
    _attr_supported_features: Any
    _attr_max_temp: int
    _attr_min_temp: int
    _thermostat: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, thermostat: Thermostat, coordinator: SENZDataUpdateCoordinator) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    @property
    def current_temperature(self) -> float: ...
    @property
    def target_temperature(self) -> float: ...
    @property
    def available(self) -> bool: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
