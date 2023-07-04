from .discovery import MatterEntityInfo as MatterEntityInfo
from .entity import MatterEntity as MatterEntity
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters import Objects as clusters
from enum import IntEnum
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityDescription as ClimateEntityDescription, ClimateEntityFeature as ClimateEntityFeature, DEFAULT_MAX_TEMP as DEFAULT_MAX_TEMP, DEFAULT_MIN_TEMP as DEFAULT_MIN_TEMP, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, Platform as Platform, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from matter_server.client import MatterClient as MatterClient
from matter_server.client.models.node import MatterEndpoint as MatterEndpoint
from typing import Any

TEMPERATURE_SCALING_FACTOR: int
HVAC_SYSTEM_MODE_MAP: Incomplete
SystemModeEnum: Incomplete
ControlSequenceEnum: Incomplete
ThermostatFeature: Incomplete

class ThermostatRunningState(IntEnum):
    Heat: int
    Cool: int
    Fan: int
    HeatStage2: int
    CoolStage2: int
    FanStage2: int
    FanStage3: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterClimate(MatterEntity, ClimateEntity):
    _attr_temperature_unit: str
    _attr_supported_features: ClimateEntityFeature
    _attr_hvac_mode: HVACMode
    _attr_hvac_modes: Incomplete
    def __init__(self, matter_client: MatterClient, endpoint: MatterEndpoint, entity_info: MatterEntityInfo) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_hvac_action: Incomplete
    _attr_target_temperature: Incomplete
    _attr_target_temperature_high: Incomplete
    _attr_target_temperature_low: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    def _update_from_device(self) -> None: ...
    def _get_temperature_in_degrees(self, attribute: type[clusters.ClusterAttributeDescriptor]) -> float | None: ...
    @staticmethod
    def _create_optional_setpoint_command(mode: clusters.Thermostat.Enums.SetpointAdjustMode, target_temp: float, current_target_temp: float) -> clusters.Thermostat.Commands.SetpointRaiseLower | None: ...

DISCOVERY_SCHEMAS: Incomplete
