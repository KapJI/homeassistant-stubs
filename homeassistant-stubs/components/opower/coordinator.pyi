from .const import CONF_LOGIN_DATA as CONF_LOGIN_DATA, CONF_TOTP_SECRET as CONF_TOTP_SECRET, CONF_UTILITY as CONF_UTILITY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.recorder.models import StatisticData as StatisticData, StatisticMeanType as StatisticMeanType, StatisticMetaData as StatisticMetaData
from homeassistant.components.recorder.statistics import async_add_external_statistics as async_add_external_statistics, get_last_statistics as get_last_statistics, statistics_during_period as statistics_during_period
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, UnitOfEnergy as UnitOfEnergy, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.unit_conversion import EnergyConverter as EnergyConverter, VolumeConverter as VolumeConverter
from opower import Account as Account, CostRead as CostRead, Forecast

_LOGGER: Incomplete
type OpowerConfigEntry = ConfigEntry[OpowerCoordinator]

class OpowerCoordinator(DataUpdateCoordinator[dict[str, Forecast]]):
    config_entry: OpowerConfigEntry
    api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: OpowerConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, Forecast]: ...
    async def _insert_statistics(self) -> None: ...
    async def _async_maybe_migrate_statistics(self, utility_account_id: str, migration_map: dict[str, str], metadata_map: dict[str, StatisticMetaData]) -> bool: ...
    async def _async_get_cost_reads(self, account: Account, time_zone_str: str, start_time: float | None = None) -> list[CostRead]: ...
