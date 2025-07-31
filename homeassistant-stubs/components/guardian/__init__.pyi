import asyncio
from .const import API_SENSOR_PAIRED_SENSOR_STATUS as API_SENSOR_PAIRED_SENSOR_STATUS, API_SENSOR_PAIR_DUMP as API_SENSOR_PAIR_DUMP, API_SYSTEM_DIAGNOSTICS as API_SYSTEM_DIAGNOSTICS, API_SYSTEM_ONBOARD_SENSOR_STATUS as API_SYSTEM_ONBOARD_SENSOR_STATUS, API_VALVE_STATUS as API_VALVE_STATUS, API_WIFI_STATUS as API_WIFI_STATUS, CONF_UID as CONF_UID, DOMAIN as DOMAIN, LOGGER as LOGGER, SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED as SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED
from .coordinator import GuardianDataUpdateCoordinator as GuardianDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from aioguardian import Client
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete
type GuardianConfigEntry = ConfigEntry[GuardianData]

@dataclass
class GuardianData:
    entry: GuardianConfigEntry
    client: Client
    valve_controller_coordinators: dict[str, GuardianDataUpdateCoordinator]
    paired_sensor_manager: PairedSensorManager

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: GuardianConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GuardianConfigEntry) -> bool: ...

class PairedSensorManager:
    _api_lock: Incomplete
    _client: Incomplete
    _entry: Incomplete
    _hass: Incomplete
    _paired_uids: set[str]
    _sensor_pair_dump_coordinator: Incomplete
    coordinators: dict[str, GuardianDataUpdateCoordinator]
    def __init__(self, hass: HomeAssistant, entry: GuardianConfigEntry, client: Client, api_lock: asyncio.Lock, sensor_pair_dump_coordinator: GuardianDataUpdateCoordinator) -> None: ...
    async def async_initialize(self) -> None: ...
    async def async_pair_sensor(self, uid: str) -> None: ...
    async def async_process_latest_paired_sensor_uids(self) -> None: ...
    async def async_unpair_sensor(self, uid: str) -> None: ...
