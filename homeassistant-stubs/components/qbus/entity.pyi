import abc
from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.components.mqtt import ReceiveMessage as ReceiveMessage
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.entity import Entity as Entity
from qbusmqttapi.discovery import QbusMqttOutput as QbusMqttOutput
from qbusmqttapi.state import QbusMqttState as QbusMqttState

_REFID_REGEX: Incomplete

def format_ref_id(ref_id: str) -> str | None: ...

class QbusEntity(Entity, ABC, metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _topic_factory: Incomplete
    _message_factory: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _mqtt_output: Incomplete
    _state_topic: Incomplete
    def __init__(self, mqtt_output: QbusMqttOutput) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @abstractmethod
    async def _state_received(self, msg: ReceiveMessage) -> None: ...
    async def _async_publish_output_state(self, state: QbusMqttState) -> None: ...
