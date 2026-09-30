from _typeshed import Incomplete
from collections.abc import Callable
from dataclasses import dataclass, field
from enum import StrEnum
from homeassistant.util import ulid as ulid_util
from typing import Any

class PipelineEventType(StrEnum):
    RUN_START = 'run-start'
    RUN_END = 'run-end'
    WAKE_WORD_START = 'wake_word-start'
    WAKE_WORD_END = 'wake_word-end'
    STT_START = 'stt-start'
    STT_VAD_START = 'stt-vad-start'
    STT_VAD_END = 'stt-vad-end'
    STT_END = 'stt-end'
    INTENT_START = 'intent-start'
    INTENT_PROGRESS = 'intent-progress'
    INTENT_END = 'intent-end'
    TTS_START = 'tts-start'
    TTS_END = 'tts-end'
    ERROR = 'error'

@dataclass(frozen=True)
class PipelineEvent:
    type: PipelineEventType
    data: dict[str, Any] | None = ...
    timestamp: str = field(default_factory=Incomplete)
type PipelineEventCallback = Callable[[PipelineEvent], None]

@dataclass(frozen=True)
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
    prefer_local_intents: bool = ...
    id: str = field(default_factory=ulid_util.ulid_now)
    @classmethod
    def from_json(cls, data: dict[str, Any]) -> Pipeline: ...
    def to_json(self) -> dict[str, Any]: ...

class PipelineStage(StrEnum):
    WAKE_WORD = 'wake_word'
    STT = 'stt'
    INTENT = 'intent'
    TTS = 'tts'
    END = 'end'

PIPELINE_STAGE_ORDER: Incomplete

@dataclass(frozen=True)
class WakeWordSettings:
    timeout: float | None = ...
    audio_seconds_to_buffer: float = ...

@dataclass(frozen=True)
class AudioSettings:
    noise_suppression_level: int = ...
    auto_gain_dbfs: int = ...
    volume_multiplier: float = ...
    is_vad_enabled: bool = ...
    silence_seconds: float = ...
    def __post_init__(self) -> None: ...
    @property
    def needs_processor(self) -> bool: ...
