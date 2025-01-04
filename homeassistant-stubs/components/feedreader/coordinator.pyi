import feedparser
from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, EVENT_FEEDREADER as EVENT_FEEDREADER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from time import struct_time as struct_time

DELAY_SAVE: int
STORAGE_VERSION: int
_LOGGER: Incomplete

class FeedReaderCoordinator(DataUpdateCoordinator[list[feedparser.FeedParserDict] | None]):
    config_entry: ConfigEntry
    url: Incomplete
    feed_author: Incomplete
    feed_version: Incomplete
    _max_entries: Incomplete
    _storage: Incomplete
    _last_entry_timestamp: Incomplete
    _event_type: Incomplete
    _feed: Incomplete
    _feed_id: Incomplete
    def __init__(self, hass: HomeAssistant, url: str, max_entries: int, storage: StoredData) -> None: ...
    def _log_no_entries(self) -> None: ...
    async def _async_fetch_feed(self) -> feedparser.FeedParserDict: ...
    async def async_setup(self) -> None: ...
    async def _async_update_data(self) -> list[feedparser.FeedParserDict] | None: ...
    def _filter_entries(self) -> None: ...
    def _update_and_fire_entry(self, entry: feedparser.FeedParserDict) -> None: ...
    def _publish_new_entries(self) -> None: ...

class StoredData:
    _data: Incomplete
    hass: Incomplete
    _store: Incomplete
    is_initialized: bool
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_setup(self) -> None: ...
    def get_timestamp(self, feed_id: str) -> struct_time | None: ...
    def async_put_timestamp(self, feed_id: str, timestamp: struct_time) -> None: ...
    def _async_save_data(self) -> dict[str, str]: ...
