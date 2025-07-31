from . import OnkyoConfigEntry as OnkyoConfigEntry
from .const import DOMAIN as DOMAIN, InputSource as InputSource, ListeningMode as ListeningMode, OPTION_INPUT_SOURCES as OPTION_INPUT_SOURCES, OPTION_LISTENING_MODES as OPTION_LISTENING_MODES, OPTION_MAX_VOLUME as OPTION_MAX_VOLUME, OPTION_MAX_VOLUME_DEFAULT as OPTION_MAX_VOLUME_DEFAULT, OPTION_VOLUME_RESOLUTION as OPTION_VOLUME_RESOLUTION, OPTION_VOLUME_RESOLUTION_DEFAULT as OPTION_VOLUME_RESOLUTION_DEFAULT, VOLUME_RESOLUTION_ALLOWED as VOLUME_RESOLUTION_ALLOWED
from .receiver import async_discover as async_discover, async_interview as async_interview
from .util import get_meaning as get_meaning
from _typeshed import Incomplete
from aioonkyo import ReceiverInfo as ReceiverInfo
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlowWithReload as OptionsFlowWithReload, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import section as section
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, Selector as Selector, TextSelector as TextSelector
from homeassistant.helpers.service_info.ssdp import SsdpServiceInfo as SsdpServiceInfo
from typing import Any

_LOGGER: Incomplete
CONF_DEVICE: str
INPUT_SOURCES_DEFAULT: list[InputSource]
LISTENING_MODES_DEFAULT: list[ListeningMode]
INPUT_SOURCES_ALL_MEANINGS: Incomplete
LISTENING_MODES_ALL_MEANINGS: Incomplete
STEP_MANUAL_SCHEMA: Incomplete
STEP_RECONFIGURE_SCHEMA: Incomplete
STEP_CONFIGURE_SCHEMA: Incomplete

class OnkyoConfigFlow(ConfigFlow, domain=DOMAIN):
    _receiver_info: ReceiverInfo
    _discovered_infos: dict[str, ReceiverInfo]
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_manual(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_eiscp_discovery(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_configure_receiver(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: OnkyoConfigEntry) -> OptionsFlowWithReload: ...

OPTIONS_STEP_INIT_SCHEMA: Incomplete

class OnkyoOptionsFlowHandler(OptionsFlowWithReload):
    _data: dict[str, Any]
    _input_sources: dict[InputSource, str]
    _listening_modes: dict[ListeningMode, str]
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_names(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
