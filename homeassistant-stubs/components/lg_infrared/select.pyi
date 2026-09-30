from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_INFRARED_ENTITY_ID as CONF_INFRARED_ENTITY_ID, LGDeviceType as LGDeviceType
from .entity import LgIrEntity as LgIrEntity
from _typeshed import Incomplete
from homeassistant.components.infrared import InfraredEmitterConsumerEntity as InfraredEmitterConsumerEntity
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from infrared_protocols.codes.lg.ac import LGACCode
from typing import override

PARALLEL_UPDATES: int
ENERGY_LIMIT_OFF: str
_ENERGY_LIMIT_TO_CODE: dict[str, LGACCode]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LgAcEnergyLimitSelect(LgIrEntity, InfraredEmitterConsumerEntity, SelectEntity, RestoreEntity):
    _attr_assumed_state: bool
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_options: Incomplete
    _infrared_emitter_entity_id: Incomplete
    _attr_current_option: Incomplete
    def __init__(self, entry: ConfigEntry, emitter_entity_id: str) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
