from . import SpeechManager as SpeechManager, TextToSpeechEntity as TextToSpeechEntity
from .const import DATA_TTS_MANAGER as DATA_TTS_MANAGER, DOMAIN as DOMAIN
from .legacy import Provider as Provider
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent

def get_engine_instance(hass: HomeAssistant, engine: str) -> TextToSpeechEntity | Provider | None: ...
