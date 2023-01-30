import abc
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from jellyfin_apiclient_python import JellyfinClient as JellyfinClient
from typing import Any, TypeVar

JellyfinDataT = TypeVar('JellyfinDataT', bound=dict[str, dict[str, Any]] | dict[str, Any])

class JellyfinDataUpdateCoordinator(DataUpdateCoordinator[JellyfinDataT], ABC, metaclass=abc.ABCMeta):
    config_entry: ConfigEntry
    api_client: Incomplete
    server_id: Incomplete
    server_name: Incomplete
    server_version: Incomplete
    user_id: Incomplete
    def __init__(self, hass: HomeAssistant, api_client: JellyfinClient, system_info: dict[str, Any], user_id: str) -> None: ...
    async def _async_update_data(self) -> JellyfinDataT: ...
    @abstractmethod
    async def _fetch_data(self) -> JellyfinDataT: ...

class SessionsDataUpdateCoordinator(JellyfinDataUpdateCoordinator[dict[str, dict[str, Any]]]):
    async def _fetch_data(self) -> dict[str, dict[str, Any]]: ...
