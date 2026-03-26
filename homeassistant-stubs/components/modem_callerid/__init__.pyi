from .const import EXCEPTIONS as EXCEPTIONS
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from phone_modem import PhoneModem

PLATFORMS: Incomplete
type ModemCallerIdConfigEntry = ConfigEntry[PhoneModem]

async def async_setup_entry(hass: HomeAssistant, entry: ModemCallerIdConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ModemCallerIdConfigEntry) -> bool: ...
