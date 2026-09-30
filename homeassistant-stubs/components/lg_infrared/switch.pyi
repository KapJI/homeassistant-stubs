from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_INFRARED_ENTITY_ID as CONF_INFRARED_ENTITY_ID, LGDeviceType as LGDeviceType
from .entity import LgIrEntity as LgIrEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.infrared import InfraredEmitterConsumerEntity as InfraredEmitterConsumerEntity
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from infrared_protocols.codes.lg.ac import LGACCode
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LgAcSwitchEntityDescription(SwitchEntityDescription):
    on_code: LGACCode
    off_code: LGACCode

AC_SWITCH_DESCRIPTIONS: tuple[LgAcSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LgAcSwitch(LgIrEntity, InfraredEmitterConsumerEntity, SwitchEntity, RestoreEntity):
    _attr_assumed_state: bool
    entity_description: LgAcSwitchEntityDescription
    _infrared_emitter_entity_id: Incomplete
    _attr_is_on: bool
    def __init__(self, entry: ConfigEntry, emitter_entity_id: str, description: LgAcSwitchEntityDescription) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
