from . import OpenAIConfigEntry as OpenAIConfigEntry
from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, DEFAULT_STT_PROMPT as DEFAULT_STT_PROMPT, RECOMMENDED_STT_MODEL as RECOMMENDED_STT_MODEL
from .entity import OpenAIBaseLLMEntity as OpenAIBaseLLMEntity
from _typeshed import Incomplete
from collections.abc import AsyncIterable
from homeassistant.components import stt as stt
from homeassistant.const import CONF_PROMPT as CONF_PROMPT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: OpenAIConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenAISTTEntity(stt.SpeechToTextEntity, OpenAIBaseLLMEntity):
    @property
    @override
    def supported_languages(self) -> list[str]: ...
    @property
    @override
    def supported_formats(self) -> list[stt.AudioFormats]: ...
    @property
    @override
    def supported_codecs(self) -> list[stt.AudioCodecs]: ...
    @property
    @override
    def supported_bit_rates(self) -> list[stt.AudioBitRates]: ...
    @property
    @override
    def supported_sample_rates(self) -> list[stt.AudioSampleRates]: ...
    @property
    @override
    def supported_channels(self) -> list[stt.AudioChannels]: ...
    @override
    async def async_process_audio_stream(self, metadata: stt.SpeechMetadata, stream: AsyncIterable[bytes]) -> stt.SpeechResult: ...
