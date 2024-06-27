from .const import CONF_ALLOW_NAMELESS_UUIDS as CONF_ALLOW_NAMELESS_UUIDS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import bluetooth as bluetooth
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.core import callback as callback
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any

class IBeaconConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...

class IBeaconOptionsFlow(OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict | None = None) -> ConfigFlowResult: ...
