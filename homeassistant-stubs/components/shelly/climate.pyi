from .const import BLU_TRV_TEMPERATURE_SETTINGS as BLU_TRV_TEMPERATURE_SETTINGS, DOMAIN as DOMAIN, LOGGER as LOGGER, NOT_CALIBRATED_ISSUE_ID as NOT_CALIBRATED_ISSUE_ID, RPC_THERMOSTAT_SETTINGS as RPC_THERMOSTAT_SETTINGS, SHTRV_01_TEMPERATURE_SETTINGS as SHTRV_01_TEMPERATURE_SETTINGS
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import ShellyRpcEntity as ShellyRpcEntity, get_entity_block_device_info as get_entity_block_device_info, rpc_call as rpc_call
from .utils import async_remove_shelly_entity as async_remove_shelly_entity, get_block_entity_name as get_block_entity_name, get_blu_trv_device_info as get_blu_trv_device_info, get_device_entry_gen as get_device_entry_gen, get_rpc_key_ids as get_rpc_key_ids, is_rpc_thermostat_internal_actuator as is_rpc_thermostat_internal_actuator
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from collections.abc import Mapping
from dataclasses import dataclass
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from homeassistant.helpers.restore_state import ExtraStoredData as ExtraStoredData, RestoreEntity as RestoreEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from homeassistant.util.unit_system import US_CUSTOMARY_SYSTEM as US_CUSTOMARY_SYSTEM
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def async_setup_climate_entities(async_add_entities: AddConfigEntryEntitiesCallback, coordinator: ShellyBlockCoordinator) -> None: ...
@callback
def async_restore_climate_entities(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, coordinator: ShellyBlockCoordinator) -> None: ...
@callback
def async_setup_rpc_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

@dataclass
class ShellyClimateExtraStoredData(ExtraStoredData):
    last_target_temp: float | None = ...
    def as_dict(self) -> dict[str, Any]: ...

class BlockSleepingClimate(CoordinatorEntity[ShellyBlockCoordinator], RestoreEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_max_temp: Incomplete
    _attr_min_temp: Incomplete
    _attr_supported_features: Incomplete
    _attr_target_temperature_step: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_has_entity_name: bool
    block: Block | None
    control_result: dict[str, Any] | None
    device_block: Block | None
    last_state: State | None
    last_state_attributes: Mapping[str, Any]
    _preset_modes: list[str]
    _last_target_temp: Incomplete
    _unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_name: Incomplete
    _channel: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, sensor_block: Block | None, device_block: Block | None, entry: RegistryEntry | None = None) -> None: ...
    @property
    def extra_restore_state_data(self) -> ShellyClimateExtraStoredData: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def available(self) -> bool: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def preset_mode(self) -> str | None: ...
    @property
    def hvac_action(self) -> HVACAction: ...
    @property
    def preset_modes(self) -> list[str]: ...
    def _check_is_off(self) -> bool: ...
    async def set_state_full_path(self, **kwargs: Any) -> Any: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...

class RpcClimate(ShellyRpcEntity, ClimateEntity):
    _attr_max_temp: Incomplete
    _attr_min_temp: Incomplete
    _attr_supported_features: Incomplete
    _attr_target_temperature_step: Incomplete
    _attr_temperature_unit: Incomplete
    _id: Incomplete
    _thermostat_type: Incomplete
    _attr_hvac_modes: Incomplete
    _humidity_key: str | None
    def __init__(self, coordinator: ShellyRpcCoordinator, id_: int) -> None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def current_humidity(self) -> float | None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_action(self) -> HVACAction: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...

class RpcBluTrvClimate(ShellyRpcEntity, ClimateEntity):
    _attr_max_temp: Incomplete
    _attr_min_temp: Incomplete
    _attr_supported_features: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_target_temperature_step: Incomplete
    _attr_temperature_unit: Incomplete
    _id: Incomplete
    _config: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, id_: int) -> None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def hvac_action(self) -> HVACAction: ...
    @rpc_call
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
