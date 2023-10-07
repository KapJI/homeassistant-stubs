from .const import CONF_DEBUG_RECORDING_DIR as CONF_DEBUG_RECORDING_DIR, DATA_CONFIG as DATA_CONFIG, DATA_LAST_WAKE_UP as DATA_LAST_WAKE_UP, DEFAULT_WAKE_WORD_COOLDOWN as DEFAULT_WAKE_WORD_COOLDOWN, DOMAIN as DOMAIN
from .error import IntentRecognitionError as IntentRecognitionError, PipelineError as PipelineError, PipelineNotFound as PipelineNotFound, SpeechToTextError as SpeechToTextError, TextToSpeechError as TextToSpeechError, WakeWordDetectionAborted as WakeWordDetectionAborted, WakeWordDetectionError as WakeWordDetectionError, WakeWordTimeoutError as WakeWordTimeoutError
from .vad import AudioBuffer as AudioBuffer, VoiceActivityTimeout as VoiceActivityTimeout, VoiceCommandSegmenter as VoiceCommandSegmenter, chunk_samples as chunk_samples
from _typeshed import Incomplete
from collections import deque
from collections.abc import AsyncGenerator, AsyncIterable, Callable, Iterable
from enum import StrEnum
from homeassistant.components import conversation as conversation, media_source as media_source, stt as stt, tts as tts, wake_word as wake_word, websocket_api as websocket_api
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.collection import CHANGE_UPDATED as CHANGE_UPDATED, CollectionError as CollectionError, ItemNotFound as ItemNotFound, SerializedStorageCollection as SerializedStorageCollection, StorageCollection as StorageCollection, StorageCollectionWebsocket as StorageCollectionWebsocket
from homeassistant.helpers.singleton import singleton as singleton
from homeassistant.helpers.storage import Store as Store
from homeassistant.util.limited_size_dict import LimitedSizeDict as LimitedSizeDict
from pathlib import Path
from queue import Queue
from threading import Thread
from typing import Any, Final
from webrtc_noise_gain import AudioProcessor

_LOGGER: Incomplete
STORAGE_KEY: Incomplete
STORAGE_VERSION: int
STORAGE_VERSION_MINOR: int
ENGINE_LANGUAGE_PAIRS: Incomplete

def validate_language(data: dict[str, Any]) -> Any: ...

PIPELINE_FIELDS: Incomplete
STORED_PIPELINE_RUNS: int
SAVE_DELAY: int
AUDIO_PROCESSOR_SAMPLES: Final[int]
AUDIO_PROCESSOR_BYTES: Final[Incomplete]

async def _async_resolve_default_pipeline_settings(hass: HomeAssistant, stt_engine_id: str | None, tts_engine_id: str | None) -> dict[str, str | None]: ...
async def _async_create_default_pipeline(hass: HomeAssistant, pipeline_store: PipelineStorageCollection) -> Pipeline: ...
async def async_create_default_pipeline(hass: HomeAssistant, stt_engine_id: str, tts_engine_id: str) -> Pipeline | None: ...
def async_get_pipeline(hass: HomeAssistant, pipeline_id: str | None = ...) -> Pipeline: ...
def async_get_pipelines(hass: HomeAssistant) -> Iterable[Pipeline]: ...

class PipelineEventType(StrEnum):
    RUN_START: str
    RUN_END: str
    WAKE_WORD_START: str
    WAKE_WORD_END: str
    STT_START: str
    STT_VAD_START: str
    STT_VAD_END: str
    STT_END: str
    INTENT_START: str
    INTENT_END: str
    TTS_START: str
    TTS_END: str
    ERROR: str

class PipelineEvent:
    type: PipelineEventType
    data: dict[str, Any] | None
    timestamp: str
    def __init__(self, type, data, timestamp) -> None: ...
PipelineEventCallback = Callable[[PipelineEvent], None]

