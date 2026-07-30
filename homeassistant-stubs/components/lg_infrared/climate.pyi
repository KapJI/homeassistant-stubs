from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_HVAC_MODES as CONF_HVAC_MODES, CONF_INFRARED_ENTITY_ID as CONF_INFRARED_ENTITY_ID, CONF_INFRARED_RECEIVER_ENTITY_ID as CONF_INFRARED_RECEIVER_ENTITY_ID, LGDeviceType as LGDeviceType
from .entity import LgIrEntity as LgIrEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_FAN_MODE as ATTR_FAN_MODE, ATTR_HVAC_MODE as ATTR_HVAC_MODE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, HVACMode as HVACMode
from homeassistant.components.infrared import InfraredEmitterConsumerEntity as InfraredEmitterConsumerEntity, InfraredReceivedSignal as InfraredReceivedSignal, InfraredReceiverConsumerEntity as InfraredReceiverConsumerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from infrared_protocols.commands.lg_ac import LgAcCommand, LgAcFanSpeed, LgAcMode
from typing import Any, override

PARALLEL_UPDATES: int
FAN_QUIET: str
FAN_MEDIUM_LOW: str
FAN_MEDIUM_HIGH: str
_HA_FAN_TO_LIB: dict[str, LgAcFanSpeed]
_LIB_FAN_TO_HA: dict[LgAcFanSpeed, str]
_HA_MODE_TO_LIB: dict[HVACMode, LgAcMode]
_LIB_MODE_TO_HA: dict[LgAcMode, HVACMode]
_TEMPERATURE_MODES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LgAcClimateEntity(LgIrEntity, InfraredEmitterConsumerEntity, ClimateEntity, RestoreEntity):
    _attr_name: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_target_temperature_step: float
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_should_poll: bool
    _attr_assumed_state: bool
    _attr_translation_key: str
    _attr_fan_modes: Incomplete
    _infrared_emitter_entity_id: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_target_temperature: Incomplete
    _attr_fan_mode: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, entry: ConfigEntry, emitter_entity_id: str) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @override
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    def _build_command(self, mode: LgAcMode, temp: int, fan_mode: str) -> LgAcCommand: ...

class LgAcClimateWithReceiver(LgAcClimateEntity, InfraredReceiverConsumerEntity):
    _infrared_receiver_entity_id: Incomplete
    def __init__(self, entry: ConfigEntry, emitter_entity_id: str, receiver_entity_id: str) -> None: ...
    _attr_hvac_mode: Incomplete
    _attr_fan_mode: Incomplete
    _attr_target_temperature: Incomplete
    @override
    @callback
    def _handle_signal(self, signal: InfraredReceivedSignal) -> None: ...
