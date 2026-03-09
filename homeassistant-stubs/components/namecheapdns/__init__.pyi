from .const import DOMAIN as DOMAIN
from .coordinator import NamecheapConfigEntry as NamecheapConfigEntry, NamecheapDnsUpdateCoordinator as NamecheapDnsUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN, CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: NamecheapConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: NamecheapConfigEntry) -> bool: ...
