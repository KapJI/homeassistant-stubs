from . import PchkConnectionManager as PchkConnectionManager
from .const import CONF_ACKNOWLEDGE as CONF_ACKNOWLEDGE, CONF_DIM_MODE as CONF_DIM_MODE, CONF_SK_NUM_TRIES as CONF_SK_NUM_TRIES, DIM_MODES as DIM_MODES, DOMAIN as DOMAIN
from .helpers import purge_device_registry as purge_device_registry, purge_entity_registry as purge_entity_registry
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_BASE as CONF_BASE, CONF_DEVICES as CONF_DEVICES, CONF_ENTITIES as CONF_ENTITIES, CONF_HOST as CONF_HOST, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
CONFIG_DATA: Incomplete
USER_DATA: Incomplete
CONFIG_SCHEMA: Incomplete
USER_SCHEMA: Incomplete

def get_config_entry(hass: HomeAssistant, data: ConfigType) -> config_entries.ConfigEntry | None: ...
async def validate_connection(data: ConfigType) -> str | None: ...

class LcnFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    _context_entry: ConfigEntry
    async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> config_entries.ConfigFlowResult: ...
    async def async_step_reconfigure(self, entry_data: Mapping[str, Any]) -> config_entries.ConfigFlowResult: ...
    async def async_step_reconfigure_confirm(self, user_input: dict[str, Any] | None = None) -> config_entries.ConfigFlowResult: ...
