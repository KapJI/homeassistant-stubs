from .const import CONF_USE_AUX1 as CONF_USE_AUX1, CONF_USE_AUX2 as CONF_USE_AUX2, CONF_USE_AUX3 as CONF_USE_AUX3, CONF_USE_AUX4 as CONF_USE_AUX4, CONF_USE_LIGHT as CONF_USE_LIGHT, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, FOLLOW_UP_REFRESH_DELAY as FOLLOW_UP_REFRESH_DELAY
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from neopool_modbus import NeoPoolModbusClient as NeoPoolModbusClient
from typing import Any, override

_LOGGER: Incomplete
_AUX_TIMER_BLOCKS: dict[str, str]
type NeoPoolConfigEntry = ConfigEntry['NeoPoolCoordinator']

class NeoPoolCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    client: NeoPoolModbusClient
    config_entry: NeoPoolConfigEntry
    _corrupted_gpio_state: frozenset[tuple[str, int]] | None
    _follow_up_unsub: CALLBACK_TYPE | None
    def __init__(self, hass: HomeAssistant, client: NeoPoolModbusClient, entry: NeoPoolConfigEntry) -> None: ...
    def request_refresh_with_followup(self, delay: float = ...) -> None: ...
    def cancel_follow_up_refresh(self) -> None: ...
    def _check_gpio_registers(self, data: dict[str, Any]) -> None: ...
    def _get_enabled_timers(self, data: dict[str, Any]) -> list[str]: ...
    async def _read_timers_into_data(self, data: dict[str, Any]) -> None: ...
    @override
    async def _async_update_data(self) -> dict[str, Any]: ...
