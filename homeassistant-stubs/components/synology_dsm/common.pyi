from .const import CONF_DEVICE_TOKEN as CONF_DEVICE_TOKEN, DOMAIN as DOMAIN, SYSTEM_LOADED as SYSTEM_LOADED
from collections.abc import Callable as Callable
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from synology_dsm.api.dsm.network import SynoDSMNetwork as SynoDSMNetwork
from typing import Any

LOGGER: Any

class SynoApi:
    _hass: Any
    _entry: Any
    config_url: Any
    dsm: Any
    information: Any
    network: Any
    security: Any
    storage: Any
    surveillance_station: Any
    system: Any
    upgrade: Any
    utilisation: Any
    _fetching_entities: Any
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
    def _async_setup_api_requests(self) -> None: ...
    def _fetch_device_configuration(self) -> None: ...
    def _set_system_loaded(self, state: bool = ...) -> None: ...
    async def _syno_api_executer(self, api_call: Callable) -> None: ...
    async def async_reboot(self) -> None: ...
    async def async_shutdown(self) -> None: ...
    async def async_unload(self) -> None: ...
    async def async_update(self, now: Union[timedelta, None] = ...) -> None: ...
