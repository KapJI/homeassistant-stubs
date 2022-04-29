from .const import DOMAIN as DOMAIN, FroniusDeviceInfo as FroniusDeviceInfo, SOLAR_NET_ID_SYSTEM as SOLAR_NET_ID_SYSTEM
from .coordinator import FroniusCoordinatorBase as FroniusCoordinatorBase, FroniusInverterUpdateCoordinator as FroniusInverterUpdateCoordinator, FroniusLoggerUpdateCoordinator as FroniusLoggerUpdateCoordinator, FroniusMeterUpdateCoordinator as FroniusMeterUpdateCoordinator, FroniusOhmpilotUpdateCoordinator as FroniusOhmpilotUpdateCoordinator, FroniusPowerFlowUpdateCoordinator as FroniusPowerFlowUpdateCoordinator, FroniusStorageUpdateCoordinator as FroniusStorageUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
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
    async def _get_inverter_infos(self) -> list[FroniusDeviceInfo]: ...
    @staticmethod
    async def _init_optional_coordinator(coordinator: _FroniusCoordinatorT) -> Union[_FroniusCoordinatorT, None]: ...
