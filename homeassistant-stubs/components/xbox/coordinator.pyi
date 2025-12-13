from . import api as api
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass, field
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.config_entry_oauth2_flow import ImplementationUnavailableError as ImplementationUnavailableError, OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pythonxbox.api.client import XboxLiveClient
from pythonxbox.api.provider.catalog.models import Product as Product
from pythonxbox.api.provider.people.models import Person as Person
from pythonxbox.api.provider.smartglass.models import SmartglassConsoleList, SmartglassConsoleStatus as SmartglassConsoleStatus
from pythonxbox.api.provider.titlehub.models import Title as Title

_LOGGER: Incomplete
type XboxConfigEntry = ConfigEntry[XboxCoordinators]

@dataclass
class ConsoleData:
    status: SmartglassConsoleStatus
    app_details: Product | None

@dataclass
class XboxData:
    consoles: dict[str, ConsoleData] = field(default_factory=dict)
    presence: dict[str, Person] = field(default_factory=dict)
    title_info: dict[str, Title] = field(default_factory=dict)

@dataclass
class XboxCoordinators:
    status: XboxUpdateCoordinator
    consoles: XboxConsolesCoordinator

class XboxUpdateCoordinator(DataUpdateCoordinator[XboxData]):
    config_entry: XboxConfigEntry
    consoles: SmartglassConsoleList
    client: XboxLiveClient
    data: Incomplete
    current_friends: set[str]
    title_data: dict[str, Title]
    def __init__(self, hass: HomeAssistant, config_entry: XboxConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> XboxData: ...
    def last_seen_timestamp(self, person: Person) -> datetime | None: ...
    def remove_stale_devices(self, xuids: set[str]) -> None: ...
    def configured_as_entry(self) -> set[str]: ...

class XboxConsolesCoordinator(DataUpdateCoordinator[SmartglassConsoleList]):
    config_entry: XboxConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: XboxConfigEntry, coordinator: XboxUpdateCoordinator) -> None: ...
    async def _async_update_data(self) -> SmartglassConsoleList: ...
