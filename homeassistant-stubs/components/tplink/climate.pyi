from . import TPLinkConfigEntry as TPLinkConfigEntry, legacy_device_id as legacy_device_id
from .const import DOMAIN as DOMAIN, UNIT_MAPPING as UNIT_MAPPING
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkModuleEntity as CoordinatedTPLinkModuleEntity, TPLinkModuleEntityDescription as TPLinkModuleEntityDescription, async_refresh_after as async_refresh_after
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.climate import ATTR_TEMPERATURE as ATTR_TEMPERATURE, ClimateEntity as ClimateEntity, ClimateEntityDescription as ClimateEntityDescription, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.const import PRECISION_TENTHS as PRECISION_TENTHS, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from kasa import Device as Device
from typing import Any

PARALLEL_UPDATES: int
STATE_TO_ACTION: Incomplete
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class TPLinkClimateEntityDescription(ClimateEntityDescription, TPLinkModuleEntityDescription):
    unique_id_fn: Callable[[Device, TPLinkModuleEntityDescription], str] = ...

CLIMATE_DESCRIPTIONS: tuple[TPLinkClimateEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TPLinkClimateEntity(CoordinatedTPLinkModuleEntity, ClimateEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_precision = PRECISION_TENTHS
    entity_description: TPLinkClimateEntityDescription
    _thermostat_module: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_temperature_unit: Incomplete
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, description: TPLinkClimateEntityDescription, *, parent: Device) -> None: ...
    @async_refresh_after
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @async_refresh_after
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @async_refresh_after
    async def async_turn_on(self) -> None: ...
    @async_refresh_after
    async def async_turn_off(self) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_hvac_action: Incomplete
    @callback
    def _async_update_attrs(self) -> bool: ...
