from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from sunsynk.battery import Battery as Battery
from sunsynk.client import SunsynkClient as SunsynkClient
from sunsynk.grid import Grid as Grid
from sunsynk.input import Input as Input
from sunsynk.inverter import Inverter as Inverter
from sunsynk.load import Load as Load
from typing import override

type SunsynkConfigEntry = ConfigEntry[list[SunsynkDataUpdateCoordinator]]
@dataclass
class SunsynkInverterData:
    battery: Battery
    grid: Grid
    load: Load
    solar: Input

class SunsynkDataUpdateCoordinator(DataUpdateCoordinator[SunsynkInverterData]):
    config_entry: SunsynkConfigEntry
    client: Incomplete
    inverter: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: SunsynkConfigEntry, client: SunsynkClient, inverter: Inverter) -> None: ...
    @override
    async def _async_update_data(self) -> SunsynkInverterData: ...
