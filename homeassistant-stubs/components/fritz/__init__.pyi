from .const import DEFAULT_SSL as DEFAULT_SSL, DOMAIN as DOMAIN, FRITZ_AUTH_EXCEPTIONS as FRITZ_AUTH_EXCEPTIONS, FRITZ_EXCEPTIONS as FRITZ_EXCEPTIONS, PLATFORMS as PLATFORMS
from .coordinator import AvmWrapper as AvmWrapper, FRITZ_DATA_KEY as FRITZ_DATA_KEY, FritzConfigEntry as FritzConfigEntry, FritzData as FritzData
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: FritzConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FritzConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: FritzConfigEntry) -> None: ...
