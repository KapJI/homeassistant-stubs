from .coordinator import QbusConfigEntry as QbusConfigEntry
from .entity import QbusEntity as QbusEntity
from _typeshed import Incomplete
from homeassistant.components.mqtt import ReceiveMessage as ReceiveMessage
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from qbusmqttapi.discovery import QbusMqttOutput as QbusMqttOutput
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: QbusConfigEntry, add_entities: AddEntitiesCallback) -> None: ...

class QbusSwitch(QbusEntity, SwitchEntity):
    _attr_device_class: Incomplete
    _attr_is_on: bool
    def __init__(self, mqtt_output: QbusMqttOutput) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _state_received(self, msg: ReceiveMessage) -> None: ...
