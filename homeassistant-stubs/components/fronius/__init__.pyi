from .const import DOMAIN as DOMAIN, FroniusDeviceInfo as FroniusDeviceInfo, SOLAR_NET_DISCOVERY_NEW as SOLAR_NET_DISCOVERY_NEW, SOLAR_NET_ID_SYSTEM as SOLAR_NET_ID_SYSTEM, SOLAR_NET_RESCAN_TIMER as SOLAR_NET_RESCAN_TIMER
from .coordinator import FroniusCoordinatorBase as FroniusCoordinatorBase, FroniusInverterUpdateCoordinator as FroniusInverterUpdateCoordinator, FroniusLoggerUpdateCoordinator as FroniusLoggerUpdateCoordinator, FroniusMeterUpdateCoordinator as FroniusMeterUpdateCoordinator, FroniusOhmpilotUpdateCoordinator as FroniusOhmpilotUpdateCoordinator, FroniusPowerFlowUpdateCoordinator as FroniusPowerFlowUpdateCoordinator, FroniusStorageUpdateCoordinator as FroniusStorageUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from pyfronius import Fronius
from typing import Final, TypeVar

_LOGGER: Final[Incomplete]
PLATFORMS: Final[Incomplete]
_FroniusCoordinatorT = TypeVar('_FroniusCoordinatorT', bound=FroniusCoordinatorBase)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class FroniusSolarNet:
    hass: Incomplete
    cleanup_callbacks: Incomplete
    config_entry: Incomplete
    coordinator_lock: Incomplete
    fronius: Incomplete
    host: Incomplete
    solar_net_device_id: Incomplete
    system_device_info: Incomplete
    inverter_coordinators: Incomplete
    logger_coordinator: Incomplete
    meter_coordinator: Incomplete
    ohmpilot_coordinator: Incomplete
    power_flow_coordinator: Incomplete
    storage_coordinator: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, fronius: Fronius) -> None: ...
    async def init_devices(self) -> None: ...
    async def _create_solar_net_device(self) -> DeviceInfo: ...
    async def _init_devices_inverter(self, _now: datetime | None = ...) -> None: ...
    async def _get_inverter_infos(self) -> list[FroniusDeviceInfo]: ...
    @staticmethod
    async def _init_optional_coordinator(coordinator: _FroniusCoordinatorT) -> _FroniusCoordinatorT | None: ...
