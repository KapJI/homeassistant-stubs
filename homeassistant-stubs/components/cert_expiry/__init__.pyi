from .coordinator import CertExpiryConfigEntry as CertExpiryConfigEntry, CertExpiryDataUpdateCoordinator as CertExpiryDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.start import async_at_started as async_at_started

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: CertExpiryConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: CertExpiryConfigEntry) -> bool: ...
