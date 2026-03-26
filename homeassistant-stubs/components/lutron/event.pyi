from . import ATTR_ACTION as ATTR_ACTION, ATTR_FULL_ID as ATTR_FULL_ID, ATTR_UUID as ATTR_UUID, LutronConfigEntry as LutronConfigEntry
from .entity import LutronKeypad as LutronKeypad
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.components.event import EventEntity as EventEntity
from homeassistant.const import ATTR_ID as ATTR_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util import slugify as slugify
from pylutron import Button, Keypad as Keypad, Lutron as Lutron, LutronEntity as LutronEntity, LutronEvent as LutronEvent

class LutronEventType(StrEnum):
    SINGLE_PRESS = 'single_press'
    PRESS = 'press'
    RELEASE = 'release'

LEGACY_EVENT_TYPES: dict[LutronEventType, str]

async def async_setup_entry(hass: HomeAssistant, config_entry: LutronConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LutronEventEntity(LutronKeypad, EventEntity):
    _attr_translation_key: str
    _attr_name: Incomplete
    _has_release_event: Incomplete
    _attr_event_types: Incomplete
    _full_id: Incomplete
    _id: Incomplete
    def __init__(self, area_name: str, keypad: Keypad, button: Button, controller: Lutron) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def handle_event(self, button: LutronEntity, _context: None, event: LutronEvent, _params: dict) -> None: ...
