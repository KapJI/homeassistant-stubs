from .const import FALLBACK_UPDATE_INTERVAL as FALLBACK_UPDATE_INTERVAL, LOGGER as LOGGER, REFRESH_EVENT_TYPES as REFRESH_EVENT_TYPES
from _typeshed import Incomplete
from aiogithubapi import GitHubAPI as GitHubAPI, GitHubEventModel as GitHubEventModel, GitHubException, GitHubResponseModel as GitHubResponseModel
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

GRAPHQL_REPOSITORY_QUERY: str
type GithubConfigEntry = ConfigEntry[dict[str, GitHubDataUpdateCoordinator]]

class GitHubDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: GithubConfigEntry
    repository: Incomplete
    _client: Incomplete
    _last_response: GitHubResponseModel[dict[str, Any]] | None
    _subscription_id: str | None
    data: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: GithubConfigEntry, client: GitHubAPI, repository: str) -> None: ...
    async def _async_update_data(self) -> GitHubResponseModel[dict[str, Any]]: ...
    async def _handle_event(self, event: GitHubEventModel) -> None: ...
    @staticmethod
    async def _handle_error(error: GitHubException) -> None: ...
    async def subscribe(self) -> None: ...
    def unsubscribe(self, *args: Any) -> None: ...
