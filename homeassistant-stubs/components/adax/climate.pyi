from . import AdaxConfigEntry as AdaxConfigEntry
from .const import CONNECTION_TYPE as CONNECTION_TYPE, DOMAIN as DOMAIN, LOCAL as LOCAL
from .coordinator import AdaxCloudCoordinator as AdaxCloudCoordinator, AdaxLocalCoordinator as AdaxLocalCoordinator
from _typeshed import Incomplete
from adax import Adax as Adax
from adax_local import Adax as AdaxLocal
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_UNIQUE_ID as CONF_UNIQUE_ID, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: AdaxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AdaxDevice(CoordinatorEntity[AdaxCloudCoordinator], ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_max_temp: int
    _attr_min_temp: int
    _attr_supported_features: Incomplete
    _attr_target_temperature_step = PRECISION_WHOLE
    _attr_temperature_unit: Incomplete
    _adax_data_handler: Adax
    _device_id: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AdaxCloudCoordinator, device_id: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def room(self) -> dict[str, Any]: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_icon: str
    def _apply_data(self, room: dict[str, Any]) -> None: ...

class LocalAdaxDevice(CoordinatorEntity[AdaxLocalCoordinator], ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_icon: str
    _attr_max_temp: int
    _attr_min_temp: int
    _attr_supported_features: Incomplete
    _attr_target_temperature_step = PRECISION_WHOLE
    _attr_temperature_unit: Incomplete
    _adax_data_handler: AdaxLocal
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AdaxLocalCoordinator, unique_id: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_available: Incomplete
    _attr_target_temperature: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
