from .config_flow import get_client_controller as get_client_controller
from .const import CONF_ALLOW_INACTIVE_ZONES_TO_RUN as CONF_ALLOW_INACTIVE_ZONES_TO_RUN, CONF_DEFAULT_ZONE_RUN_TIME as CONF_DEFAULT_ZONE_RUN_TIME, CONF_USE_APP_RUN_TIMES as CONF_USE_APP_RUN_TIMES, DATA_API_VERSIONS as DATA_API_VERSIONS, DATA_MACHINE_FIRMWARE_UPDATE_STATUS as DATA_MACHINE_FIRMWARE_UPDATE_STATUS, DATA_PROGRAMS as DATA_PROGRAMS, DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DATA_RESTRICTIONS_CURRENT as DATA_RESTRICTIONS_CURRENT, DATA_RESTRICTIONS_UNIVERSAL as DATA_RESTRICTIONS_UNIVERSAL, DATA_ZONES as DATA_ZONES, DEFAULT_ZONE_RUN as DEFAULT_ZONE_RUN, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import RainMachineDataUpdateCoordinator as RainMachineDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import UpdateFailed as UpdateFailed
from homeassistant.util.network import is_ip_address as is_ip_address
from regenmaschine.controller import Controller as Controller

DEFAULT_SSL: bool
PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete
COORDINATOR_UPDATE_INTERVAL_MAP: Incomplete
type RainMachineConfigEntry = ConfigEntry[RainMachineData]

@dataclass
class RainMachineData:
    controller: Controller
    coordinators: dict[str, RainMachineDataUpdateCoordinator]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: RainMachineConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: RainMachineConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: RainMachineConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: RainMachineConfigEntry) -> None: ...
