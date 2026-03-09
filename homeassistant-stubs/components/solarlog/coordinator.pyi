from .const import DOMAIN as DOMAIN
from .models import SolarlogIntegrationData as SolarlogIntegrationData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util import slugify as slugify
from solarlog_cli.solarlog_connector import SolarLogConnector as SolarLogConnector
from solarlog_cli.solarlog_models import EnergyData, InverterData, SolarlogData

_LOGGER: Incomplete
type SolarlogConfigEntry = ConfigEntry[SolarlogIntegrationData]

class SolarLogBasicDataCoordinator(DataUpdateCoordinator[SolarlogData]):
    config_entry: SolarlogConfigEntry
    unique_id: Incomplete
    solarlog: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: SolarlogConfigEntry, api: SolarLogConnector) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> SolarlogData: ...
    async def renew_authentication(self) -> bool: ...

class SolarLogDeviceDataCoordinator(DataUpdateCoordinator[dict[int, InverterData]]):
    config_entry: SolarlogConfigEntry
    new_device_callbacks: list[Callable[[int], None]]
    _devices_last_update: set[tuple[int, str]]
    solarlog: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: SolarlogConfigEntry, api: SolarLogConnector) -> None: ...
    data: Incomplete
    async def _async_update_data(self) -> dict[int, InverterData]: ...
    def _async_add_remove_devices(self, inverter_data: dict[int, InverterData]) -> None: ...

class SolarLogLongtimeDataCoordinator(DataUpdateCoordinator[EnergyData]):
    config_entry: SolarlogConfigEntry
    solarlog: Incomplete
    connection_timeout: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: SolarlogConfigEntry, api: SolarLogConnector, timeout: float) -> None: ...
    async def _async_update_data(self) -> EnergyData: ...
