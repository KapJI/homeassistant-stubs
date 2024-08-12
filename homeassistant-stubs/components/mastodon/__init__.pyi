from .const import CONF_BASE_URL as CONF_BASE_URL, DOMAIN as DOMAIN
from .utils import create_mastodon_client as create_mastodon_client
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery as discovery
from mastodon.Mastodon import Mastodon as Mastodon

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def setup_mastodon(entry: ConfigEntry) -> tuple[Mastodon, dict, dict]: ...
