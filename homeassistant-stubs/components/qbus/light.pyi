from .coordinator import QbusConfigEntry as QbusConfigEntry
from .entity import QbusEntity as QbusEntity, add_new_outputs as add_new_outputs
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.color import brightness_to_value as brightness_to_value, value_to_brightness as value_to_brightness
from qbusmqttapi.discovery import QbusMqttOutput as QbusMqttOutput
from qbusmqttapi.state import QbusMqttAnalogState
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: QbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class QbusLight(QbusEntity, LightEntity):
    _state_cls = QbusMqttAnalogState
    _attr_name: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    def __init__(self, mqtt_output: QbusMqttOutput) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _handle_state_received(self, state: QbusMqttAnalogState) -> None: ...
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    def _set_state(self, percentage: int) -> None: ...
