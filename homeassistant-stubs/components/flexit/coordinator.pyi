import logging
from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from modbus_connection import ModbusUnit as ModbusUnit
from typing import override

_LOGGER: logging.Logger
type FlexitConfigEntry = ConfigEntry[FlexitDataCoordinator]

class FlexitDataCoordinator(DataUpdateCoordinator[None]):
    device: Incomplete
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, entry: FlexitConfigEntry, unit: ModbusUnit) -> None: ...
    @override
    async def _async_update_data(self) -> None: ...
