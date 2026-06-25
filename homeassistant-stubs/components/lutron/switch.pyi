from . import LutronConfigEntry as LutronConfigEntry
from .entity import LutronDevice as LutronDevice, LutronKeypad as LutronKeypad
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylutron import Button as Button, Keypad as Keypad, Led, Lutron as Lutron, Output as Output
from typing import Any, override

async def async_setup_entry(hass: HomeAssistant, config_entry: LutronConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LutronSwitch(LutronDevice, SwitchEntity):
    _lutron_device: Output
    _attr_name: Incomplete
    @override
    def turn_on(self, **kwargs: Any) -> None: ...
    @override
    def turn_off(self, **kwargs: Any) -> None: ...
    @property
    @override
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
    @override
    def _request_state(self) -> None: ...
    _attr_is_on: Incomplete
    @override
    def _update_attrs(self) -> None: ...

class LutronLed(LutronKeypad, SwitchEntity):
    _lutron_device: Led
    _keypad_name: Incomplete
    _attr_name: Incomplete
    def __init__(self, area_name: str, keypad: Keypad, scene_device: Button, led_device: Led, controller: Lutron) -> None: ...
    @override
    def turn_on(self, **kwargs: Any) -> None: ...
    @override
    def turn_off(self, **kwargs: Any) -> None: ...
    @property
    @override
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
    @override
    def _request_state(self) -> None: ...
    _attr_is_on: Incomplete
    @override
    def _update_attrs(self) -> None: ...
