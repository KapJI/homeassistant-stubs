import abc
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import timedelta
from habiticalib import Avatar as Avatar, ContentData as ContentData, GroupData as GroupData, Habitica as Habitica, TaskData as TaskData, UserData as UserData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any
from uuid import UUID

_LOGGER: Incomplete

@dataclass
class HabiticaData:
    user: UserData
    tasks: list[TaskData]

@dataclass
class HabiticaPartyData:
    party: GroupData
    members: dict[UUID, UserData]
type HabiticaConfigEntry = ConfigEntry[HabiticaDataUpdateCoordinator]

class HabiticaBaseCoordinator[_DataT](DataUpdateCoordinator[_DataT], metaclass=abc.ABCMeta):
    config_entry: HabiticaConfigEntry
    _update_interval: timedelta
    habitica: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: HabiticaConfigEntry, habitica: Habitica) -> None: ...
    @abstractmethod
    async def _update_data(self) -> _DataT: ...
    async def _async_update_data(self) -> _DataT: ...

class HabiticaDataUpdateCoordinator(HabiticaBaseCoordinator[HabiticaData]):
    _update_interval: Incomplete
    content: ContentData
    async def _async_setup(self) -> None: ...
    async def _update_data(self) -> HabiticaData: ...
    async def execute(self, func: Callable[[Habitica], Any]) -> None: ...
    async def generate_avatar(self, avatar: Avatar) -> bytes: ...

class HabiticaPartyCoordinator(HabiticaBaseCoordinator[HabiticaPartyData]):
    _update_interval: Incomplete
    async def _update_data(self) -> HabiticaPartyData: ...
