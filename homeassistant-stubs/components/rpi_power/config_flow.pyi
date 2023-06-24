from .const import DOMAIN as DOMAIN
from collections.abc import Awaitable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.config_entry_flow import DiscoveryFlowHandler as DiscoveryFlowHandler
from typing import Any

async def _async_supported(hass: HomeAssistant) -> bool: ...

class RPiPowerFlow(DiscoveryFlowHandler[Awaitable[bool]], domain=DOMAIN):
    VERSION: int
    def __init__(self) -> None: ...
    async def async_step_onboarding(self, data: dict[str, Any] | None = ...) -> FlowResult: ...
