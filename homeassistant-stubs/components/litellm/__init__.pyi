from .coordinator import LiteLLMConfigEntry as LiteLLMConfigEntry, LiteLLMDataUpdateCoordinator as LiteLLMDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LiteLLMConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: LiteLLMConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: LiteLLMConfigEntry) -> bool: ...
