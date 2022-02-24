from .const import DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from pywizlight.discovery import DiscoveredBulb
from typing import Any

_LOGGER: Any

async def async_discover_devices(hass: HomeAssistant, timeout: int) -> list[DiscoveredBulb]: ...
def async_trigger_discovery(hass: HomeAssistant, discovered_devices: list[DiscoveredBulb]) -> None: ...
