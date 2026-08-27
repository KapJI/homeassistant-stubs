from .coordinator import FlowItConfigEntry as FlowItConfigEntry, FlowItCoordinator as FlowItCoordinator, FlowItData as FlowItData
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.httpx_client import get_async_client as get_async_client

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: FlowItConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FlowItConfigEntry) -> bool: ...
