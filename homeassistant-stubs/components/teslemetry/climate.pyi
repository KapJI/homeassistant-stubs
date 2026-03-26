from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .const import DOMAIN as DOMAIN, TeslemetryClimateSide as TeslemetryClimateSide
from .entity import TeslemetryRootEntity as TeslemetryRootEntity, TeslemetryVehiclePollingEntity as TeslemetryVehiclePollingEntity, TeslemetryVehicleStreamEntity as TeslemetryVehicleStreamEntity
from .helpers import handle_vehicle_command as handle_vehicle_command
from .models import TeslemetryVehicleData as TeslemetryVehicleData
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, HVAC_MODES as HVAC_MODES
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from tesla_fleet_api.const import Scope
from tesla_fleet_api.teslemetry import Vehicle as Vehicle
from typing import Any

DEFAULT_MIN_TEMP: int
DEFAULT_MAX_TEMP: int
COP_TEMPERATURES: Incomplete
PRESET_MODES: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: TeslemetryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TeslemetryClimateEntity(TeslemetryRootEntity, ClimateEntity):
    api: Vehicle
    _attr_precision = PRECISION_HALVES
    _attr_temperature_unit: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_fan_modes: Incomplete
    _enable_turn_on_off_backwards_compatibility: bool
    _attr_hvac_mode: Incomplete
    async def async_turn_on(self) -> None: ...
    _attr_preset_mode: Incomplete
    _attr_fan_mode: Incomplete
    async def async_turn_off(self) -> None: ...
    _attr_target_temperature: Incomplete
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...

class TeslemetryVehiclePollingClimateEntity(TeslemetryClimateEntity, TeslemetryVehiclePollingEntity):
    _attr_supported_features: Incomplete
    scoped: Incomplete
    def __init__(self, data: TeslemetryVehicleData, side: TeslemetryClimateSide, scopes: list[Scope]) -> None: ...
    _attr_hvac_mode: Incomplete
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_preset_mode: Incomplete
    _attr_fan_mode: str
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingClimateEntity(TeslemetryClimateEntity, TeslemetryVehicleStreamEntity, RestoreEntity):
    _attr_supported_features: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_fan_mode: Incomplete
    _attr_preset_mode: Incomplete
    scoped: Incomplete
    side: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    rhd: bool
    def __init__(self, data: TeslemetryVehicleData, side: TeslemetryClimateSide, scopes: list[Scope]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _async_handle_inside_temp(self, data: float | None) -> None: ...
    def _async_handle_hvac_power(self, data: str | None) -> None: ...
    def _async_handle_climate_keeper_mode(self, data: str | None) -> None: ...
    def _async_handle_hvac_temperature_request(self, data: float | None) -> None: ...
    def _async_handle_rhd(self, data: bool | None) -> None: ...

COP_MODES: Incomplete
COP_LEVELS: Incomplete

class TeslemetryCabinOverheatProtectionEntity(TeslemetryRootEntity, ClimateEntity):
    api: Vehicle
    _attr_precision = PRECISION_WHOLE
    _attr_target_temperature_step: int
    _attr_min_temp: int
    _attr_max_temp: int
    _attr_temperature_unit: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_entity_registry_enabled_default: bool
    _enable_turn_on_off_backwards_compatibility: bool
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    _attr_target_temperature: Incomplete
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    _attr_hvac_mode: Incomplete
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...

class TeslemetryVehiclePollingCabinOverheatProtectionEntity(TeslemetryVehiclePollingEntity, TeslemetryCabinOverheatProtectionEntity):
    _attr_supported_features: Incomplete
    scoped: Incomplete
    def __init__(self, data: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    _attr_hvac_mode: Incomplete
    _attr_target_temperature: Incomplete
    _attr_current_temperature: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingCabinOverheatProtectionEntity(TeslemetryVehicleStreamEntity, TeslemetryCabinOverheatProtectionEntity, RestoreEntity):
    _attr_hvac_mode: Incomplete
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_fan_mode: Incomplete
    _attr_preset_mode: Incomplete
    _attr_supported_features: Incomplete
    scoped: Incomplete
    def __init__(self, data: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _async_handle_inside_temp(self, value: float | None) -> None: ...
    def _async_handle_protection_mode(self, value: str | None) -> None: ...
    def _async_handle_temperature_limit(self, value: str | None) -> None: ...
