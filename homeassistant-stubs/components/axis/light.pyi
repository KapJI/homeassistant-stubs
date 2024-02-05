from .device import AxisNetworkDevice as AxisNetworkDevice
from .entity import AxisEventEntity as AxisEventEntity
from _typeshed import Incomplete
from axis.models.event import Event as Event
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AxisLight(AxisEventEntity, LightEntity):
    _attr_should_poll: bool
    _light_id: Incomplete
    current_intensity: int
    max_intensity: int
    _attr_name: Incomplete
    _attr_is_on: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    def __init__(self, event: Event, device: AxisNetworkDevice) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def async_event_callback(self, event: Event) -> None: ...
    @property
    def brightness(self) -> int: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_update(self) -> None: ...
