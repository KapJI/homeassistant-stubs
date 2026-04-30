import dataclasses
from .const import CONF_HEATING_CIRCUITS as CONF_HEATING_CIRCUITS, CONF_PASSKEY as CONF_PASSKEY, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import BSBLanFastCoordinator as BSBLanFastCoordinator, BSBLanSlowCoordinator as BSBLanSlowCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from bsblan import BSBLAN, Device as Device, Info as Info, StaticState as StaticState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete
type BSBLanConfigEntry = ConfigEntry[BSBLanData]

@dataclasses.dataclass
class BSBLanData:
    fast_coordinator: BSBLanFastCoordinator
    slow_coordinator: BSBLanSlowCoordinator
    client: BSBLAN
    device: Device
    info: Info
    static: dict[int, StaticState | None]
    available_circuits: list[int]

def get_bsblan_device_info(device: Device, info: Info, host: str, port: int) -> DeviceInfo: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: BSBLanConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BSBLanConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: BSBLanConfigEntry) -> bool: ...
