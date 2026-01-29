from . import LeilSaunaConfigEntry as LeilSaunaConfigEntry
from .const import DEFAULT_PRESET_NAME_TYPE_1 as DEFAULT_PRESET_NAME_TYPE_1, DEFAULT_PRESET_NAME_TYPE_2 as DEFAULT_PRESET_NAME_TYPE_2, DEFAULT_PRESET_NAME_TYPE_3 as DEFAULT_PRESET_NAME_TYPE_3, DOMAIN as DOMAIN, OPT_PRESET_NAME_TYPE_1 as OPT_PRESET_NAME_TYPE_1, OPT_PRESET_NAME_TYPE_2 as OPT_PRESET_NAME_TYPE_2, OPT_PRESET_NAME_TYPE_3 as OPT_PRESET_NAME_TYPE_3
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_USER as SOURCE_USER
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import callback as callback
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

async def validate_input(data: dict[str, Any]) -> None: ...

class LeilSaunaConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: LeilSaunaConfigEntry) -> LeilSaunaOptionsFlow: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class LeilSaunaOptionsFlow(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
