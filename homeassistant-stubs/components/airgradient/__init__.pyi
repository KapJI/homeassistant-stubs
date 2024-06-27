from .const import DOMAIN as DOMAIN
from .coordinator import AirGradientConfigCoordinator as AirGradientConfigCoordinator, AirGradientMeasurementCoordinator as AirGradientMeasurementCoordinator
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

@dataclass
class AirGradientData:
    measurement: AirGradientMeasurementCoordinator
    config: AirGradientConfigCoordinator
    def __init__(self, measurement, config) -> None: ...
AirGradientConfigEntry = ConfigEntry[AirGradientData]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
