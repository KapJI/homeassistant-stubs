from .const import CONF_API_USER as CONF_API_USER, DOMAIN as DOMAIN, X_CLIENT as X_CLIENT
from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry, HabiticaDataUpdateCoordinator as HabiticaDataUpdateCoordinator, HabiticaPartyCoordinator as HabiticaPartyCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from uuid import UUID

CONFIG_SCHEMA: Incomplete
HABITICA_KEY: HassKey[dict[UUID, HabiticaPartyCoordinator]]
PLATFORMS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: HabiticaConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: HabiticaConfigEntry) -> None: ...
async def shutdown_party_coordinator(hass: HomeAssistant, party_added: UUID) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: HabiticaConfigEntry) -> bool: ...
