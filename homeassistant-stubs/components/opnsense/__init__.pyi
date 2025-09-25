from .const import CONF_API_SECRET as CONF_API_SECRET, CONF_INTERFACE_CLIENT as CONF_INTERFACE_CLIENT, CONF_TRACKER_INTERFACES as CONF_TRACKER_INTERFACES, DOMAIN as DOMAIN, OPNSENSE_DATA as OPNSENSE_DATA
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.discovery import load_platform as load_platform
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
