from .const import CONF_GENERATION as CONF_GENERATION, CONF_SERIAL_NUMBER as CONF_SERIAL_NUMBER, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, SENSOR_KEYS as SENSOR_KEYS
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from indevolt_api import IndevoltEnergyMode, IndevoltRealtimeAction
from typing import Any, Final, override

_LOGGER: Incomplete
SCAN_BATCH_SIZE: Final[int]
SCAN_INTERVAL: Final[int]
type IndevoltConfigEntry = ConfigEntry[IndevoltCoordinator]

class IndevoltCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    friendly_name: str
    config_entry: IndevoltConfigEntry
    firmware_version: str | None
    mac_address: str | None
    serial_number: str
    device_model: str
    generation: int
    api: Incomplete
    def __init__(self, hass: HomeAssistant, entry: IndevoltConfigEntry) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    @override
    async def _async_update_data(self) -> dict[str, Any]: ...
    async def async_push_data(self, sensor_key: str, value: Any) -> bool: ...
    def async_optimistic_update(self, read_key: str, value: Any) -> None: ...
    async def async_switch_energy_mode(self, target_mode: IndevoltEnergyMode, refresh: bool = True) -> None: ...
    async def async_realtime_action(self, action: IndevoltRealtimeAction, power: int = 0, target_soc: int = 0) -> None: ...
    def get_emergency_soc(self) -> int: ...
