from .assist_pipeline import async_migrate_cloud_pipeline_engine as async_migrate_cloud_pipeline_engine
from .client import CloudClient as CloudClient
from .const import DATA_CLOUD as DATA_CLOUD, DATA_PLATFORMS_SETUP as DATA_PLATFORMS_SETUP, DOMAIN as DOMAIN, PREVIEW_FEATURE_STT_V2 as PREVIEW_FEATURE_STT_V2, STT_ENTITY_UNIQUE_ID as STT_ENTITY_UNIQUE_ID
from _typeshed import Incomplete
from collections.abc import AsyncIterable
from hass_nabucasa import Cloud as Cloud
from hass_nabucasa.voice import STTResponse as STTResponse
from homeassistant.components import labs as labs
from homeassistant.components.stt import AudioBitRates as AudioBitRates, AudioChannels as AudioChannels, AudioCodecs as AudioCodecs, AudioFormats as AudioFormats, AudioSampleRates as AudioSampleRates, DEFAULT_AUDIO_PROCESSING as DEFAULT_AUDIO_PROCESSING, SpeechAudioProcessing as SpeechAudioProcessing, SpeechMetadata as SpeechMetadata, SpeechResult as SpeechResult, SpeechResultState as SpeechResultState, SpeechToTextEntity as SpeechToTextEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.setup import async_when_setup as async_when_setup
from typing import override

_LOGGER: Incomplete
STT_V2_AUDIO_PROCESSING: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CloudProviderEntity(SpeechToTextEntity):
    _attr_name: str
    _attr_unique_id = STT_ENTITY_UNIQUE_ID
    cloud: Incomplete
    def __init__(self, cloud: Cloud[CloudClient]) -> None: ...
    @property
    def _stt_v2_enabled(self) -> bool: ...
    @property
    @override
    def supported_languages(self) -> list[str]: ...
    @property
    @override
    def supported_formats(self) -> list[AudioFormats]: ...
    @property
    @override
    def supported_codecs(self) -> list[AudioCodecs]: ...
    @property
    @override
    def supported_bit_rates(self) -> list[AudioBitRates]: ...
    @property
    @override
    def supported_sample_rates(self) -> list[AudioSampleRates]: ...
    @property
    @override
    def supported_channels(self) -> list[AudioChannels]: ...
    @property
    @override
    def audio_processing(self) -> SpeechAudioProcessing: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_will_remove_from_hass(self) -> None: ...
    async def _async_handle_labs_update(self, event_data: labs.EventLabsUpdatedData) -> None: ...
    @override
    async def async_process_audio_stream(self, metadata: SpeechMetadata, stream: AsyncIterable[bytes]) -> SpeechResult: ...
    async def _async_process_stt_v2(self, metadata: SpeechMetadata, stream: AsyncIterable[bytes]) -> STTResponse: ...
    async def _async_process_azure_stt(self, metadata: SpeechMetadata, stream: AsyncIterable[bytes]) -> STTResponse: ...
