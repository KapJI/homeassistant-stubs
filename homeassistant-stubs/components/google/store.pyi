from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from gcal_sync.api import GoogleCalendarService as GoogleCalendarService
from gcal_sync.store import CalendarStore
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.storage import Store as Store
from typing import Any

_LOGGER: Incomplete
STORAGE_KEY_FORMAT: str
STORAGE_VERSION: int
STORAGE_SAVE_DELAY_SECONDS: int
type GoogleConfigEntry = ConfigEntry[GoogleRuntimeData]

@dataclass
class GoogleRuntimeData:
    service: GoogleCalendarService
    store: LocalCalendarStore

class LocalCalendarStore(CalendarStore):
    _store: Incomplete
    _data: dict[str, Any] | None
    def __init__(self, hass: HomeAssistant, entry_id: str) -> None: ...
    async def async_load(self) -> dict[str, Any] | None: ...
    async def async_save(self, data: dict[str, Any]) -> None: ...
    async def async_remove(self) -> None: ...
