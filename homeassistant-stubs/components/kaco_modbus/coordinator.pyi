from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from kaco_modbus import KacoInverter as KacoInverter, UpdateReport
from propcache.api import cached_property
from typing import override

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
type KacoConfigEntry = ConfigEntry[KacoDataUpdateCoordinator]

class KacoDataUpdateCoordinator(DataUpdateCoordinator[UpdateReport]):
    config_entry: KacoConfigEntry
    device: Incomplete
    def __init__(self, hass: HomeAssistant, entry: KacoConfigEntry, device: KacoInverter) -> None: ...
    @cached_property
    def device_info(self) -> DeviceInfo: ...
    @override
    async def _async_update_data(self) -> UpdateReport: ...
