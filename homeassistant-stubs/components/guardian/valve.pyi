from . import GuardianData as GuardianData, ValveControllerEntity as ValveControllerEntity, ValveControllerEntityDescription as ValveControllerEntityDescription
from .const import API_VALVE_STATUS as API_VALVE_STATUS, DOMAIN as DOMAIN
from .util import convert_exceptions_to_homeassistant_error as convert_exceptions_to_homeassistant_error
from _typeshed import Incomplete
from aioguardian import Client as Client
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.valve import ValveDeviceClass as ValveDeviceClass, ValveEntity as ValveEntity, ValveEntityDescription as ValveEntityDescription, ValveEntityFeature as ValveEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

VALVE_KIND_VALVE: str

class GuardianValveState(StrEnum):
    CLOSED: str
    CLOSING: str
    FINISH_CLOSING: str
    FINISH_OPENING: str
    OPEN: str
    OPENING: str
    START_CLOSING: str
    START_OPENING: str

@dataclass(frozen=True, kw_only=True)
class ValveControllerValveDescription(ValveEntityDescription, ValveControllerEntityDescription):
    is_closed_fn: Callable[[dict[str, Any]], bool]
    is_closing_fn: Callable[[dict[str, Any]], bool]
    is_opening_fn: Callable[[dict[str, Any]], bool]
    close_coro_fn: Callable[[Client], Coroutine[Any, Any, None]]
    halt_coro_fn: Callable[[Client], Coroutine[Any, Any, None]]
    open_coro_fn: Callable[[Client], Coroutine[Any, Any, None]]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, api_category, reports_position, is_closed_fn, is_closing_fn, is_opening_fn, close_coro_fn, halt_coro_fn, open_coro_fn) -> None: ...

async def async_close_valve(client: Client) -> None: ...
async def async_halt_valve(client: Client) -> None: ...
async def async_open_valve(client: Client) -> None: ...
def is_closing(data: dict[str, Any]) -> bool: ...
def is_opening(data: dict[str, Any]) -> bool: ...

VALVE_CONTROLLER_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ValveControllerValve(ValveControllerEntity, ValveEntity):
    _attr_supported_features: Incomplete
    entity_description: ValveControllerValveDescription
    _client: Incomplete
    def __init__(self, entry: ConfigEntry, data: GuardianData, description: ValveControllerValveDescription) -> None: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def is_closed(self) -> bool: ...
    @property
    def is_opening(self) -> bool: ...
    async def async_close_valve(self) -> None: ...
    async def async_open_valve(self) -> None: ...
    async def async_stop_valve(self) -> None: ...
