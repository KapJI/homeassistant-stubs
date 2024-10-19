import abc
import asyncio
from .const import AssistSatelliteEntityFeature as AssistSatelliteEntityFeature
from .errors import AssistSatelliteError as AssistSatelliteError, SatelliteBusyError as SatelliteBusyError
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import AsyncIterable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components import media_source as media_source, stt as stt, tts as tts
from homeassistant.components.assist_pipeline import AudioSettings as AudioSettings, OPTION_PREFERRED as OPTION_PREFERRED, PipelineEvent as PipelineEvent, PipelineEventType as PipelineEventType, PipelineStage as PipelineStage, async_get_pipeline as async_get_pipeline, async_get_pipelines as async_get_pipelines, async_pipeline_from_audio_stream as async_pipeline_from_audio_stream, vad as vad
from homeassistant.components.media_player import async_process_play_media_url as async_process_play_media_url
from homeassistant.core import Context as Context, callback as callback
from homeassistant.helpers import entity as entity
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from typing import Any, Final, Literal

_CONVERSATION_TIMEOUT_SEC: Final[Incomplete]
_LOGGER: Incomplete

class AssistSatelliteState(StrEnum):
    IDLE = 'idle'
    LISTENING = 'listening'
    PROCESSING = 'processing'
    RESPONDING = 'responding'

class AssistSatelliteEntityDescription(EntityDescription, frozen_or_thawed=True):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...
    def __replace__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...

@dataclass(frozen=True)
class AssistSatelliteWakeWord:
    id: str
    wake_word: str
    trained_languages: list[str]
    def __init__(self, id, wake_word, trained_languages) -> None: ...

@dataclass
class AssistSatelliteConfiguration:
    available_wake_words: list[AssistSatelliteWakeWord]
    active_wake_words: list[str]
    max_active_wake_words: int
    def __init__(self, available_wake_words, active_wake_words, max_active_wake_words) -> None: ...

@dataclass
class AssistSatelliteAnnouncement:
    message: str
    media_id: str
    media_id_source: Literal['url', 'media_id', 'tts']
    def __init__(self, message, media_id, media_id_source) -> None: ...

class AssistSatelliteEntity(entity.Entity, metaclass=abc.ABCMeta):
    entity_description: AssistSatelliteEntityDescription
    _attr_should_poll: bool
    _attr_supported_features: Incomplete
    _attr_pipeline_entity_id: str | None
    _attr_vad_sensitivity_entity_id: str | None
    _conversation_id: str | None
    _conversation_id_time: float | None
    _run_has_tts: bool
    _is_announcing: bool
    _wake_word_intercept_future: asyncio.Future[str | None] | None
    _attr_tts_options: dict[str, Any] | None
    _pipeline_task: asyncio.Task | None
    __assist_satellite_state: Incomplete
    @property
    def state(self) -> str | None: ...
    @property
    def pipeline_entity_id(self) -> str | None: ...
    @property
    def vad_sensitivity_entity_id(self) -> str | None: ...
    @property
    def tts_options(self) -> dict[str, Any] | None: ...
    @abstractmethod
    def async_get_configuration(self) -> AssistSatelliteConfiguration: ...
    @abstractmethod
    async def async_set_configuration(self, config: AssistSatelliteConfiguration) -> None: ...
    async def async_intercept_wake_word(self) -> str | None: ...
    async def async_internal_announce(self, message: str | None = None, media_id: str | None = None) -> None: ...
    async def async_announce(self, announcement: AssistSatelliteAnnouncement) -> None: ...
    async def async_accept_pipeline_from_satellite(self, audio_stream: AsyncIterable[bytes], start_stage: PipelineStage = ..., end_stage: PipelineStage = ..., wake_word_phrase: str | None = None) -> None: ...
    async def _cancel_running_pipeline(self) -> None: ...
    @abstractmethod
    def on_pipeline_event(self, event: PipelineEvent) -> None: ...
    def _internal_on_pipeline_event(self, event: PipelineEvent) -> None: ...
    def _set_state(self, state: AssistSatelliteState) -> None: ...
    def tts_response_finished(self) -> None: ...
    def _resolve_pipeline(self) -> str | None: ...
    def _resolve_vad_sensitivity(self) -> float: ...
