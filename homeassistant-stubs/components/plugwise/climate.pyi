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
from typing import Any

ERROR_NO_SCHEDULE: str
PARALLEL_UPDATES: int

@dataclass
class PlugwiseClimateExtraStoredData(ExtraStoredData):
    last_active_schedule: str | None
    previous_action_mode: str | None
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> PlugwiseClimateExtraStoredData: ...

async def async_setup_entry(hass: HomeAssistant, entry: PlugwiseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PlugwiseClimateEntity(PlugwiseEntity, ClimateEntity, RestoreEntity):
    _attr_name: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_translation_key = DOMAIN
    _last_active_schedule: str | None
    _previous_action_mode: str | None
    async def async_added_to_hass(self) -> None: ...
    _attr_unique_id: Incomplete
    _gateway_data: Incomplete
    _location: Incomplete
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_target_temperature_step: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str) -> None: ...
    @property
    def current_temperature(self) -> float: ...
    @property
    def extra_restore_state_data(self) -> PlugwiseClimateExtraStoredData: ...
    @property
    def target_temperature(self) -> float: ...
    @property
    def target_temperature_high(self) -> float: ...
    @property
    def target_temperature_low(self) -> float: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_modes(self) -> list[HVACMode]: ...
    @property
    def hvac_action(self) -> HVACAction: ...
    @property
    def preset_mode(self) -> str | None: ...
    @plugwise_command
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @plugwise_command
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @plugwise_command
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
