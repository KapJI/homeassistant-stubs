from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from pylutron import Keypad as Keypad, Lutron as Lutron, LutronEntity as LutronEntity, LutronEvent as LutronEvent
from typing import override

class LutronBaseEntity(Entity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _lutron_device: Incomplete
    _controller: Incomplete
    _area_name: Incomplete
    def __init__(self, area_name: str, lutron_device: LutronEntity, controller: Lutron) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    def _request_state(self) -> None: ...
    def _update_attrs(self) -> None: ...
    def _update_callback(self, _device: LutronEntity, _context: None, _event: LutronEvent, _params: dict) -> None: ...
    @property
    @override
    def unique_id(self) -> str: ...
    def update(self) -> None: ...

class LutronDevice(LutronBaseEntity):
    _attr_device_info: Incomplete
    def __init__(self, hass: HomeAssistant, area_name: str, lutron_device: LutronEntity, controller: Lutron, config_entry_id: str) -> None: ...

class LutronKeypad(LutronBaseEntity):
    _keypad: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, hass: HomeAssistant, area_name: str, lutron_device: LutronEntity, controller: Lutron, keypad: Keypad, config_entry_id: str) -> None: ...
