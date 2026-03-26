from .const import CONF_PHONE_NUMBER as CONF_PHONE_NUMBER, DOMAIN as DOMAIN
from .coordinator import PecoOutageCoordinator as PecoOutageCoordinator, PecoSmartMeterCoordinator as PecoSmartMeterCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Final

PLATFORMS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
