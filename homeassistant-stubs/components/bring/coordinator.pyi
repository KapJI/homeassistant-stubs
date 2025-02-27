from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from bring_api import Bring as Bring, BringActivityResponse as BringActivityResponse, BringItemsResponse as BringItemsResponse, BringList as BringList, BringUserSettingsResponse as BringUserSettingsResponse, BringUsersResponse as BringUsersResponse
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EMAIL as CONF_EMAIL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from mashumaro.mixins.orjson import DataClassORJSONMixin

_LOGGER: Incomplete
type BringConfigEntry = ConfigEntry[BringDataUpdateCoordinator]

@dataclass(frozen=True)
class BringData(DataClassORJSONMixin):
    lst: BringList
    content: BringItemsResponse
    activity: BringActivityResponse
    users: BringUsersResponse

class BringDataUpdateCoordinator(DataUpdateCoordinator[dict[str, BringData]]):
    config_entry: BringConfigEntry
    user_settings: BringUserSettingsResponse
    lists: list[BringList]
    bring: Incomplete
    previous_lists: set[str]
    def __init__(self, hass: HomeAssistant, config_entry: BringConfigEntry, bring: Bring) -> None: ...
    async def _async_update_data(self) -> dict[str, BringData]: ...
    async def _async_setup(self) -> None: ...
    def _purge_deleted_lists(self) -> None: ...
