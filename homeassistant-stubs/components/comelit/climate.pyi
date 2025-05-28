from .const import PRESET_MODE_AUTO as PRESET_MODE_AUTO, PRESET_MODE_AUTO_TARGET_TEMP as PRESET_MODE_AUTO_TARGET_TEMP, PRESET_MODE_MANUAL as PRESET_MODE_MANUAL
from .coordinator import ComelitConfigEntry as ComelitConfigEntry, ComelitSerialBridge as ComelitSerialBridge
from .entity import ComelitBridgeBaseEntity as ComelitBridgeBaseEntity
from .utils import bridge_api_call as bridge_api_call, cleanup_stale_entity as cleanup_stale_entity, load_api_data as load_api_data
from _typeshed import Incomplete
from aiocomelit import ComelitSerialBridgeObject as ComelitSerialBridgeObject
from enum import StrEnum
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, UnitOfTemperature as UnitOfTemperature
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_TENTHS as PRECISION_TENTHS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, TypedDict

PARALLEL_UPDATES: int

class ClimaComelitMode(StrEnum):
    AUTO = 'A'
    OFF = 'O'
    LOWER = 'L'
    UPPER = 'U'

class ClimaComelitCommand(StrEnum):
    AUTO = 'auto'
    MANUAL = 'man'
    OFF = 'off'
    ON = 'on'
    SET = 'set'
    SNOW = 'lower'
    SUN = 'upper'

class ClimaComelitApiStatus(TypedDict):
    hvac_mode: HVACMode
    hvac_action: HVACAction

API_STATUS: dict[str, ClimaComelitApiStatus]
HVACMODE_TO_ACTION: dict[HVACMode, ClimaComelitCommand]
PRESET_MODE_TO_ACTION: dict[str, ClimaComelitCommand]

async def async_setup_entry(hass: HomeAssistant, config_entry: ComelitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ComelitClimateEntity(ComelitBridgeBaseEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_max_temp: int
    _attr_min_temp: int
    _attr_supported_features: Incomplete
    _attr_target_temperature_step = PRECISION_TENTHS
    _attr_temperature_unit: Incomplete
    _attr_name: Incomplete
    _attr_translation_key: str
    def __init__(self, coordinator: ComelitSerialBridge, device: ComelitSerialBridgeObject, config_entry_entry_id: str) -> None: ...
    _attr_preset_mode: Incomplete
    _attr_current_temperature: Incomplete
    _attr_hvac_action: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_target_temperature: Incomplete
    def _update_attributes(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @bridge_api_call
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @bridge_api_call
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
