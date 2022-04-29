from .base import FritzBoxPhonebook as FritzBoxPhonebook
from .const import CONF_PHONEBOOK as CONF_PHONEBOOK, CONF_PREFIXES as CONF_PREFIXES, DOMAIN as DOMAIN, FRITZBOX_PHONEBOOK as FRITZBOX_PHONEBOOK, PLATFORMS as PLATFORMS, UNDO_UPDATE_LISTENER as UNDO_UPDATE_LISTENER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
