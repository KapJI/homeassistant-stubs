from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, NOT_CALIBRATED_ISSUE_ID as NOT_CALIBRATED_ISSUE_ID, SHTRV_01_TEMPERATURE_SETTINGS as SHTRV_01_TEMPERATURE_SETTINGS
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, get_entry_data as get_entry_data
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_NONE as PRESET_NONE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry, async_entries_for_config_entry as async_entries_for_config_entry
from homeassistant.helpers.restore_state import ExtraStoredData as ExtraStoredData, RestoreEntity as RestoreEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from homeassistant.util.unit_system import US_CUSTOMARY_SYSTEM as US_CUSTOMARY_SYSTEM
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def async_setup_climate_entities(async_add_entities: AddEntitiesCallback, coordinator: ShellyBlockCoordinator) -> None: ...
def async_restore_climate_entities(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, coordinator: ShellyBlockCoordinator) -> None: ...

class ShellyClimateExtraStoredData(ExtraStoredData):
    last_target_temp: float | None
    def as_dict(self) -> dict[str, Any]: ...
    def __init__(self, last_target_temp) -> None: ...
    def __mypy-replace(*, last_target_temp) -> None: ...

class BlockSleepingClimate(CoordinatorEntity[ShellyBlockCoordinator], RestoreEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_icon: str
    _attr_max_temp: Incomplete
    _attr_min_temp: Incomplete
    _attr_supported_features: Incomplete
    _attr_target_temperature_step: Incomplete
    _attr_temperature_unit: Incomplete
    block: Incomplete
    control_result: Incomplete
    device_block: Incomplete
    last_state: Incomplete
    last_state_attributes: Incomplete
    _preset_modes: Incomplete
    _last_target_temp: Incomplete
    _unique_id: Incomplete
    _channel: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, sensor_block: Block | None, device_block: Block | None, entry: RegistryEntry | None = ...) -> None: ...
    @property
    def extra_restore_state_data(self) -> ShellyClimateExtraStoredData: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def name(self) -> str: ...
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
    @property
    def device_info(self) -> DeviceInfo: ...
    def _check_is_off(self) -> bool: ...
    async def set_state_full_path(self, **kwargs: Any) -> Any: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
