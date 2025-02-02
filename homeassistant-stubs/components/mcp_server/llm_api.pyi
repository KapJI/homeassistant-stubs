from .const import LLM_API as LLM_API, LLM_API_NAME as LLM_API_NAME
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import llm as llm

EXPOSED_ENTITY_FIELDS: Incomplete

def async_register_api(hass: HomeAssistant) -> None: ...

class StatelessAssistAPI(llm.AssistAPI):
    id: Incomplete
    name: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @callback
    def _async_get_exposed_entities_prompt(self, llm_context: llm.LLMContext, exposed_entities: dict | None) -> list[str]: ...
