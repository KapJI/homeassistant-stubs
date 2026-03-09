from .const import API_DEFAULT_RETRY_AFTER as API_DEFAULT_RETRY_AFTER, APPLIANCES_WITH_PROGRAMS as APPLIANCES_WITH_PROGRAMS, BSH_OPERATION_STATE_PAUSE as BSH_OPERATION_STATE_PAUSE, DOMAIN as DOMAIN
from .utils import get_dict_from_home_connect_error as get_dict_from_home_connect_error
from _typeshed import Incomplete
from aiohomeconnect.client import Client as HomeConnectClient
from aiohomeconnect.model import CommandKey, Event, EventKey, EventMessage as EventMessage, GetSetting, HomeAppliance as HomeAppliance, OptionKey as OptionKey, ProgramKey, SettingKey, Status, StatusKey
from aiohomeconnect.model.program import EnumerateProgram as EnumerateProgram, ProgramDefinitionOption as ProgramDefinitionOption
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
MAX_EXECUTIONS_TIME_WINDOW: Incomplete
MAX_EXECUTIONS: int
type HomeConnectConfigEntry = ConfigEntry[HomeConnectRuntimeData]

@dataclass(frozen=True, kw_only=True)
class HomeConnectApplianceData:
    commands: set[CommandKey]
    events: dict[EventKey, Event]
    info: HomeAppliance
    options: dict[OptionKey, ProgramDefinitionOption]
    programs: list[EnumerateProgram]
    settings: dict[SettingKey, GetSetting]
    status: dict[StatusKey, Status]
    def update(self, other: HomeConnectApplianceData) -> None: ...
    @classmethod
    def empty(cls, appliance: HomeAppliance) -> HomeConnectApplianceData: ...

class HomeConnectRuntimeData:
    config_entry: HomeConnectConfigEntry
    appliance_coordinators: dict[str, HomeConnectApplianceCoordinator]
    hass: Incomplete
    client: Incomplete
    global_listeners: dict[CALLBACK_TYPE, tuple[CALLBACK_TYPE, tuple[EventKey, ...]]]
    device_registry: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: HomeConnectConfigEntry, client: HomeConnectClient) -> None: ...
    @callback
    def start_event_listener(self) -> None: ...
    async def _event_listener(self) -> None: ...
    @callback
    def async_add_global_listener(self, update_callback: CALLBACK_TYPE, context: tuple[EventKey, ...]) -> Callable[[], None]: ...
    async def setup_appliance_coordinators(self) -> None: ...

class HomeConnectApplianceCoordinator(DataUpdateCoordinator[HomeConnectApplianceData]):
    _config_entry: Incomplete
    client: Incomplete
    device_registry: Incomplete
    global_listeners: Incomplete
    data: Incomplete
    _execution_tracker: list[float]
    def __init__(self, hass: HomeAssistant, config_entry: HomeConnectConfigEntry, client: HomeConnectClient, global_listeners: dict[CALLBACK_TYPE, tuple[CALLBACK_TYPE, tuple[EventKey, ...]]], appliance: HomeAppliance) -> None: ...
    def _get_listeners_for_event_key(self, event_key: EventKey) -> list[CALLBACK_TYPE]: ...
    async def event_listener(self, event_message: EventMessage) -> None: ...
    @callback
    def _call_event_listener(self, event_message: EventMessage) -> None: ...
    @callback
    def call_all_event_listeners(self) -> None: ...
    async def _async_update_data(self) -> HomeConnectApplianceData: ...
    async def get_appliance_data(self) -> None: ...
    async def get_options_definitions(self, program_key: ProgramKey) -> dict[OptionKey, ProgramDefinitionOption]: ...
    async def update_options(self, event_key: EventKey, program_key: ProgramKey) -> None: ...
    def refreshed_too_often_recently(self) -> bool: ...
