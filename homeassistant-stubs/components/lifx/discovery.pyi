from .const import CONF_SERIAL as CONF_SERIAL, DOMAIN as DOMAIN
from aiolifx.aiolifx import Light as Light
from collections.abc import Iterable
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

DEFAULT_TIMEOUT: float

async def async_discover_devices(hass: HomeAssistant) -> Iterable[Light]: ...
def async_init_discovery_flow(hass: HomeAssistant, host: str, serial: str) -> None: ...
def async_trigger_discovery(hass: HomeAssistant, discovered_devices: Iterable[Light]) -> None: ...
