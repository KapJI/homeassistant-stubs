from . import EleventLabsConfigEntry as EleventLabsConfigEntry
from .const import CONF_VOICE as CONF_VOICE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from elevenlabs.client import AsyncElevenLabs as AsyncElevenLabs
from elevenlabs.types import Model as Model, Voice as ElevenLabsVoice
from homeassistant.components.tts import ATTR_VOICE as ATTR_VOICE, TextToSpeechEntity as TextToSpeechEntity, TtsAudioType as TtsAudioType, Voice as Voice
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: EleventLabsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElevenLabsTTSEntity(TextToSpeechEntity):
    _attr_supported_options: Incomplete
    _client: Incomplete
    _model: Incomplete
    _default_voice_id: Incomplete
    _voices: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    _attr_supported_languages: Incomplete
    _attr_default_language: Incomplete
    def __init__(self, client: AsyncElevenLabs, model: Model, voices: list[ElevenLabsVoice], default_voice_id: str, entry_id: str, title: str) -> None: ...
    def async_get_supported_voices(self, language: str) -> list[Voice]: ...
    async def async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...
