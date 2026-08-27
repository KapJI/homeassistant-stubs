from .const import CONF_LIST_ID as CONF_LIST_ID, DOMAIN as DOMAIN, LOGGER as LOGGER, SUBENTRY_TYPE_LIST as SUBENTRY_TYPE_LIST
from _typeshed import Incomplete
from aiortm import AioRTMClient as AioRTMClient
from dataclasses import dataclass
from homeassistant.components.todo import TodoItem as TodoItem, TodoItemStatus as TodoItemStatus
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigSubentry as ConfigSubentry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

UPDATE_INTERVAL: Incomplete

@dataclass(kw_only=True, frozen=True)
class RtmList:
    name: str
    tasks: dict[str, RtmTask]

@dataclass(kw_only=True, frozen=True)
class RtmTask:
    uid: str
    todo_item: TodoItem
    note_id: int | None

@dataclass(kw_only=True, frozen=True)
class RememberTheMilkData:
    entity_id: str
    client: AioRTMClient
    coordinator: RtmTodoCoordinator
type RememberTheMilkConfigEntry = ConfigEntry[RememberTheMilkData]

class RtmTodoCoordinator(DataUpdateCoordinator[dict[int, RtmList]]):
    config_entry: RememberTheMilkConfigEntry
    client: Incomplete
    syncing_subentries: bool
    def __init__(self, hass: HomeAssistant, config_entry: RememberTheMilkConfigEntry, client: AioRTMClient) -> None: ...
    @override
    async def _async_update_data(self) -> dict[int, RtmList]: ...
    async def _async_sync_subentries(self, lists: dict[int, RtmList]) -> None: ...
