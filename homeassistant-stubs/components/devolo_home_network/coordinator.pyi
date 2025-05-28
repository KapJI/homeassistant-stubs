from .const import CONNECTED_PLC_DEVICES as CONNECTED_PLC_DEVICES, CONNECTED_WIFI_CLIENTS as CONNECTED_WIFI_CLIENTS, DOMAIN as DOMAIN, FIRMWARE_UPDATE_INTERVAL as FIRMWARE_UPDATE_INTERVAL, LAST_RESTART as LAST_RESTART, LONG_UPDATE_INTERVAL as LONG_UPDATE_INTERVAL, NEIGHBORING_WIFI_NETWORKS as NEIGHBORING_WIFI_NETWORKS, REGULAR_FIRMWARE as REGULAR_FIRMWARE, SHORT_UPDATE_INTERVAL as SHORT_UPDATE_INTERVAL, SWITCH_GUEST_WIFI as SWITCH_GUEST_WIFI, SWITCH_LEDS as SWITCH_LEDS
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import timedelta
from devolo_plc_api import Device as Device
from devolo_plc_api.device_api import ConnectedStationInfo, NeighborAPInfo, UpdateFirmwareCheck, WifiGuestAccessGet
from devolo_plc_api.plcnet_api import LogicalNetwork
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from logging import Logger
from typing import Any

SEMAPHORE: Incomplete
type DevoloHomeNetworkConfigEntry = ConfigEntry[DevoloHomeNetworkData]

class DevoloDataUpdateCoordinator[_DataT](DataUpdateCoordinator[_DataT]):
    device: Incomplete
    def __init__(self, hass: HomeAssistant, logger: Logger, *, config_entry: DevoloHomeNetworkConfigEntry, name: str, update_interval: timedelta | None = None) -> None: ...
    async def _async_update_data(self) -> _DataT: ...
    @callback
    def update_sw_version(self) -> None: ...

class DevoloFirmwareUpdateCoordinator(DevoloDataUpdateCoordinator[UpdateFirmwareCheck]):
    update_method: Incomplete
    def __init__(self, hass: HomeAssistant, logger: Logger, *, config_entry: ConfigEntry, name: str = ..., update_interval: timedelta | None = ...) -> None: ...
    async def async_update_firmware_available(self) -> UpdateFirmwareCheck: ...

class DevoloLedSettingsGetCoordinator(DevoloDataUpdateCoordinator[bool]):
    update_method: Incomplete
    def __init__(self, hass: HomeAssistant, logger: Logger, *, config_entry: ConfigEntry, name: str = ..., update_interval: timedelta | None = ...) -> None: ...
    async def async_update_led_status(self) -> bool: ...

class DevoloLogicalNetworkCoordinator(DevoloDataUpdateCoordinator[LogicalNetwork]):
    update_method: Incomplete
    def __init__(self, hass: HomeAssistant, logger: Logger, *, config_entry: ConfigEntry, name: str = ..., update_interval: timedelta | None = ...) -> None: ...
    async def async_update_connected_plc_devices(self) -> LogicalNetwork: ...

class DevoloUptimeGetCoordinator(DevoloDataUpdateCoordinator[int]):
    update_method: Incomplete
    def __init__(self, hass: HomeAssistant, logger: Logger, *, config_entry: ConfigEntry, name: str = ..., update_interval: timedelta | None = ...) -> None: ...
    async def async_update_last_restart(self) -> int: ...

class DevoloWifiConnectedStationsGetCoordinator(DevoloDataUpdateCoordinator[list[ConnectedStationInfo]]):
    update_method: Incomplete
    def __init__(self, hass: HomeAssistant, logger: Logger, *, config_entry: ConfigEntry, name: str = ..., update_interval: timedelta | None = ...) -> None: ...
    async def async_get_wifi_connected_station(self) -> list[ConnectedStationInfo]: ...

class DevoloWifiGuestAccessGetCoordinator(DevoloDataUpdateCoordinator[WifiGuestAccessGet]):
    update_method: Incomplete
    def __init__(self, hass: HomeAssistant, logger: Logger, *, config_entry: ConfigEntry, name: str = ..., update_interval: timedelta | None = ...) -> None: ...
    async def async_update_guest_wifi_status(self) -> WifiGuestAccessGet: ...

class DevoloWifiNeighborAPsGetCoordinator(DevoloDataUpdateCoordinator[list[NeighborAPInfo]]):
    update_method: Incomplete
    def __init__(self, hass: HomeAssistant, logger: Logger, *, config_entry: ConfigEntry, name: str = ..., update_interval: timedelta | None = ...) -> None: ...
    async def async_update_wifi_neighbor_access_points(self) -> list[NeighborAPInfo]: ...

@dataclass
class DevoloHomeNetworkData:
    device: Device
    coordinators: dict[str, DevoloDataUpdateCoordinator[Any]]
