from .const import DOMAIN as DOMAIN
from .host import ReolinkHost as ReolinkHost
from collections.abc import Awaitable, Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant import config_entries as config_entries
from homeassistant.components.media_source import Unresolvable as Unresolvable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

type ReolinkConfigEntry = config_entries.ConfigEntry[ReolinkData]
@dataclass
class ReolinkData:
    host: ReolinkHost
    device_coordinator: DataUpdateCoordinator[None]
    firmware_coordinator: DataUpdateCoordinator[None]

def is_connected(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool: ...
def get_host(hass: HomeAssistant, config_entry_id: str) -> ReolinkHost: ...
def get_device_uid_and_ch(device: dr.DeviceEntry, host: ReolinkHost) -> tuple[list[str], int | None, bool]: ...
def raise_translated_error[**P, R](func: Callable[P, Awaitable[R]]) -> Callable[P, Coroutine[Any, Any, R]]: ...
