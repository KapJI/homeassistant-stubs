from . import OpenAIConfigEntry as OpenAIConfigEntry
from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_PROMPT as CONF_PROMPT, CONF_TTS_SPEED as CONF_TTS_SPEED, RECOMMENDED_TTS_SPEED as RECOMMENDED_TTS_SPEED
from .entity import OpenAIBaseLLMEntity as OpenAIBaseLLMEntity
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.tts import ATTR_PREFERRED_FORMAT as ATTR_PREFERRED_FORMAT, ATTR_VOICE as ATTR_VOICE, TextToSpeechEntity as TextToSpeechEntity, TtsAudioType as TtsAudioType, Voice as Voice
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from propcache.api import cached_property
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: OpenAIConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenAITTSEntity(TextToSpeechEntity, OpenAIBaseLLMEntity):
    _attr_supported_options: Incomplete
    _attr_supported_languages: Incomplete
    _attr_default_language: str
    _supported_voices: Incomplete
    _supported_formats: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    def __init__(self, entry: OpenAIConfigEntry, subentry: ConfigSubentry) -> None: ...
    @callback
    def async_get_supported_voices(self, language: str) -> list[Voice]: ...
    @cached_property
    def default_options(self) -> Mapping[str, Any]: ...
    async def async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...
