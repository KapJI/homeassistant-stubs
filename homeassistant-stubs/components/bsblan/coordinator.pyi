from . import BSBLanConfigEntry as BSBLanConfigEntry
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL_FAST as SCAN_INTERVAL_FAST, SCAN_INTERVAL_SLOW as SCAN_INTERVAL_SLOW
from _typeshed import Incomplete
from bsblan import BSBLAN as BSBLAN, HotWaterConfig as HotWaterConfig, HotWaterSchedule as HotWaterSchedule, HotWaterState as HotWaterState, Sensor as Sensor, State as State
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

STATE_INCLUDE: Incomplete
SENSOR_INCLUDE: Incomplete
DHW_STATE_INCLUDE: Incomplete
DHW_CONFIG_INCLUDE: Incomplete

@dataclass
class BSBLanFastData:
    states: dict[int, State]
    sensor: Sensor
    dhw: HotWaterState | None = ...

@dataclass
class BSBLanSlowData:
    dhw_config: HotWaterConfig | None = ...
    dhw_schedule: HotWaterSchedule | None = ...

class BSBLanCoordinator[T](DataUpdateCoordinator[T]):
    config_entry: BSBLanConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: BSBLanConfigEntry, client: BSBLAN, name: str, update_interval: timedelta) -> None: ...

class BSBLanFastCoordinator(BSBLanCoordinator[BSBLanFastData]):
    circuits: list[int]
    def __init__(self, hass: HomeAssistant, config_entry: BSBLanConfigEntry, client: BSBLAN, circuits: list[int]) -> None: ...
    @override
    async def _async_update_data(self) -> BSBLanFastData: ...

class BSBLanSlowCoordinator(BSBLanCoordinator[BSBLanSlowData]):
    _dhw_schedule_refresh_pending: bool
    _dhw_schedule_refresh_generation: int
    def __init__(self, hass: HomeAssistant, config_entry: BSBLanConfigEntry, client: BSBLAN) -> None: ...
    @override
    async def _async_update_data(self) -> BSBLanSlowData: ...
    async def async_refresh_schedule_after_write(self) -> None: ...
    async def _async_fetch_dhw_schedule(self) -> tuple[HotWaterSchedule | None, bool]: ...
