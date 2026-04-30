from . import LutronConfigEntry as LutronConfigEntry
from .entity import LutronKeypad as LutronKeypad
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylutron import Button as Button, Keypad as Keypad, Led, Lutron as Lutron

_LED_STATE_TO_OPTION: Incomplete
_LED_OPTION_TO_STATE: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: LutronConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LutronLedSelect(LutronKeypad, SelectEntity):
    _lutron_device: Led
    _attr_options: Incomplete
    _attr_translation_key: str
    _attr_name: Incomplete
    def __init__(self, area_name: str, keypad: Keypad, scene_device: Button, led_device: Led, controller: Lutron) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    def select_option(self, option: str) -> None: ...
    def _request_state(self) -> None: ...
