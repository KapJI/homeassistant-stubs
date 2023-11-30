from .const import CONF_COUNTY as CONF_COUNTY, CONF_PHONE_NUMBER as CONF_PHONE_NUMBER, COUNTY_LIST as COUNTY_LIST, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

STEP_USER_DATA_SCHEMA: Incomplete
_LOGGER: Incomplete

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    meter_verification: bool
    meter_data: dict[str, str]
    meter_error: dict[str, str]
    async def _verify_meter(self, phone_number: str) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_finish_smart_meter(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
