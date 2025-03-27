from .const import DOMAIN as DOMAIN
from .coordinator import VodafoneConfigEntry as VodafoneConfigEntry, VodafoneStationRouter as VodafoneStationRouter
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: VodafoneConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: VodafoneConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: VodafoneConfigEntry) -> None: ...