class Pipeline:
    conversation_engine: str
    conversation_language: str
    language: str
    name: str
    stt_engine: str | None
    stt_language: str | None
    tts_engine: str | None
    tts_language: str | None
    tts_voice: str | None
    wake_word_entity: str | None
    wake_word_id: str | None
    id: str
    @classmethod
    def from_json(cls, data: dict[str, Any]) -> Pipeline: ...
    def to_json(self) -> dict[str, Any]: ...
    def __init__(self, conversation_engine, conversation_language, language, name, stt_engine, stt_language, tts_engine, tts_language, tts_voice, wake_word_entity, wake_word_id, id) -> None: ...

class PipelineStage(StrEnum):
    WAKE_WORD: str
    STT: str
    INTENT: str
    TTS: str

PIPELINE_STAGE_ORDER: Incomplete

class PipelineRunValidationError(Exception): ...

class InvalidPipelineStagesError(PipelineRunValidationError):
    def __init__(self, start_stage: PipelineStage, end_stage: PipelineStage) -> None: ...

class WakeWordSettings:
    timeout: float | None
    audio_seconds_to_buffer: float
    cooldown_seconds: float
    def __init__(self, timeout, audio_seconds_to_buffer, cooldown_seconds) -> None: ...

class AudioSettings:
    noise_suppression_level: int
    auto_gain_dbfs: int
    volume_multiplier: float
    is_vad_enabled: bool
    is_chunking_enabled: bool
    def __post_init__(self) -> None: ...
    @property
    def needs_processor(self) -> bool: ...
    def __init__(self, noise_suppression_level, auto_gain_dbfs, volume_multiplier, is_vad_enabled, is_chunking_enabled) -> None: ...

class ProcessedAudioChunk:
    audio: bytes
    timestamp_ms: int
    is_speech: bool | None
    def __init__(self, audio, timestamp_ms, is_speech) -> None: ...

class PipelineRun:
    hass: HomeAssistant
    context: Context
    pipeline: Pipeline
    start_stage: PipelineStage
    end_stage: PipelineStage
    event_callback: PipelineEventCallback
    language: str
    runner_data: Any | None
    intent_agent: str | None
    tts_audio_output: str | None
    wake_word_settings: WakeWordSettings | None
    audio_settings: AudioSettings
    id: str
    stt_provider: stt.SpeechToTextEntity | stt.Provider
    tts_engine: str
    tts_options: dict | None
    wake_word_entity_id: str | None
    wake_word_entity: wake_word.WakeWordDetectionEntity
    abort_wake_word_detection: bool
    debug_recording_thread: Thread | None
    debug_recording_queue: Queue[str | bytes | None] | None
    audio_processor: AudioProcessor | None
    audio_processor_buffer: AudioBuffer
    def __post_init__(self) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def process_event(self, event: PipelineEvent) -> None: ...
    def start(self, device_id: str | None) -> None: ...
    async def end(self) -> None: ...
    async def prepare_wake_word_detection(self) -> None: ...
    async def wake_word_detection(self, stream: AsyncIterable[ProcessedAudioChunk], audio_chunks_for_stt: list[ProcessedAudioChunk]) -> wake_word.DetectionResult | None: ...
    async def _wake_word_audio_stream(self, audio_stream: AsyncIterable[ProcessedAudioChunk], stt_audio_buffer: deque[ProcessedAudioChunk] | None, wake_word_vad: VoiceActivityTimeout | None, sample_rate: int = ..., sample_width: int = ...) -> AsyncIterable[tuple[bytes, int]]: ...
    async def prepare_speech_to_text(self, metadata: stt.SpeechMetadata) -> None: ...
    async def speech_to_text(self, metadata: stt.SpeechMetadata, stream: AsyncIterable[ProcessedAudioChunk]) -> str: ...
    async def _speech_to_text_stream(self, audio_stream: AsyncIterable[ProcessedAudioChunk], stt_vad: VoiceCommandSegmenter | None, sample_rate: int = ..., sample_width: int = ...) -> AsyncGenerator[bytes, None]: ...
    async def prepare_recognize_intent(self) -> None: ...
    async def recognize_intent(self, intent_input: str, conversation_id: str | None, device_id: str | None) -> str: ...
    async def prepare_text_to_speech(self) -> None: ...
    async def text_to_speech(self, tts_input: str) -> str: ...
    def _start_debug_recording_thread(self, device_id: str | None) -> None: ...
    async def _stop_debug_recording_thread(self) -> None: ...
    async def process_volume_only(self, audio_stream: AsyncIterable[bytes], sample_rate: int = ..., sample_width: int = ...) -> AsyncGenerator[ProcessedAudioChunk, None]: ...
    async def process_enhance_audio(self, audio_stream: AsyncIterable[bytes], sample_rate: int = ..., sample_width: int = ...) -> AsyncGenerator[ProcessedAudioChunk, None]: ...
    def __init__(self, hass, context, pipeline, start_stage, end_stage, event_callback, language, runner_data, intent_agent, tts_audio_output, wake_word_settings, audio_settings, id, debug_recording_thread, debug_recording_queue, audio_processor) -> None: ...

