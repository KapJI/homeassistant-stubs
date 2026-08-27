from .const import CONF_FW_VERSION as CONF_FW_VERSION, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aio_wattwaechter import Wattwaechter as Wattwaechter
from aio_wattwaechter.models import MeterData as MeterData, OtaData as OtaData, SystemInfo as SystemInfo
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_MODEL as CONF_MODEL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete
type WattwaechterConfigEntry = ConfigEntry[WattwaechterCoordinator]

@dataclass
class WattwaechterData:
    meter: MeterData
    system: SystemInfo | None
    ota: OtaData | None

class WattwaechterCoordinator(DataUpdateCoordinator[WattwaechterData]):
    config_entry: WattwaechterConfigEntry
    client: Incomplete
    device_id: str
    host: str
    model: str | None
    mac: str
    fw_version: str | None
    def __init__(self, hass: HomeAssistant, config_entry: WattwaechterConfigEntry, client: Wattwaechter) -> None: ...
    @override
    async def _async_update_data(self) -> WattwaechterData: ...
