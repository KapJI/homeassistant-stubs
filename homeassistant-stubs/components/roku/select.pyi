from . import roku_exception_handler as roku_exception_handler
from .const import DOMAIN as DOMAIN
from .coordinator import RokuDataUpdateCoordinator as RokuDataUpdateCoordinator
from .entity import RokuEntity as RokuEntity
from .helpers import format_channel_name as format_channel_name
from collections.abc import Awaitable, Callable as Callable
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from rokuecp import Roku as Roku
from rokuecp.models import Device as RokuDevice
from typing import Any

class RokuSelectEntityDescriptionMixin:
    options_fn: Callable[[RokuDevice], list[str]]
    value_fn: Callable[[RokuDevice], Union[str, None]]
    set_fn: Callable[[RokuDevice, Roku, str], Awaitable[None]]
    def __init__(self, options_fn, value_fn, set_fn) -> None: ...

def _get_application_name(device: RokuDevice) -> Union[str, None]: ...
def _get_applications(device: RokuDevice) -> list[str]: ...
def _get_channel_name(device: RokuDevice) -> Union[str, None]: ...
def _get_channels(device: RokuDevice) -> list[str]: ...
async def _launch_application(device: RokuDevice, roku: Roku, value: str) -> None: ...
async def _tune_channel(device: RokuDevice, roku: Roku, value: str) -> None: ...

class RokuSelectEntityDescription(SelectEntityDescription, RokuSelectEntityDescriptionMixin):
    def __init__(self, options_fn, value_fn, set_fn, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

ENTITIES: tuple[RokuSelectEntityDescription, ...]
CHANNEL_ENTITY: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RokuSelectEntity(RokuEntity, SelectEntity):
    entity_description: RokuSelectEntityDescription
    @property
    def current_option(self) -> Union[str, None]: ...
    @property
    def options(self) -> list[str]: ...
    async def async_select_option(self, option: str) -> None: ...
