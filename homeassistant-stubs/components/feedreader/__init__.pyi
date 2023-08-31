import feedparser
from _typeshed import Incomplete
from datetime import datetime, timedelta
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from time import struct_time as struct_time

_LOGGER: Incomplete
CONF_URLS: str
CONF_MAX_ENTRIES: str
DEFAULT_MAX_ENTRIES: int
DEFAULT_SCAN_INTERVAL: Incomplete
DELAY_SAVE: int
DOMAIN: str
EVENT_FEEDREADER: str
STORAGE_VERSION: int
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class FeedManager:
    _hass: Incomplete
    _url: Incomplete
    _scan_interval: Incomplete
    _max_entries: Incomplete
    _feed: Incomplete
    _firstrun: bool
    _storage: Incomplete
    _last_entry_timestamp: Incomplete
    _has_published_parsed: bool
    _has_updated_parsed: bool
    _event_type: Incomplete
    _feed_id: Incomplete
    def __init__(self, hass: HomeAssistant, url: str, scan_interval: timedelta, max_entries: int, storage: StoredData) -> None: ...
    def async_setup(self) -> None: ...
    def _log_no_entries(self) -> None: ...
    async def _async_update(self, _: datetime | Event) -> None: ...
    def _update(self) -> struct_time | None: ...
    def _filter_entries(self) -> None: ...
    def _update_and_fire_entry(self, entry: feedparser.FeedParserDict) -> None: ...
    def _publish_new_entries(self) -> None: ...

class StoredData:
    _legacy_data_file: Incomplete
    _data: Incomplete
    _hass: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant, legacy_data_file: str) -> None: ...
    async def async_setup(self) -> None: ...
    def _legacy_fetch_data(self) -> dict[str, struct_time]: ...
    def get_timestamp(self, feed_id: str) -> struct_time | None: ...
    def async_put_timestamp(self, feed_id: str, timestamp: struct_time) -> None: ...
    def _async_save_data(self) -> dict[str, str]: ...
