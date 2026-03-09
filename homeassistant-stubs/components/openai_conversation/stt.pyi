from . import OpenAIConfigEntry as OpenAIConfigEntry
from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_PROMPT as CONF_PROMPT, DEFAULT_STT_PROMPT as DEFAULT_STT_PROMPT, RECOMMENDED_STT_MODEL as RECOMMENDED_STT_MODEL
from .entity import OpenAIBaseLLMEntity as OpenAIBaseLLMEntity
from _typeshed import Incomplete
from collections.abc import AsyncIterable
from homeassistant.components import stt as stt
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: OpenAIConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenAISTTEntity(stt.SpeechToTextEntity, OpenAIBaseLLMEntity):
    @property
    def supported_languages(self) -> list[str]: ...
    @property
    def supported_formats(self) -> list[stt.AudioFormats]: ...
    @property
    def supported_codecs(self) -> list[stt.AudioCodecs]: ...
    @property
    def supported_bit_rates(self) -> list[stt.AudioBitRates]: ...
    @property
    def supported_sample_rates(self) -> list[stt.AudioSampleRates]: ...
    @property
    def supported_channels(self) -> list[stt.AudioChannels]: ...
    async def async_process_audio_stream(self, metadata: stt.SpeechMetadata, stream: AsyncIterable[bytes]) -> stt.SpeechResult: ...
