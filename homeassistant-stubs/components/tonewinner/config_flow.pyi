from .const import CONF_SERIAL_PORT as CONF_SERIAL_PORT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigEntryFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_MODEL as CONF_MODEL
from homeassistant.helpers.selector import SerialPortSelector as SerialPortSelector
from tonewinner_rs232 import ReceiverInfo as ReceiverInfo
from typing import Any, override

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

class TonewinnerConfigFlow(ConfigEntryFlow, domain=DOMAIN):
    async def _async_probe_receiver(self, port: str) -> str | None: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
