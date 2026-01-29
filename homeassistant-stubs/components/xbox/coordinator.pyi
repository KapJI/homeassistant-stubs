import abc
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pythonxbox.api.client import XboxLiveClient as XboxLiveClient
from pythonxbox.api.provider.catalog.models import Product as Product
from pythonxbox.api.provider.people.models import Person as Person
from pythonxbox.api.provider.smartglass.models import SmartglassConsole, SmartglassConsoleStatus as SmartglassConsoleStatus
from pythonxbox.api.provider.titlehub.models import Title as Title
from typing import ClassVar

_LOGGER: Incomplete
type XboxConfigEntry = ConfigEntry[XboxCoordinators]

@dataclass
class ConsoleData:
    status: SmartglassConsoleStatus
    app_details: Product | None

@dataclass
class XboxData:
    presence: dict[str, Person] = field(default_factory=dict)
    title_info: dict[str, Title] = field(default_factory=dict)

@dataclass
class XboxCoordinators:
    consoles: XboxConsolesCoordinator
    status: XboxConsoleStatusCoordinator
    presence: XboxPresenceCoordinator

class XboxBaseCoordinator[_DataT](DataUpdateCoordinator[_DataT], metaclass=abc.ABCMeta):
    config_entry: XboxConfigEntry
    _update_inverval: timedelta
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: XboxConfigEntry, client: XboxLiveClient) -> None: ...
    @abstractmethod
    async def update_data(self) -> _DataT: ...
    async def _async_update_data(self) -> _DataT: ...

class XboxConsolesCoordinator(XboxBaseCoordinator[dict[str, SmartglassConsole]]):
    config_entry: XboxConfigEntry
    _update_interval: Incomplete
    async def update_data(self) -> dict[str, SmartglassConsole]: ...

class XboxConsoleStatusCoordinator(XboxBaseCoordinator[dict[str, ConsoleData]]):
    config_entry: XboxConfigEntry
    _update_interval: Incomplete
    data: dict[str, ConsoleData]
    consoles: dict[str, SmartglassConsole] | None
    def __init__(self, hass: HomeAssistant, config_entry: XboxConfigEntry, client: XboxLiveClient, consoles: dict[str, SmartglassConsole]) -> None: ...
    async def update_data(self) -> dict[str, ConsoleData]: ...

class XboxPresenceCoordinator(XboxBaseCoordinator[XboxData]):
    config_entry: XboxConfigEntry
    _update_interval: Incomplete
    title_data: ClassVar[dict[str, Title]]
    async def update_data(self) -> XboxData: ...
    def last_seen_timestamp(self, person: Person) -> datetime | None: ...
    def friend_subentries(self) -> set[str]: ...
