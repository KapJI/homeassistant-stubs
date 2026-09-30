from .const import CONF_HVAC_MODES as CONF_HVAC_MODES, CONF_INFRARED_EMITTER_ENTITY_ID as CONF_INFRARED_EMITTER_ENTITY_ID, CONF_INFRARED_RECEIVER_ENTITY_ID as CONF_INFRARED_RECEIVER_ENTITY_ID
from .entity import GreeIrEntity as GreeIrEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.climate import ATTR_FAN_MODE as ATTR_FAN_MODE, ATTR_HVAC_MODE as ATTR_HVAC_MODE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, HVACMode as HVACMode
from homeassistant.components.infrared import InfraredEmitterConsumerEntity as InfraredEmitterConsumerEntity, InfraredReceivedSignal as InfraredReceivedSignal, InfraredReceiverConsumerEntity as InfraredReceiverConsumerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import ExtraStoredData as ExtraStoredData, RestoreEntity as RestoreEntity
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from infrared_protocols.commands.gree_ac import GreeAcCommand, GreeAcFanSpeed, GreeAcMode
from typing import Any, override

PARALLEL_UPDATES: int
_HA_FAN_TO_LIB: dict[str, GreeAcFanSpeed]
_LIB_FAN_TO_HA: dict[GreeAcFanSpeed, str]
_HA_MODE_TO_LIB: dict[HVACMode, GreeAcMode]
_LIB_MODE_TO_HA: dict[GreeAcMode, HVACMode]

@dataclass
class _GreeAcExtraStoredData(ExtraStoredData):
    last_active_hvac_mode: str
    @override
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> _GreeAcExtraStoredData | None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class GreeAcClimateEntity(GreeIrEntity, InfraredEmitterConsumerEntity, ClimateEntity, RestoreEntity):
    _attr_name: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_target_temperature_step: float
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_should_poll: bool
    _attr_assumed_state: bool
    _attr_supported_features: Incomplete
    _attr_fan_modes: Incomplete
    _infrared_emitter_entity_id: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_target_temperature: Incomplete
    _attr_fan_mode: Incomplete
    _last_active_hvac_mode: Incomplete
    def __init__(self, entry: ConfigEntry, emitter_entity_id: str) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @property
    @override
    def extra_restore_state_data(self) -> ExtraStoredData: ...
    async def _async_send_state(self, hvac_mode: HVACMode, temp: int, fan_mode: str) -> None: ...
    @override
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @override
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    def _build_command(self, hvac_mode: HVACMode, power: bool, temp: int, fan_mode: str) -> GreeAcCommand: ...

class GreeAcClimateWithReceiver(GreeAcClimateEntity, InfraredReceiverConsumerEntity):
    _infrared_receiver_entity_id: Incomplete
    def __init__(self, entry: ConfigEntry, emitter_entity_id: str, receiver_entity_id: str) -> None: ...
    _last_active_hvac_mode: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_fan_mode: Incomplete
    _attr_target_temperature: Incomplete
    @override
    @callback
    def _handle_signal(self, signal: InfraredReceivedSignal) -> None: ...
