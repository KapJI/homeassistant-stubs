from .coordinator import RabbitAirConfigEntry as RabbitAirConfigEntry, RabbitAirDataUpdateCoordinator as RabbitAirDataUpdateCoordinator
from homeassistant.components import zeroconf as zeroconf
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from rabbitair import Client as Client

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: RabbitAirConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: RabbitAirConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: RabbitAirConfigEntry) -> None: ...
