import asyncio
from .const import ADDON_SLUG as ADDON_SLUG, CONF_ADDON_DEVICE as CONF_ADDON_DEVICE, CONF_ADDON_S0_LEGACY_KEY as CONF_ADDON_S0_LEGACY_KEY, CONF_ADDON_S2_ACCESS_CONTROL_KEY as CONF_ADDON_S2_ACCESS_CONTROL_KEY, CONF_ADDON_S2_AUTHENTICATED_KEY as CONF_ADDON_S2_AUTHENTICATED_KEY, CONF_ADDON_S2_UNAUTHENTICATED_KEY as CONF_ADDON_S2_UNAUTHENTICATED_KEY, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from enum import Enum
from homeassistant.components.hassio import async_create_backup as async_create_backup, async_get_addon_discovery_info as async_get_addon_discovery_info, async_get_addon_info as async_get_addon_info, async_get_addon_store_info as async_get_addon_store_info, async_install_addon as async_install_addon, async_restart_addon as async_restart_addon, async_set_addon_options as async_set_addon_options, async_start_addon as async_start_addon, async_stop_addon as async_stop_addon, async_uninstall_addon as async_uninstall_addon, async_update_addon as async_update_addon
from homeassistant.components.hassio.handler import HassioAPIError as HassioAPIError
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.singleton import singleton as singleton
from typing import Any, TypeVar

_R = TypeVar('_R')
_P: Incomplete
DATA_ADDON_MANAGER: Incomplete

def get_addon_manager(hass: HomeAssistant) -> AddonManager: ...
def api_error(error_message: str) -> Callable[[Callable[_P, Awaitable[_R]]], Callable[_P, Coroutine[Any, Any, _R]]]: ...

class AddonInfo:
    options: dict[str, Any]
    state: AddonState
    update_available: bool
    version: Union[str, None]
    def __init__(self, options, state, update_available, version) -> None: ...

class AddonState(Enum):
    NOT_INSTALLED: str
    INSTALLING: str
    UPDATING: str
    NOT_RUNNING: str
    RUNNING: str

class AddonManager:
    _hass: Incomplete
    _install_task: Incomplete
    _restart_task: Incomplete
    _start_task: Incomplete
    _update_task: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def task_in_progress(self) -> bool: ...
    async def async_get_addon_discovery_info(self) -> dict: ...
    async def async_get_addon_info(self) -> AddonInfo: ...
    def async_get_addon_state(self, addon_info: dict[str, Any]) -> AddonState: ...
    async def async_set_addon_options(self, config: dict) -> None: ...
    async def async_install_addon(self) -> None: ...
    def async_schedule_install_addon(self, catch_error: bool = ...) -> asyncio.Task: ...
    def async_schedule_install_setup_addon(self, usb_path: str, s0_legacy_key: str, s2_access_control_key: str, s2_authenticated_key: str, s2_unauthenticated_key: str, catch_error: bool = ...) -> asyncio.Task: ...
    async def async_uninstall_addon(self) -> None: ...
    async def async_update_addon(self) -> None: ...
    def async_schedule_update_addon(self, catch_error: bool = ...) -> asyncio.Task: ...
    async def async_start_addon(self) -> None: ...
    async def async_restart_addon(self) -> None: ...
    def async_schedule_start_addon(self, catch_error: bool = ...) -> asyncio.Task: ...
    def async_schedule_restart_addon(self, catch_error: bool = ...) -> asyncio.Task: ...
    async def async_stop_addon(self) -> None: ...
    async def async_configure_addon(self, usb_path: str, s0_legacy_key: str, s2_access_control_key: str, s2_authenticated_key: str, s2_unauthenticated_key: str) -> None: ...
    def async_schedule_setup_addon(self, usb_path: str, s0_legacy_key: str, s2_access_control_key: str, s2_authenticated_key: str, s2_unauthenticated_key: str, catch_error: bool = ...) -> asyncio.Task: ...
    async def async_create_backup(self) -> None: ...
    def _async_schedule_addon_operation(self, *funcs: Callable, catch_error: bool = ...) -> asyncio.Task: ...

class AddonError(HomeAssistantError): ...
