from .const import DOMAIN as DOMAIN, MASTER_THERMOSTATS as MASTER_THERMOSTATS
from .coordinator import PlugwiseConfigEntry as PlugwiseConfigEntry, PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from .entity import PlugwiseEntity as PlugwiseEntity
from .util import plugwise_command as plugwise_command
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import ExtraStoredData as ExtraStoredData, RestoreEntity as RestoreEntity
from typing import Any, override

ERROR_NO_SCHEDULE: str
PARALLEL_UPDATES: int

def _check_for_schedule(active: bool, last_active: str | None) -> None: ...

@dataclass
class PlugwiseClimateExtraStoredData(ExtraStoredData):
    last_active_schedule: str | None
    previous_action_mode: str | None
    @override
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> PlugwiseClimateExtraStoredData: ...

async def async_setup_entry(hass: HomeAssistant, entry: PlugwiseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PlugwiseClimateEntity(PlugwiseEntity, ClimateEntity, RestoreEntity):
    _attr_name: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_translation_key = DOMAIN
    _attr_unique_id: Incomplete
    _api: Incomplete
    _gateway_data: Incomplete
    _last_active_schedule: str | None
    _location: Incomplete
    _previous_action_mode: Incomplete
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_target_temperature_step: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @property
    @override
    def extra_restore_state_data(self) -> PlugwiseClimateExtraStoredData: ...
    @property
    @override
    def current_temperature(self) -> float | None: ...
    @property
    @override
    def target_temperature(self) -> float: ...
    @property
    @override
    def target_temperature_high(self) -> float: ...
    @property
    @override
    def target_temperature_low(self) -> float: ...
    @property
    @override
    def hvac_mode(self) -> HVACMode: ...
    @property
    @override
    def hvac_modes(self) -> list[HVACMode]: ...
    @property
    @override
    def hvac_action(self) -> HVACAction: ...
    @property
    @override
    def preset_mode(self) -> str | None: ...
    @plugwise_command
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    def _regulation_mode_for_hvac(self, hvac_mode: HVACMode) -> str: ...
    @plugwise_command
    @override
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @plugwise_command
    @override
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
