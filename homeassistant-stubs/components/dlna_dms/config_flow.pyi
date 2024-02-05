from .const import CONFIG_VERSION as CONFIG_VERSION, CONF_SOURCE_ID as CONF_SOURCE_ID, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .util import generate_source_id as generate_source_id
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components import ssdp as ssdp
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_HOST as CONF_HOST, CONF_URL as CONF_URL
from homeassistant.data_entry_flow import AbortFlow as AbortFlow, FlowResult as FlowResult
from typing import Any

LOGGER: Incomplete

class DlnaDmsFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = CONFIG_VERSION
    _discoveries: Incomplete
    _location: Incomplete
    _usn: Incomplete
    _name: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    def _create_entry(self) -> FlowResult: ...
    async def _async_parse_discovery(self, discovery_info: ssdp.SsdpServiceInfo, raise_on_progress: bool = True) -> None: ...
    async def _async_get_discoveries(self) -> list[ssdp.SsdpServiceInfo]: ...
