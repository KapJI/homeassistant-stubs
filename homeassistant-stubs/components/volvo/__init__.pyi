from .api import VolvoAuth as VolvoAuth
from .const import CONF_VIN as CONF_VIN, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import VolvoConfigEntry as VolvoConfigEntry, VolvoFastIntervalCoordinator as VolvoFastIntervalCoordinator, VolvoMediumIntervalCoordinator as VolvoMediumIntervalCoordinator, VolvoSlowIntervalCoordinator as VolvoSlowIntervalCoordinator, VolvoVerySlowIntervalCoordinator as VolvoVerySlowIntervalCoordinator
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from volvocarsapi.api import VolvoCarsApi
from volvocarsapi.models import VolvoCarsVehicle as VolvoCarsVehicle

async def async_setup_entry(hass: HomeAssistant, entry: VolvoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: VolvoConfigEntry) -> bool: ...
async def _async_auth_and_create_api(hass: HomeAssistant, entry: VolvoConfigEntry) -> VolvoCarsApi: ...
async def _async_load_vehicle(api: VolvoCarsApi) -> VolvoCarsVehicle: ...
