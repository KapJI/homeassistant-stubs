from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from habiticalib import Avatar as Avatar, ContentData as ContentData, Habitica as Habitica, TaskData as TaskData, UserData as UserData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Incomplete

@dataclass
class HabiticaData:
    user: UserData
    tasks: list[TaskData]
type HabiticaConfigEntry = ConfigEntry[HabiticaDataUpdateCoordinator]

class HabiticaDataUpdateCoordinator(DataUpdateCoordinator[HabiticaData]):
    config_entry: ConfigEntry
    habitica: Incomplete
    content: ContentData
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, habitica: Habitica) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> HabiticaData: ...
    async def execute(self, func: Callable[[HabiticaDataUpdateCoordinator], Any]) -> None: ...
    async def generate_avatar(self, avatar: Avatar) -> bytes: ...
