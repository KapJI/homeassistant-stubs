from .const import API_DEFAULT_RETRY_AFTER as API_DEFAULT_RETRY_AFTER, APPLIANCES_WITH_PROGRAMS as APPLIANCES_WITH_PROGRAMS, DOMAIN as DOMAIN
from .utils import get_dict_from_home_connect_error as get_dict_from_home_connect_error
from _typeshed import Incomplete
from aiohomeconnect.client import Client as HomeConnectClient
from aiohomeconnect.model import CommandKey as CommandKey, Event, EventKey, EventMessage as EventMessage, GetSetting, HomeAppliance as HomeAppliance, OptionKey as OptionKey, ProgramKey, SettingKey, Status, StatusKey
from aiohomeconnect.model.program import EnumerateProgram as EnumerateProgram, ProgramDefinitionOption as ProgramDefinitionOption
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from propcache.api import cached_property
from typing import Any

_LOGGER: Incomplete
MAX_EXECUTIONS_TIME_WINDOW: Incomplete
MAX_EXECUTIONS: int
type HomeConnectConfigEntry = ConfigEntry[HomeConnectCoordinator]

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

class HomeConnectCoordinator(DataUpdateCoordinator[dict[str, HomeConnectApplianceData]]):
    config_entry: HomeConnectConfigEntry
    client: Incomplete
    _special_listeners: dict[CALLBACK_TYPE, tuple[CALLBACK_TYPE, tuple[EventKey, ...]]]
    device_registry: Incomplete
    data: Incomplete
    _execution_tracker: dict[str, list[float]]
    def __init__(self, hass: HomeAssistant, config_entry: HomeConnectConfigEntry, client: HomeConnectClient) -> None: ...
    @cached_property
    def context_listeners(self) -> dict[tuple[str, EventKey], list[CALLBACK_TYPE]]: ...
    @callback
    def async_add_listener(self, update_callback: CALLBACK_TYPE, context: Any = None) -> Callable[[], None]: ...
    @callback
    def async_add_special_listener(self, update_callback: CALLBACK_TYPE, context: tuple[EventKey, ...]) -> Callable[[], None]: ...
    @callback
    def start_event_listener(self) -> None: ...
    async def _event_listener(self) -> None: ...
    @callback
    def _call_event_listener(self, event_message: EventMessage) -> None: ...
    @callback
    def _call_all_event_listeners_for_appliance(self, ha_id: str) -> None: ...
    async def _async_update_data(self) -> dict[str, HomeConnectApplianceData]: ...
    async def async_setup(self) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _get_appliance_data(self, appliance: HomeAppliance, appliance_data_to_update: HomeConnectApplianceData | None = None) -> HomeConnectApplianceData: ...
    async def get_options_definitions(self, ha_id: str, program_key: ProgramKey) -> dict[OptionKey, ProgramDefinitionOption]: ...
    async def update_options(self, ha_id: str, event_key: EventKey, program_key: ProgramKey) -> None: ...
    def refreshed_too_often_recently(self, appliance_ha_id: str) -> bool: ...
    async def reset_execution_tracker(self, appliance_ha_id: str) -> None: ...
