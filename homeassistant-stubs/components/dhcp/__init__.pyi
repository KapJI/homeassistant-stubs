import aiodhcpwatcher
import asyncio
from .helpers import async_discovered_service_info as async_discovered_service_info
from .models import DHCPData
from _typeshed import Incomplete
from aiodiscover import DiscoverHosts
from collections.abc import Callable
from homeassistant import config_entries
from homeassistant.core import Event, EventStateChangedData, HomeAssistant, State, callback
from typing import Any, override

__all__ = ['async_discovered_service_info']

class WatcherBase:
    hass: Incomplete
    _callbacks: Incomplete
    _integration_matchers: Incomplete
    _address_data: Incomplete
    _unsub: Callable[[], None] | None
    def __init__(self, hass: HomeAssistant, dhcp_data: DHCPData) -> None: ...
    @callback
    def async_stop(self) -> None: ...
    @callback
    def async_process_client(self, ip_address: str, hostname: str, unformatted_mac_address: str, force: bool = False) -> None: ...

class NetworkWatcher(WatcherBase):
    _discover_hosts: DiscoverHosts | None
    _discover_task: asyncio.Task | None
    def __init__(self, hass: HomeAssistant, dhcp_data: DHCPData) -> None: ...
    @callback
    @override
    def async_stop(self) -> None: ...
    _unsub: Incomplete
    @callback
    def async_start(self) -> None: ...
    @callback
    def async_start_discover(self, *_: Any) -> None: ...
    async def async_discover(self) -> None: ...

class DeviceTrackerWatcher(WatcherBase):
    _unsub: Incomplete
    @callback
    def async_start(self) -> None: ...
    @callback
    def _async_process_device_event(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _async_process_device_state(self, state: State | None) -> None: ...

class DeviceTrackerRegisteredWatcher(WatcherBase):
    _unsub: Incomplete
    @callback
    def async_start(self) -> None: ...
    @callback
    def _async_process_device_data(self, data: dict[str, str | None]) -> None: ...

class DHCPWatcher(WatcherBase):
    @callback
    def _async_process_dhcp_request(self, response: aiodhcpwatcher.DHCPRequest) -> None: ...
    async def async_get_adapter_indexes(self) -> list[int] | None: ...
    _unsub: Incomplete
    async def async_start(self) -> None: ...

class RediscoveryWatcher(WatcherBase):
    @callback
    def _handle_config_entry_removed(self, entry: config_entries.ConfigEntry) -> None: ...
    _unsub: Incomplete
    @callback
    def async_start(self) -> None: ...
