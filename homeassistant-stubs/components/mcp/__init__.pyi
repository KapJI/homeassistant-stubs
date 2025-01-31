from .const import DOMAIN as DOMAIN
from .coordinator import ModelContextProtocolCoordinator
from .types import ModelContextProtocolConfigEntry
from dataclasses import dataclass
from homeassistant.core import HomeAssistant
from homeassistant.helpers import llm

__all__ = ['DOMAIN', 'async_setup_entry', 'async_unload_entry']

async def async_setup_entry(hass: HomeAssistant, entry: ModelContextProtocolConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ModelContextProtocolConfigEntry) -> bool: ...

@dataclass(kw_only=True)
class ModelContextProtocolAPI(llm.API):
    coordinator: ModelContextProtocolCoordinator
    async def async_get_api_instance(self, llm_context: llm.LLMContext) -> llm.APIInstance: ...
