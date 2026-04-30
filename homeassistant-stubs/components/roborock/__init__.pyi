from .const import CONF_BASE_URL as CONF_BASE_URL, CONF_SHOW_BACKGROUND as CONF_SHOW_BACKGROUND, CONF_SHOW_ROOMS as CONF_SHOW_ROOMS, CONF_SHOW_WALLS as CONF_SHOW_WALLS, CONF_USER_DATA as CONF_USER_DATA, DEFAULT_DRAWABLES as DEFAULT_DRAWABLES, DOMAIN as DOMAIN, DRAWABLES as DRAWABLES, MAP_SCALE as MAP_SCALE, PLATFORMS as PLATFORMS
from .coordinator import RoborockB01Q10UpdateCoordinator as RoborockB01Q10UpdateCoordinator, RoborockB01Q7UpdateCoordinator as RoborockB01Q7UpdateCoordinator, RoborockConfigEntry as RoborockConfigEntry, RoborockCoordinators as RoborockCoordinators, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator, RoborockDataUpdateCoordinatorA01 as RoborockDataUpdateCoordinatorA01, RoborockDataUpdateCoordinatorB01 as RoborockDataUpdateCoordinatorB01, RoborockWashingMachineUpdateCoordinator as RoborockWashingMachineUpdateCoordinator, RoborockWetDryVacUpdateCoordinator as RoborockWetDryVacUpdateCoordinator
from .models import get_device_info as get_device_info
from .roborock_storage import CacheStore as CacheStore, async_cleanup_map_storage as async_cleanup_map_storage
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from collections.abc import Coroutine
from homeassistant.const import CONF_USERNAME as CONF_USERNAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType
from roborock.data import UserData
from roborock.devices.device import RoborockDevice as RoborockDevice
from typing import Any

CONFIG_SCHEMA: Incomplete
SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: RoborockConfigEntry) -> bool: ...
def _is_device_disabled(device_registry: dr.DeviceRegistry, device: RoborockDevice) -> bool: ...
def _remove_stale_devices(hass: HomeAssistant, entry: RoborockConfigEntry, devices: list[RoborockDevice]) -> None: ...
async def async_migrate_entry(hass: HomeAssistant, entry: RoborockConfigEntry) -> bool: ...
def build_setup_functions(hass: HomeAssistant, entry: RoborockConfigEntry, devices: list[RoborockDevice], user_data: UserData) -> list[Coroutine[Any, Any, RoborockDataUpdateCoordinator | RoborockDataUpdateCoordinatorA01 | RoborockDataUpdateCoordinatorB01 | RoborockB01Q10UpdateCoordinator | None]]: ...
async def setup_coordinator(coordinator: RoborockDataUpdateCoordinator | RoborockDataUpdateCoordinatorA01 | RoborockDataUpdateCoordinatorB01 | RoborockB01Q10UpdateCoordinator) -> RoborockDataUpdateCoordinator | RoborockDataUpdateCoordinatorA01 | RoborockDataUpdateCoordinatorB01 | RoborockB01Q10UpdateCoordinator | None: ...
async def async_unload_entry(hass: HomeAssistant, entry: RoborockConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: RoborockConfigEntry) -> None: ...
