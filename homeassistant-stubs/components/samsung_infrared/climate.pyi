from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_INFRARED_EMITTER_ENTITY_ID as CONF_INFRARED_EMITTER_ENTITY_ID, SamsungDeviceType as SamsungDeviceType
from .entity import SamsungIrEntity as SamsungIrEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.climate import ATTR_FAN_MODE as ATTR_FAN_MODE, ATTR_HVAC_MODE as ATTR_HVAC_MODE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, HVACMode as HVACMode
from homeassistant.components.infrared import InfraredEmitterConsumerEntity as InfraredEmitterConsumerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import ExtraStoredData as ExtraStoredData, RestoreEntity as RestoreEntity
from typing import Any, override

PARALLEL_UPDATES: int
HA_TO_LIB_HVAC: Incomplete
HA_TO_LIB_FAN: Incomplete

@dataclass
class _SamsungAcExtraStoredData(ExtraStoredData):
    last_on_hvac_mode: str
    @override
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> _SamsungAcExtraStoredData | None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SamsungIrClimate(SamsungIrEntity, InfraredEmitterConsumerEntity, ClimateEntity, RestoreEntity):
    _attr_name: Incomplete
    _attr_assumed_state: bool
    _attr_temperature_unit: Incomplete
    _attr_fan_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_target_temperature: float
    _attr_min_temp: float
    _attr_max_temp: float
    _attr_target_temperature_step: float
    _attr_fan_mode = FAN_AUTO
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    _infrared_emitter_entity_id: Incomplete
    _device_type: Incomplete
    _last_on_hvac_mode: Incomplete
    def __init__(self, entry: ConfigEntry, infrared_emitter_entity_id: str, device_type: str) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @property
    @override
    def extra_restore_state_data(self) -> ExtraStoredData: ...
    async def _async_send_command(self) -> None: ...
    @override
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @override
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_on(self) -> None: ...
    @override
    async def async_turn_off(self) -> None: ...
