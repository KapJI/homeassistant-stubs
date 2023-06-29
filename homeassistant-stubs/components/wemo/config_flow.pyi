import voluptuous as vol
from .const import DOMAIN as DOMAIN
from .wemo_device import Options as Options, OptionsValidationError as OptionsValidationError
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, OptionsFlow as OptionsFlow
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.config_entry_flow import DiscoveryFlowHandler as DiscoveryFlowHandler
from typing import Any

async def _async_has_devices(hass: HomeAssistant) -> bool: ...

class WemoFlow(DiscoveryFlowHandler, domain=DOMAIN):
    def __init__(self) -> None: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...

class WemoOptionsFlow(OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

def _schema_for_options(options: Options) -> vol.Schema: ...
