from .const import CONF_HOSTNAME as CONF_HOSTNAME, CONF_IPV4 as CONF_IPV4, CONF_IPV6 as CONF_IPV6, CONF_IPV6_V4 as CONF_IPV6_V4, CONF_RESOLVER as CONF_RESOLVER, CONF_RESOLVER_IPV6 as CONF_RESOLVER_IPV6, DEFAULT_HOSTNAME as DEFAULT_HOSTNAME, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_RESOLVER as DEFAULT_RESOLVER, DEFAULT_RESOLVER_IPV6 as DEFAULT_RESOLVER_IPV6, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

DATA_SCHEMA: Incomplete
DATA_SCHEMA_ADV: Incomplete

async def async_validate_hostname(hostname: str, resolver_ipv4: str, resolver_ipv6: str) -> dict[str, bool]: ...

class DnsIPConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> DnsIPOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class DnsIPOptionsFlowHandler(config_entries.OptionsFlow):
    entry: Incomplete
    def __init__(self, entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
