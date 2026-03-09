from . import GhostConfigEntry as GhostConfigEntry
from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioghost import GhostAdminAPI as GhostAdminAPI
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Incomplete

@dataclass
class GhostData:
    site: dict[str, Any]
    posts: dict[str, Any]
    members: dict[str, Any]
    latest_post: dict[str, Any] | None
    latest_email: dict[str, Any] | None
    activitypub: dict[str, Any]
    mrr: dict[str, Any]
    arr: dict[str, Any]
    comments: int
    newsletters: dict[str, dict[str, Any]]

class GhostDataUpdateCoordinator(DataUpdateCoordinator[GhostData]):
    config_entry: GhostConfigEntry
    api: Incomplete
    def __init__(self, hass: HomeAssistant, api: GhostAdminAPI, config_entry: GhostConfigEntry) -> None: ...
    async def _async_update_data(self) -> GhostData: ...
