from .bluetooth import async_connect_scanner as async_connect_scanner
from .const import DOMAIN as DOMAIN
from .coordinator import RuuviGatewayUpdateCoordinator as RuuviGatewayUpdateCoordinator
from .models import RuuviGatewayRuntimeData as RuuviGatewayRuntimeData
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
