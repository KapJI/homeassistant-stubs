from .coordinator import QbusConfigEntry as QbusConfigEntry
from .entity import QbusEntity as QbusEntity, create_new_entities as create_new_entities
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_EFFECT as ATTR_EFFECT, ATTR_HS_COLOR as ATTR_HS_COLOR, ColorMode as ColorMode, EFFECT_OFF as EFFECT_OFF, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.color import brightness_to_value as brightness_to_value, value_to_brightness as value_to_brightness
from qbusmqttapi.discovery import QbusMqttOutput as QbusMqttOutput
from qbusmqttapi.state import QbusMqttAnalogState, QbusMqttMultiColorState
from typing import Any, override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: QbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class QbusLight(QbusEntity, LightEntity):
    _state_cls = QbusMqttAnalogState
    _attr_name: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    def __init__(self, mqtt_output: QbusMqttOutput) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @override
    async def _handle_state_received(self, state: QbusMqttAnalogState) -> None: ...
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    def _set_state(self, percentage: int) -> None: ...

class QbusMultiColor(QbusEntity, LightEntity):
    _state_cls = QbusMqttMultiColorState
    _attr_name: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    _effect_name_to_value: dict[str, int]
    _effect_value_to_name: dict[int, str]
    _attr_effect_list: Incomplete
    def __init__(self, mqtt_output: QbusMqttOutput) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @override
    async def _handle_state_received(self, state: QbusMqttMultiColorState) -> None: ...
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    _attr_hs_color: Incomplete
    _attr_effect: Incomplete
    def _set_state(self, brightness: int | None = None, hs: tuple[float, float] | None = None, effect: str | None = None) -> None: ...
    async def _async_request_state(self) -> None: ...
