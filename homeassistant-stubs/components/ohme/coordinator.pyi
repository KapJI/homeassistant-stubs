import abc
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import abstractmethod
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from ohme import OhmeApiClient as OhmeApiClient

_LOGGER: Incomplete

@dataclass()
class OhmeRuntimeData:
    charge_session_coordinator: OhmeChargeSessionCoordinator
    advanced_settings_coordinator: OhmeAdvancedSettingsCoordinator
    device_info_coordinator: OhmeDeviceInfoCoordinator
type OhmeConfigEntry = ConfigEntry[OhmeRuntimeData]

class OhmeBaseCoordinator(DataUpdateCoordinator[None], metaclass=abc.ABCMeta):
    config_entry: OhmeConfigEntry
    client: OhmeApiClient
    _default_update_interval: timedelta | None
    coordinator_name: str
    name: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: OhmeConfigEntry, client: OhmeApiClient) -> None: ...
    async def _async_update_data(self) -> None: ...
    @abstractmethod
    async def _internal_update_data(self) -> None: ...

class OhmeChargeSessionCoordinator(OhmeBaseCoordinator):
    coordinator_name: str
    _default_update_interval: Incomplete
    async def _internal_update_data(self) -> None: ...

class OhmeAdvancedSettingsCoordinator(OhmeBaseCoordinator):
    coordinator_name: str
    async def _internal_update_data(self) -> None: ...

class OhmeDeviceInfoCoordinator(OhmeBaseCoordinator):
    coordinator_name: str
    _default_update_interval: Incomplete
    async def _internal_update_data(self) -> None: ...
