from .const import DOMAIN as DOMAIN
from .coordinator import UptimeKumaConfigEntry as UptimeKumaConfigEntry, UptimeKumaDataUpdateCoordinator as UptimeKumaDataUpdateCoordinator, UptimeKumaSoftwareUpdateCoordinator as UptimeKumaSoftwareUpdateCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.util.hass_dict import HassKey as HassKey

_PLATFORMS: list[Platform]
UPTIME_KUMA_KEY: HassKey[UptimeKumaSoftwareUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: UptimeKumaConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: UptimeKumaConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: UptimeKumaConfigEntry) -> bool: ...
