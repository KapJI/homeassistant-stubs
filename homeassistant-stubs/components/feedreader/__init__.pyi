from .const import DOMAIN as DOMAIN
from .coordinator import FeedReaderConfigEntry as FeedReaderConfigEntry, FeedReaderCoordinator as FeedReaderCoordinator, StoredData as StoredData
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util.hass_dict import HassKey as HassKey

FEEDREADER_KEY: HassKey[StoredData]

async def async_setup_entry(hass: HomeAssistant, entry: FeedReaderConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FeedReaderConfigEntry) -> bool: ...
