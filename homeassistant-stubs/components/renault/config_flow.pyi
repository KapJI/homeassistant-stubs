from .const import CONF_KAMEREON_ACCOUNT_ID as CONF_KAMEREON_ACCOUNT_ID, CONF_LOCALE as CONF_LOCALE, DOMAIN as DOMAIN
from .renault_hub import RenaultHub as RenaultHub
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class RenaultFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    renault_config: Any
    renault_hub: Any
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    def _show_user_form(self, errors: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_kamereon(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
