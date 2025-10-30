from .const import DOMAIN as DOMAIN
from .coordinator import ModelContextProtocolCoordinator
from dataclasses import dataclass
from homeassistant.helpers import llm

__all__ = ['DOMAIN']

@dataclass(kw_only=True)
class ModelContextProtocolAPI(llm.API):
    coordinator: ModelContextProtocolCoordinator
    async def async_get_api_instance(self, llm_context: llm.LLMContext) -> llm.APIInstance: ...
