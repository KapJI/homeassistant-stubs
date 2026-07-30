from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_INFRARED_RECEIVER_ENTITY_ID as CONF_INFRARED_RECEIVER_ENTITY_ID, LEDIrDeviceType as LEDIrDeviceType
from .entity import LEDIrBaseEntity as LEDIrBaseEntity
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity
from homeassistant.components.infrared import InfraredReceivedSignal as InfraredReceivedSignal, InfraredReceiverConsumerEntity as InfraredReceiverConsumerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LEDIrEventEntity(LEDIrBaseEntity, InfraredReceiverConsumerEntity, EventEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _infrared_receiver_entity_id: Incomplete
    _attr_event_types: Incomplete
    def __init__(self, entry: ConfigEntry, device_type: LEDIrDeviceType, receiver_entity_id: str) -> None: ...
    @callback
    @override
    def _handle_signal(self, signal: InfraredReceivedSignal) -> None: ...
