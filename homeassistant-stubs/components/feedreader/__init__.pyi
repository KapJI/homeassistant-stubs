from .const import DOMAIN as DOMAIN
from .coordinator import FeedReaderCoordinator as FeedReaderCoordinator, StoredData as StoredData
from _typeshed import Incomplete
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

CONF_URLS: str
CONF_MAX_ENTRIES: str
DEFAULT_MAX_ENTRIES: int
DEFAULT_SCAN_INTERVAL: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
