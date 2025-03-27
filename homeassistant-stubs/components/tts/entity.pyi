from .const import TtsAudioType as TtsAudioType
from .media_source import generate_media_source_id as generate_media_source_id
from .models import Voice as Voice
from _typeshed import Incomplete
from collections.abc import AsyncGenerator, Mapping
from dataclasses import dataclass
from homeassistant.components.media_player import ATTR_MEDIA_ANNOUNCE as ATTR_MEDIA_ANNOUNCE, ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, ATTR_MEDIA_CONTENT_TYPE as ATTR_MEDIA_CONTENT_TYPE, MediaType as MediaType, SERVICE_PLAY_MEDIA as SERVICE_PLAY_MEDIA
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from propcache.api import cached_property
from typing import Any, final

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

@dataclass
class TTSAudioRequest:
    language: str
    options: dict[str, Any]
    message_gen: AsyncGenerator[str]

@dataclass
class TTSAudioResponse:
    extension: str
    data_gen: AsyncGenerator[bytes]

class TextToSpeechEntity(RestoreEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _attr_should_poll: bool
    __last_tts_loaded: str | None
    _attr_default_language: str
    _attr_default_options: Mapping[str, Any] | None
    _attr_supported_languages: list[str]
    _attr_supported_options: list[str] | None
    @property
    @final
    def state(self) -> str | None: ...
    @cached_property
    def supported_languages(self) -> list[str]: ...
    @cached_property
    def default_language(self) -> str: ...
    @cached_property
    def supported_options(self) -> list[str] | None: ...
    @cached_property
    def default_options(self) -> Mapping[str, Any] | None: ...
    @callback
    def async_get_supported_voices(self, language: str) -> list[Voice] | None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    async def async_speak(self, media_player_entity_id: list[str], message: str, cache: bool, language: str | None = None, options: dict | None = None) -> None: ...
    @final
    async def internal_async_stream_tts_audio(self, request: TTSAudioRequest) -> TTSAudioResponse: ...
    async def async_stream_tts_audio(self, request: TTSAudioRequest) -> TTSAudioResponse: ...
    def get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...
    async def async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...
