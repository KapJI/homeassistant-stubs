import abc
import asyncio
from . import silabs_multiprotocol_addon as silabs_multiprotocol_addon
from .const import ZHA_DOMAIN as ZHA_DOMAIN
from .util import get_otbr_addon_manager as get_otbr_addon_manager, get_zha_device_path as get_zha_device_path, get_zigbee_flasher_addon_manager as get_zigbee_flasher_addon_manager
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.components.hassio import AddonError as AddonError, AddonInfo as AddonInfo, AddonManager as AddonManager, AddonState as AddonState
from homeassistant.components.zha.repairs.wrong_silabs_firmware import probe_silabs_firmware_type as probe_silabs_firmware_type
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryBaseFlow as ConfigEntryBaseFlow, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers.hassio import is_hassio as is_hassio
from typing import Any
from universal_silabs_flasher.const import ApplicationType

_LOGGER: Incomplete
STEP_PICK_FIRMWARE_THREAD: str
STEP_PICK_FIRMWARE_ZIGBEE: str

class BaseFirmwareInstallFlow(ConfigEntryBaseFlow, ABC, metaclass=abc.ABCMeta):
    _failed_addon_name: str
    _failed_addon_reason: str
    _probed_firmware_type: ApplicationType | None
    _device: str | None
    _hardware_name: str
    addon_install_task: asyncio.Task | None
    addon_start_task: asyncio.Task | None
    addon_uninstall_task: asyncio.Task | None
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def _get_translation_placeholders(self) -> dict[str, str]: ...
    async def _async_set_addon_config(self, config: dict, addon_manager: AddonManager) -> None: ...
    async def _async_get_addon_info(self, addon_manager: AddonManager) -> AddonInfo: ...
    async def async_step_pick_firmware(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _probe_firmware_type(self) -> bool: ...
    async def async_step_pick_firmware_zigbee(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_install_zigbee_flasher_addon(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _install_addon(self, addon_manager: silabs_multiprotocol_addon.WaitingAddonManager, step_id: str, next_step_id: str) -> ConfigFlowResult: ...
    async def async_step_addon_operation_failed(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_run_zigbee_flasher_addon(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_uninstall_zigbee_flasher_addon(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_confirm_zigbee(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_pick_firmware_thread(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_install_otbr_addon(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_start_otbr_addon(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_confirm_otbr(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @abstractmethod
    def _async_flow_finished(self) -> ConfigFlowResult: ...

class BaseFirmwareConfigFlow(BaseFirmwareInstallFlow, ConfigFlow, metaclass=abc.ABCMeta):
    @staticmethod
    @callback
    @abstractmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...
    async def async_step_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class BaseFirmwareOptionsFlow(BaseFirmwareInstallFlow, OptionsFlow, metaclass=abc.ABCMeta):
    _config_entry: Incomplete
    _probed_firmware_type: Incomplete
    context: Incomplete
    def __init__(self, config_entry: ConfigEntry, *args: Any, **kwargs: Any) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_pick_firmware_zigbee(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_pick_firmware_thread(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