def _multiply_volume(chunk: bytes, volume_multiplier: float) -> bytes: ...
def _pipeline_debug_recording_thread_proc(run_recording_dir: Path, queue: Queue[str | bytes | None], message_timeout: float = ...) -> None: ...

class PipelineInput:
    run: PipelineRun
    stt_metadata: stt.SpeechMetadata | None
    stt_stream: AsyncIterable[bytes] | None
    intent_input: str | None
    tts_input: str | None
    conversation_id: str | None
    device_id: str | None
    async def execute(self) -> None: ...
    async def validate(self) -> None: ...
    def __init__(self, run, stt_metadata, stt_stream, intent_input, tts_input, conversation_id, device_id) -> None: ...

class PipelinePreferred(CollectionError):
    item_id: Incomplete
    def __init__(self, item_id: str) -> None: ...

class SerializedPipelineStorageCollection(SerializedStorageCollection):
    preferred_item: str

class PipelineStorageCollection(StorageCollection[Pipeline, SerializedPipelineStorageCollection]):
    _preferred_item: str
    async def _async_load_data(self) -> SerializedPipelineStorageCollection | None: ...
    async def _process_create_data(self, data: dict) -> dict: ...
    def _get_suggested_id(self, info: dict) -> str: ...
    async def _update_data(self, item: Pipeline, update_data: dict) -> Pipeline: ...
    def _create_item(self, item_id: str, data: dict) -> Pipeline: ...
    def _deserialize_item(self, data: dict) -> Pipeline: ...
    def _serialize_item(self, item_id: str, item: Pipeline) -> dict: ...
    async def async_delete_item(self, item_id: str) -> None: ...
    def async_get_preferred_item(self) -> str: ...
    def async_set_preferred_item(self, item_id: str) -> None: ...
    def _data_to_save(self) -> SerializedPipelineStorageCollection: ...

class PipelineStorageCollectionWebsocket(StorageCollectionWebsocket[PipelineStorageCollection]):
    def async_setup(self, hass: HomeAssistant, *, create_list: bool = ..., create_create: bool = ...) -> None: ...
    async def ws_delete_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
    def ws_get_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
    def ws_list_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
    async def ws_set_preferred_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

class PipelineRuns:
    _pipeline_runs: Incomplete
    _pipeline_store: Incomplete
    def __init__(self, pipeline_store: PipelineStorageCollection) -> None: ...
    def add_run(self, pipeline_run: PipelineRun) -> None: ...
    def remove_run(self, pipeline_run: PipelineRun) -> None: ...
    async def _change_listener(self, change_type: str, item_id: str, change: dict) -> None: ...

class PipelineData:
    pipeline_store: Incomplete
    pipeline_debug: Incomplete
    pipeline_devices: Incomplete
    pipeline_runs: Incomplete
    def __init__(self, pipeline_store: PipelineStorageCollection) -> None: ...

class PipelineRunDebug:
    events: list[PipelineEvent]
    timestamp: str
    def __init__(self) -> None: ...

class PipelineStore(Store[SerializedPipelineStorageCollection]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: SerializedPipelineStorageCollection) -> SerializedPipelineStorageCollection: ...

async def async_setup_pipeline_store(hass: HomeAssistant) -> PipelineData: ...
