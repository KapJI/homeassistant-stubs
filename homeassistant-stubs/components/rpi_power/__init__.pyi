from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from rpi_bad_power import UnderVoltage

PLATFORMS: Incomplete
type RpiPowerConfigEntry = ConfigEntry[UnderVoltage]

async def async_setup_entry(hass: HomeAssistant, entry: RpiPowerConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: RpiPowerConfigEntry) -> bool: ...
