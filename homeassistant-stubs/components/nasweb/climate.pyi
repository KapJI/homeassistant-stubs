from . import NASwebConfigEntry as NASwebConfigEntry
from .const import DOMAIN as DOMAIN, STATUS_UPDATE_MAX_TIME_INTERVAL as STATUS_UPDATE_MAX_TIME_INTERVAL
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, UnitOfTemperature as UnitOfTemperature
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import BaseCoordinatorEntity as BaseCoordinatorEntity, BaseDataUpdateCoordinatorProtocol as BaseDataUpdateCoordinatorProtocol
from typing import Any
from webio_api import Thermostat as NASwebThermostat

CLIMATE_TRANSLATION_KEY: str

async def async_setup_entry(hass: HomeAssistant, config: NASwebConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class Thermostat(ClimateEntity, BaseCoordinatorEntity):
    _attr_device_class: Incomplete
    _attr_has_entity_name: bool
    _attr_hvac_modes: Incomplete
    _attr_max_temp: int
    _attr_min_temp: int
    _attr_precision: float
    _attr_should_poll: bool
    _attr_supported_features: Incomplete
    _attr_target_temperature_step: float
    _attr_temperature_unit: Incomplete
    _attr_translation_key = CLIMATE_TRANSLATION_KEY
    _thermostat: Incomplete
    _attr_available: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: BaseDataUpdateCoordinatorProtocol, nasweb_thermostat: NASwebThermostat) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _set_attr_available(self, entity_last_update: float, available: bool | None) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_target_temperature_low: Incomplete
    _attr_target_temperature_high: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_hvac_action: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
    def _get_current_hvac_mode(self) -> HVACMode: ...
    def _get_current_action(self) -> HVACAction: ...
    async def async_update(self) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
