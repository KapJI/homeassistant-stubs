from .const import DOMAIN as DOMAIN, INTENT_MEDIA_NEXT as INTENT_MEDIA_NEXT, INTENT_MEDIA_PAUSE as INTENT_MEDIA_PAUSE, INTENT_MEDIA_PREVIOUS as INTENT_MEDIA_PREVIOUS, INTENT_MEDIA_SEARCH_AND_PLAY as INTENT_MEDIA_SEARCH_AND_PLAY, INTENT_MEDIA_UNPAUSE as INTENT_MEDIA_UNPAUSE, INTENT_PLAYER_MUTE as INTENT_PLAYER_MUTE, INTENT_PLAYER_UNMUTE as INTENT_PLAYER_UNMUTE, INTENT_SET_VOLUME as INTENT_SET_VOLUME, INTENT_SET_VOLUME_RELATIVE as INTENT_SET_VOLUME_RELATIVE
from _typeshed import Incomplete
from homeassistant.components.homeassistant import async_should_expose as async_should_expose
from homeassistant.components.llm import LLMTools as LLMTools
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import intent as intent
from homeassistant.helpers.llm import IntentTool as IntentTool, LLMContext as LLMContext, LLM_API_ASSIST as LLM_API_ASSIST, Tool as Tool

LLM_INTENTS: Incomplete

@callback
def async_get_tools(hass: HomeAssistant, llm_context: LLMContext, api_id: str) -> LLMTools | None: ...
