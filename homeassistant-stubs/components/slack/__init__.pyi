from .const import ATTR_URL as ATTR_URL, ATTR_USER_ID as ATTR_USER_ID, DATA_CLIENT as DATA_CLIENT, DATA_HASS_CONFIG as DATA_HASS_CONFIG, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, SLACK_DATA as SLACK_DATA
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client, discovery as discovery
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.typing import ConfigType as ConfigType
from slack import WebClient

_LOGGER: Incomplete
PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SlackEntity(Entity):
    _attr_attribution: str
    _attr_has_entity_name: bool
    _client: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data: dict[str, str | WebClient], description: EntityDescription, entry: ConfigEntry) -> None: ...
