from . import SENZConfigEntry as SENZConfigEntry, SENZDataUpdateCoordinator as SENZDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_TENTHS as PRECISION_TENTHS, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pysenz import Thermostat as Thermostat
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: SENZConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SENZClimate(CoordinatorEntity[SENZDataUpdateCoordinator], ClimateEntity):
    _attr_temperature_unit: Incomplete
    _attr_precision = PRECISION_TENTHS
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_max_temp: int
    _attr_min_temp: int
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _thermostat: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, thermostat: Thermostat, coordinator: SENZDataUpdateCoordinator) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def current_temperature(self) -> float: ...
    @property
    def target_temperature(self) -> float: ...
    @property
    def available(self) -> bool: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_action(self) -> HVACAction: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
