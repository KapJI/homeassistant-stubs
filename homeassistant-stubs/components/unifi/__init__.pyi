from .const import PLATFORMS as PLATFORMS, UNIFI_WIRELESS_CLIENTS as UNIFI_WIRELESS_CLIENTS
from .controller import UniFiController as UniFiController, get_unifi_controller as get_unifi_controller
from .errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from .services import async_setup_services as async_setup_services, async_unload_services as async_unload_services
from _typeshed import Incomplete
from aiounifi.models.client import Client as Client
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType

SAVE_DELAY: int
STORAGE_KEY: str
STORAGE_VERSION: int
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
def async_remove_poe_client_entities(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...

class UnifiWirelessClients:
    hass: Incomplete
    data: Incomplete
    wireless_clients: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_load(self) -> None: ...
    def is_wireless(self, client: Client) -> bool: ...
    def update_clients(self, clients: set[Client]) -> None: ...
    def _data_to_save(self) -> dict[str, dict[str, list[str]] | list[str]]: ...
    def __contains__(self, obj_id: int | str) -> bool: ...
