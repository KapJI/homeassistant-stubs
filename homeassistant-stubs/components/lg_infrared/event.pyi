from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_INFRARED_RECEIVER_ENTITY_ID as CONF_INFRARED_RECEIVER_ENTITY_ID, LGDeviceType as LGDeviceType
from .entity import LgIrEntity as LgIrEntity
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity
from homeassistant.components.infrared import InfraredReceivedSignal as InfraredReceivedSignal, InfraredReceiverConsumerEntity as InfraredReceiverConsumerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from infrared_protocols.codes.lg.tv import LGTVCode
from typing import override

_LOGGER: Incomplete
PARALLEL_UPDATES: int
_COMMAND_CODE_TO_EVENT_TYPE: dict[LGTVCode, str]
_EVENT_TYPE_UNKNOWN: str
_EVENT_TYPES: list[str]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LgIrReceivedCommandEvent(LgIrEntity, InfraredReceiverConsumerEntity, EventEntity):
    _attr_translation_key: str
    _attr_event_types = _EVENT_TYPES
    _infrared_receiver_entity_id: Incomplete
    def __init__(self, entry: ConfigEntry, receiver_entity_id: str) -> None: ...
    @callback
    @override
    def _handle_signal(self, signal: InfraredReceivedSignal) -> None: ...
