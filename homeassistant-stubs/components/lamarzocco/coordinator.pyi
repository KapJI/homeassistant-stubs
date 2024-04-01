from .const import CONF_MACHINE as CONF_MACHINE, CONF_USE_BLUETOOTH as CONF_USE_BLUETOOTH, DOMAIN as DOMAIN
from _typeshed import Incomplete
from bleak.backends.device import BLEDevice as BLEDevice
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.bluetooth import async_ble_device_from_address as async_ble_device_from_address, async_discovered_service_info as async_discovered_service_info
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete
NAME_PREFIXES: Incomplete

class LaMarzoccoUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    lm: Incomplete
    local_connection_configured: Incomplete
    _use_bluetooth: bool
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def _async_init_client(self) -> None: ...
    async def _async_handle_request(self, func: Callable[..., Coroutine[None, None, None]], *args: Any, **kwargs: Any) -> None: ...
    def async_get_ble_device(self) -> BLEDevice | None: ...
