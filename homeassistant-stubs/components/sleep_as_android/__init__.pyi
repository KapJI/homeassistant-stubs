from .const import ATTR_EVENT as ATTR_EVENT, ATTR_VALUE1 as ATTR_VALUE1, ATTR_VALUE2 as ATTR_VALUE2, ATTR_VALUE3 as ATTR_VALUE3, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiohttp.web import Request as Request, Response
from homeassistant.components import webhook as webhook
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_WEBHOOK_ID as CONF_WEBHOOK_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send

PLATFORMS: list[Platform]
type SleepAsAndroidConfigEntry = ConfigEntry
WEBHOOK_SCHEMA: Incomplete

async def handle_webhook(hass: HomeAssistant, webhook_id: str, request: Request) -> Response: ...
async def async_setup_entry(hass: HomeAssistant, entry: SleepAsAndroidConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SleepAsAndroidConfigEntry) -> bool: ...
