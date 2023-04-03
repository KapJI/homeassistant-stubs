import feedparser
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.event import track_time_interval as track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from time import struct_time

_LOGGER: Incomplete
CONF_URLS: str
CONF_MAX_ENTRIES: str
DEFAULT_MAX_ENTRIES: int
DEFAULT_SCAN_INTERVAL: Incomplete
DOMAIN: str
EVENT_FEEDREADER: str
CONFIG_SCHEMA: Incomplete

def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class FeedManager:
    _url: Incomplete
    _scan_interval: Incomplete
    _max_entries: Incomplete
    _feed: Incomplete
    _hass: Incomplete
    _firstrun: bool
    _storage: Incomplete
    _last_entry_timestamp: Incomplete
    _last_update_successful: bool
    _has_published_parsed: bool
    _has_updated_parsed: bool
    _event_type: Incomplete
    _feed_id: Incomplete
    def __init__(self, url: str, scan_interval: timedelta, max_entries: int, hass: HomeAssistant, storage: StoredData) -> None: ...
    def _log_no_entries(self) -> None: ...
    def _init_regular_updates(self, hass: HomeAssistant) -> None: ...
    @property
    def last_update_successful(self) -> bool: ...
    def _update(self) -> None: ...
    def _filter_entries(self) -> None: ...
    def _update_and_fire_entry(self, entry: feedparser.FeedParserDict) -> None: ...
    def _publish_new_entries(self) -> None: ...

class StoredData:
    _data_file: Incomplete
    _lock: Incomplete
    _cache_outdated: bool
    _data: Incomplete
    def __init__(self, data_file: str) -> None: ...
    def _fetch_data(self) -> None: ...
    def get_timestamp(self, feed_id: str) -> struct_time | None: ...
    def put_timestamp(self, feed_id: str, timestamp: struct_time) -> None: ...
