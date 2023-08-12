import abc
import asyncio
from .const import LOGGER as LOGGER, SILABS_MULTIPROTOCOL_ADDON_SLUG as SILABS_MULTIPROTOCOL_ADDON_SLUG
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant import config_entries as config_entries
from homeassistant.components.hassio import AddonError as AddonError, AddonInfo as AddonInfo, AddonManager as AddonManager, AddonState as AddonState, hostname_from_addon_slug as hostname_from_addon_slug, is_hassio as is_hassio
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import AbortFlow as AbortFlow, FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.integration_platform import async_process_integration_platforms as async_process_integration_platforms
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from homeassistant.helpers.singleton import singleton as singleton
from homeassistant.helpers.storage import Store as Store
from typing import Any, Protocol

_LOGGER: Incomplete
DATA_ADDON_MANAGER: str
ADDON_SETUP_TIMEOUT: int
ADDON_SETUP_TIMEOUT_ROUNDS: int
CONF_ADDON_AUTOFLASH_FW: str
CONF_ADDON_DEVICE: str
CONF_ENABLE_MULTI_PAN: str
DEFAULT_CHANNEL: int
DEFAULT_CHANNEL_CHANGE_DELAY: Incomplete
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int
STORAGE_VERSION_MINOR: int
SAVE_DELAY: int

async def get_addon_manager(hass: HomeAssistant) -> MultiprotocolAddonManager: ...

class MultiprotocolAddonManager(AddonManager):
    _channel: Incomplete
    _platforms: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_setup(self) -> None: ...
    async def _register_multipan_platform(self, hass: HomeAssistant, integration_domain: str, platform: MultipanProtocol) -> None: ...
    async def async_change_channel(self, channel: int, delay: float) -> list[asyncio.Task]: ...
    async def async_active_platforms(self) -> list[str]: ...
    def async_get_channel(self) -> int | None: ...
    def async_set_channel(self, channel: int) -> None: ...
    async def async_load(self) -> None: ...
    def async_schedule_save(self) -> None: ...
    def _data_to_save(self) -> dict[str, list[dict[str, str | None]]]: ...

class MultipanProtocol(Protocol):
    async def async_change_channel(self, hass: HomeAssistant, channel: int, delay: float) -> asyncio.Task | None: ...
    async def async_get_channel(self, hass: HomeAssistant) -> int | None: ...
    async def async_using_multipan(self, hass: HomeAssistant) -> bool: ...

class SerialPortSettings:
    device: str
    baudrate: str
    flow_control: bool
    def __init__(self, device, baudrate, flow_control) -> None: ...
    def __mypy-replace(*, device, baudrate, flow_control) -> None: ...

def get_zigbee_socket() -> str: ...
def is_multiprotocol_url(url: str) -> bool: ...

class OptionsFlowHandler(config_entries.OptionsFlow, ABC, metaclass=abc.ABCMeta):
    install_task: Incomplete
    start_task: Incomplete
    _zha_migration_mgr: Incomplete
    config_entry: Incomplete
    original_addon_config: Incomplete
    revert_reason: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    @abstractmethod
    async def _async_serial_port_settings(self) -> SerialPortSettings: ...
    @abstractmethod
    async def _async_zha_physical_discovery(self) -> dict[str, Any]: ...
    @abstractmethod
    def _hardware_name(self) -> str: ...
    @abstractmethod
    def _zha_name(self) -> str: ...
    @property
    def flow_manager(self) -> config_entries.OptionsFlowManager: ...
    async def _async_get_addon_info(self) -> AddonInfo: ...
    async def _async_set_addon_config(self, config: dict) -> None: ...
    async def _async_install_addon(self) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_on_supervisor(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_addon_not_installed(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_install_addon(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_install_failed(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_configure_addon(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_start_addon(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_start_failed(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def _async_start_addon(self) -> None: ...
    async def async_step_finish_addon_setup(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_addon_installed(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_show_addon_menu(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reconfigure_addon(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_notify_unknown_multipan_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_change_channel(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_notify_channel_change(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_uninstall_addon(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_show_revert_guide(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_addon_installed_other_device(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

async def check_multi_pan_addon(hass: HomeAssistant) -> None: ...
async def multi_pan_addon_using_device(hass: HomeAssistant, device_path: str) -> bool: ...
