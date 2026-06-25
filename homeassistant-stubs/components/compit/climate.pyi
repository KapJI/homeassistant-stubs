import logging
from .const import DOMAIN as DOMAIN, MANUFACTURER_NAME as MANUFACTURER_NAME
from .coordinator import CompitConfigEntry as CompitConfigEntry, CompitDataUpdateCoordinator as CompitDataUpdateCoordinator
from _typeshed import Incomplete
from compit_inext_api.consts import CompitParameter
from dataclasses import dataclass
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityDescription as ClimateEntityDescription, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, FAN_OFF as FAN_OFF, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_ECO as PRESET_ECO, PRESET_HOME as PRESET_HOME, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, override

_LOGGER: logging.Logger
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class CompitDeviceDescription(ClimateEntityDescription):
    supported_features: ClimateEntityFeature
    available_presets: list[str]
    available_fan_modes: list[str]
    available_hvac_modes: list[HVACMode]

COMPIT_MODE_MAP: Incomplete
COMPIT_FANSPEED_MAP: Incomplete
COMPIT_PRESET_MAP: Incomplete
HVAC_MODE_TO_COMPIT_MODE: Incomplete
FAN_MODE_TO_COMPIT_FAN_MODE: Incomplete
PRESET_MODE_TO_COMPIT_PRESET_MODE: Incomplete
DEVICE_DEFINITIONS: dict[int, CompitDeviceDescription]

async def async_setup_entry(hass: HomeAssistant, entry: CompitConfigEntry, async_add_devices: AddConfigEntryEntitiesCallback) -> None: ...

class CompitClimate(CoordinatorEntity[CompitDataUpdateCoordinator], ClimateEntity):
    _attr_temperature_unit: Incomplete
    _attr_name: Incomplete
    _attr_has_entity_name: bool
    entity_description: CompitDeviceDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    device_id: Incomplete
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    _attr_fan_modes: Incomplete
    _attr_hvac_modes: Incomplete
    def __init__(self, coordinator: CompitDataUpdateCoordinator, device_id: int, entity_description: CompitDeviceDescription) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def current_temperature(self) -> float | None: ...
    @property
    @override
    def target_temperature(self) -> float | None: ...
    @property
    @override
    def preset_mode(self) -> str | None: ...
    @property
    @override
    def fan_mode(self) -> str | None: ...
    @property
    @override
    def hvac_mode(self) -> HVACMode | None: ...
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @override
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @override
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @override
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def set_parameter_value(self, parameter: CompitParameter, value: int) -> None: ...
    def get_parameter_value(self, parameter: CompitParameter) -> str | float | None: ...
