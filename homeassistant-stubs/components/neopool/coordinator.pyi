from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from neopool_modbus import NeoPoolModbusClient as NeoPoolModbusClient
from typing import Any, override

_LOGGER: Incomplete
type NeoPoolConfigEntry = ConfigEntry['NeoPoolCoordinator']

class NeoPoolCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    client: NeoPoolModbusClient
    config_entry: NeoPoolConfigEntry
    _corrupted_gpio_state: frozenset[tuple[str, int]] | None
    def __init__(self, hass: HomeAssistant, client: NeoPoolModbusClient, entry: NeoPoolConfigEntry) -> None: ...
    def _check_gpio_registers(self, data: dict[str, Any]) -> None: ...
    @override
    async def _async_update_data(self) -> dict[str, Any]: ...
