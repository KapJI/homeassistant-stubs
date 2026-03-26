from . import LutronConfigEntry as LutronConfigEntry
from .entity import LutronKeypad as LutronKeypad
from _typeshed import Incomplete
from homeassistant.components.scene import Scene as Scene
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylutron import Button as Button, Keypad as Keypad, Lutron as Lutron
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: LutronConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LutronScene(LutronKeypad, Scene):
    _lutron_device: Button
    _attr_name: Incomplete
    def __init__(self, area_name: str, keypad: Keypad, lutron_device: Button, controller: Lutron) -> None: ...
    def activate(self, **kwargs: Any) -> None: ...
