from .coordinator import QbusConfigEntry as QbusConfigEntry
from .entity import QbusEntity as QbusEntity, create_new_entities as create_new_entities
from _typeshed import Incomplete
from homeassistant.components.scene import BaseScene as BaseScene
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from qbusmqttapi.discovery import QbusMqttOutput as QbusMqttOutput
from qbusmqttapi.state import QbusMqttState
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: QbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class QbusScene(QbusEntity, BaseScene):
    _attr_name: Incomplete
    def __init__(self, mqtt_output: QbusMqttOutput) -> None: ...
    async def _async_activate(self, **kwargs: Any) -> None: ...
    async def _handle_state_received(self, state: QbusMqttState) -> None: ...
