from . import FeedReaderConfigEntry as FeedReaderConfigEntry
from .const import DOMAIN as DOMAIN, EVENT_FEEDREADER as EVENT_FEEDREADER
from .coordinator import FeedReaderCoordinator as FeedReaderCoordinator
from _typeshed import Incomplete
from feedparser import FeedParserDict as FeedParserDict
from homeassistant.components.event import EventEntity as EventEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

LOGGER: Incomplete
ATTR_CONTENT: str
ATTR_DESCRIPTION: str
ATTR_LINK: str
ATTR_TITLE: str

async def async_setup_entry(hass: HomeAssistant, entry: FeedReaderConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FeedReaderEvent(CoordinatorEntity[FeedReaderCoordinator], EventEntity):
    _attr_event_types: Incomplete
    _attr_name: Incomplete
    _attr_has_entity_name: bool
    _unrecorded_attributes: Incomplete
    coordinator: FeedReaderCoordinator
    _attr_unique_id: Incomplete
    _attr_translation_key: str
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FeedReaderCoordinator) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
