from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

CONFIG_SCHEMA: Incomplete

class StarlinkConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def get_device_id(self, url: str) -> str | None: ...
