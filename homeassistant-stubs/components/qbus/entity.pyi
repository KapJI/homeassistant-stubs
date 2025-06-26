import abc
from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import QbusControllerCoordinator as QbusControllerCoordinator
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Callable as Callable
from homeassistant.components.mqtt import ReceiveMessage as ReceiveMessage
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from qbusmqttapi.discovery import QbusMqttOutput as QbusMqttOutput
from qbusmqttapi.state import QbusMqttState
from typing import Generic, TypeVar

_REFID_REGEX: Incomplete
StateT = TypeVar('StateT', bound=QbusMqttState)

def add_new_outputs(coordinator: QbusControllerCoordinator, added_outputs: list[QbusMqttOutput], filter_fn: Callable[[QbusMqttOutput], bool], entity_type: type[QbusEntity], async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def format_ref_id(ref_id: str) -> str | None: ...
def create_main_device_identifier(mqtt_output: QbusMqttOutput) -> tuple[str, str]: ...

class QbusEntity(Entity, ABC, Generic[StateT], metaclass=abc.ABCMeta):
    _state_cls: type[StateT]
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _mqtt_output: Incomplete
    _topic_factory: Incomplete
    _message_factory: Incomplete
    _state_topic: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, mqtt_output: QbusMqttOutput) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _state_received(self, msg: ReceiveMessage) -> None: ...
    @abstractmethod
    async def _handle_state_received(self, state: StateT) -> None: ...
    async def _async_publish_output_state(self, state: QbusMqttState) -> None: ...
