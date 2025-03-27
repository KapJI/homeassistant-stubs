from .const import DOMAIN as DOMAIN
from .host import ReolinkHost as ReolinkHost
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant import config_entries as config_entries
from homeassistant.components.media_source import Unresolvable as Unresolvable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.translation import async_get_exception_message as async_get_exception_message
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from reolink_aio.exceptions import ReolinkError
from typing import Any

STORAGE_VERSION: int
type ReolinkConfigEntry = config_entries.ConfigEntry[ReolinkData]

@dataclass
class ReolinkData:
    host: ReolinkHost
    device_coordinator: DataUpdateCoordinator[None]
    firmware_coordinator: DataUpdateCoordinator[None]

def is_connected(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool: ...
def get_host(hass: HomeAssistant, config_entry_id: str) -> ReolinkHost: ...
def get_store(hass: HomeAssistant, config_entry_id: str) -> Store[str]: ...
def get_device_uid_and_ch(device: dr.DeviceEntry, host: ReolinkHost) -> tuple[list[str], int | None, bool]: ...
def check_translation_key(err: ReolinkError) -> str | None: ...

_EXCEPTION_TO_TRANSLATION_KEY: Incomplete

def raise_translated_error[**P, R](func: Callable[P, Awaitable[R]]) -> Callable[P, Coroutine[Any, Any, R]]: ...
