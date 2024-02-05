from .device import AxisNetworkDevice as AxisNetworkDevice
from .entity import AxisEventEntity as AxisEventEntity
from _typeshed import Incomplete
from axis.models.event import Event as Event
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AxisSwitch(AxisEventEntity, SwitchEntity):
    _attr_name: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, event: Event, device: AxisNetworkDevice) -> None: ...
    def async_event_callback(self, event: Event) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
