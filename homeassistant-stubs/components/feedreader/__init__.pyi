from .const import CONF_MAX_ENTRIES as CONF_MAX_ENTRIES, DEFAULT_MAX_ENTRIES as DEFAULT_MAX_ENTRIES, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from .coordinator import FeedReaderCoordinator as FeedReaderCoordinator, StoredData as StoredData
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey

FeedReaderConfigEntry = ConfigEntry[FeedReaderCoordinator]
CONF_URLS: str
MY_KEY: HassKey[StoredData]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: FeedReaderConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FeedReaderConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: FeedReaderConfigEntry) -> None: ...
