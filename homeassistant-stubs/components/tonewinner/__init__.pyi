from .const import CONF_SERIAL_PORT as CONF_SERIAL_PORT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from tonewinner_rs232 import TonewinnerReceiver

PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete
type TonewinnerConfigEntry = ConfigEntry[TonewinnerReceiver]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TonewinnerConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TonewinnerConfigEntry) -> bool: ...
