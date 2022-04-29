from .const import CONF_TRACKED_ASSET_PAIRS as CONF_TRACKED_ASSET_PAIRS, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from .utils import get_tradable_asset_pairs as get_tradable_asset_pairs
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class KrakenConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> KrakenOptionsFlowHandler: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class KrakenOptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
