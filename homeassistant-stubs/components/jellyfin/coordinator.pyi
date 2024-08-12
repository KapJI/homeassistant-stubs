import abc
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, USER_APP_NAME as USER_APP_NAME
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from jellyfin_apiclient_python import JellyfinClient as JellyfinClient
from typing import Any, TypeVar

JellyfinDataT = TypeVar('JellyfinDataT', bound=dict[str, dict[str, Any]] | dict[str, Any])

class JellyfinDataUpdateCoordinator(DataUpdateCoordinator[JellyfinDataT], ABC, metaclass=abc.ABCMeta):
    api_client: Incomplete
    server_id: Incomplete
    server_name: Incomplete
    server_version: Incomplete
    client_device_id: Incomplete
    user_id: Incomplete
    session_ids: Incomplete
    device_ids: Incomplete
    def __init__(self, hass: HomeAssistant, api_client: JellyfinClient, system_info: dict[str, Any], client_device_id: str, user_id: str) -> None: ...
    async def _async_update_data(self) -> JellyfinDataT: ...
    @abstractmethod
    async def _fetch_data(self) -> JellyfinDataT: ...

class SessionsDataUpdateCoordinator(JellyfinDataUpdateCoordinator[dict[str, dict[str, Any]]]):
    device_ids: Incomplete
    async def _fetch_data(self) -> dict[str, dict[str, Any]]: ...
