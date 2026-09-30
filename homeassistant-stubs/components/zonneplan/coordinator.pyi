from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import date
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyzonneplan import Account as Account, Connection as Connection, ConsumerPrices as ConsumerPrices, ElectricityChart as ElectricityChart, GasChart as GasChart, Zonneplan as Zonneplan
from typing import override

LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete
type ZonneplanConfigEntry = ConfigEntry[ZonneplanCoordinator]

@dataclass(frozen=True, kw_only=True)
class ZonneplanData:
    account: Account
    electricity_prices: ConsumerPrices | None = ...
    gas_prices: ConsumerPrices | None = ...
    electricity_usage: ElectricityChart | None = ...
    gas_usage: GasChart | None = ...

def _connection(account: Account, market_segment: str) -> Connection | None: ...

class ZonneplanCoordinator(DataUpdateCoordinator[ZonneplanData]):
    config_entry: ZonneplanConfigEntry
    zonneplan: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ZonneplanConfigEntry, zonneplan: Zonneplan) -> None: ...
    async def _async_fetch_electricity(self, account: Account, today: date) -> tuple[ConsumerPrices | None, ElectricityChart | None]: ...
    async def _async_fetch_gas(self, account: Account, today: date) -> tuple[ConsumerPrices | None, GasChart | None]: ...
    @override
    async def _async_update_data(self) -> ZonneplanData: ...
