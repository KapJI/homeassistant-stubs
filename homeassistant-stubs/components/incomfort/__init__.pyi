from .const import DOMAIN as DOMAIN
from .coordinator import InComfortConfigEntry as InComfortConfigEntry, InComfortData as InComfortData, InComfortDataCoordinator as InComfortDataCoordinator, async_connect_gateway as async_connect_gateway
from .errors import InComfortTimeout as InComfortTimeout, InComfortUnknownError as InComfortUnknownError, NoHeaters as NoHeaters, NotFound as NotFound
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers import device_registry as dr

PLATFORMS: Incomplete
INTEGRATION_TITLE: str

@callback
def async_cleanup_stale_devices(hass: HomeAssistant, entry: InComfortConfigEntry, data: InComfortData, gateway_device: dr.DeviceEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: InComfortConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: InComfortConfigEntry) -> bool: ...
