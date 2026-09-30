from .const import DOMAIN as DOMAIN, FIRMWARE_SCAN_INTERVAL as FIRMWARE_SCAN_INTERVAL, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from dataclasses import dataclass
from elgato import BatteryInfo as BatteryInfo, FirmwareVersion, Info as Info, Settings as Settings, State as State
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

type ElgatoConfigEntry = ConfigEntry[ElgatoDataUpdateCoordinator]
@dataclass
class ElgatoData:
    battery: BatteryInfo | None
    info: Info
    settings: Settings
    state: State

class ElgatoDataUpdateCoordinator(DataUpdateCoordinator[ElgatoData]):
    config_entry: ElgatoConfigEntry
    has_battery: bool | None
    client: Incomplete
    device_lock: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ElgatoConfigEntry) -> None: ...
    @override
    async def _async_update_data(self) -> ElgatoData: ...

class ElgatoFirmwareCoordinator(DataUpdateCoordinator[dict[int, FirmwareVersion]]):
    catalog: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @override
    async def _async_update_data(self) -> dict[int, FirmwareVersion]: ...
