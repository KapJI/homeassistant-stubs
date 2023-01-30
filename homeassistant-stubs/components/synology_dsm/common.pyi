from .const import CONF_DEVICE_TOKEN as CONF_DEVICE_TOKEN, SYNOLOGY_CONNECTION_EXCEPTIONS as SYNOLOGY_CONNECTION_EXCEPTIONS
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from synology_dsm.api.dsm.network import SynoDSMNetwork as SynoDSMNetwork

LOGGER: Incomplete

class SynoApi:
    _hass: Incomplete
    _entry: Incomplete
    config_url: Incomplete
    dsm: Incomplete
    information: Incomplete
    network: Incomplete
    security: Incomplete
    storage: Incomplete
    surveillance_station: Incomplete
    system: Incomplete
    upgrade: Incomplete
    utilisation: Incomplete
    _fetching_entities: Incomplete
    _with_information: bool
    _with_security: bool
    _with_storage: bool
    _with_surveillance_station: bool
    _with_system: bool
    _with_upgrade: bool
    _with_utilisation: bool
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def async_setup(self) -> None: ...
    def subscribe(self, api_key: str, unique_id: str) -> Callable[[], None]: ...
    def _setup_api_requests(self) -> None: ...
    async def _fetch_device_configuration(self) -> None: ...
    async def _syno_api_executer(self, api_call: Callable) -> None: ...
    async def async_reboot(self) -> None: ...
    async def async_shutdown(self) -> None: ...
    async def async_unload(self) -> None: ...
    async def async_update(self) -> None: ...
    async def _update(self) -> None: ...
