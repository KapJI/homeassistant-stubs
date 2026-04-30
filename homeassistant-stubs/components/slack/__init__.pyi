from .const import ATTR_URL as ATTR_URL, ATTR_USER_ID as ATTR_USER_ID, DATA_CLIENT as DATA_CLIENT, DATA_HASS_CONFIG as DATA_HASS_CONFIG, DOMAIN as DOMAIN, SLACK_DATA as SLACK_DATA
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client, discovery as discovery
from homeassistant.helpers.typing import ConfigType as ConfigType
from slack_sdk.web.async_client import AsyncWebClient

_LOGGER: Incomplete
PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete
type SlackConfigEntry = ConfigEntry[SlackData]

@dataclass
class SlackData:
    client: AsyncWebClient
    url: str
    user_id: str

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: SlackConfigEntry) -> bool: ...
