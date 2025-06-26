from .coordinator import QbusConfigEntry as QbusConfigEntry
from .entity import QbusEntity as QbusEntity, add_new_outputs as add_new_outputs, create_main_device_identifier as create_main_device_identifier
from _typeshed import Incomplete
from homeassistant.components.scene import Scene as Scene
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from qbusmqttapi.discovery import QbusMqttOutput as QbusMqttOutput
from qbusmqttapi.state import QbusMqttState
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: QbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class QbusScene(QbusEntity, Scene):
    _attr_device_info: Incomplete
    _attr_name: Incomplete
    def __init__(self, mqtt_output: QbusMqttOutput) -> None: ...
    async def async_activate(self, **kwargs: Any) -> None: ...
    async def _handle_state_received(self, state: QbusMqttState) -> None: ...
