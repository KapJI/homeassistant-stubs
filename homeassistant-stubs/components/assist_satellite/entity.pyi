import abc
import asyncio
from .const import AssistSatelliteEntityFeature as AssistSatelliteEntityFeature, PREANNOUNCE_URL as PREANNOUNCE_URL
from .errors import AssistSatelliteError as AssistSatelliteError, SatelliteBusyError as SatelliteBusyError
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import AsyncIterable
from dataclasses import dataclass, field
from enum import StrEnum
from hassil.expression import Expression as Expression
from homeassistant.components import conversation as conversation, media_source as media_source, stt as stt, tts as tts
from homeassistant.components.assist_pipeline import AudioSettings as AudioSettings, OPTION_PREFERRED as OPTION_PREFERRED, PipelineEvent as PipelineEvent, PipelineEventType as PipelineEventType, PipelineStage as PipelineStage, async_get_pipeline as async_get_pipeline, async_get_pipelines as async_get_pipelines, async_pipeline_from_audio_stream as async_pipeline_from_audio_stream, vad as vad
from homeassistant.components.media_player import async_process_play_media_url as async_process_play_media_url
from homeassistant.core import Context as Context, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import chat_session as chat_session, entity as entity
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from typing import Any, Literal, final

_LOGGER: Incomplete

class AssistSatelliteState(StrEnum):
    IDLE = 'idle'
    LISTENING = 'listening'
    PROCESSING = 'processing'
    RESPONDING = 'responding'

class AssistSatelliteEntityDescription(EntityDescription, frozen_or_thawed=True): ...

@dataclass(frozen=True)
class AssistSatelliteWakeWord:
    id: str
    wake_word: str
    trained_languages: list[str]

@dataclass
class AssistSatelliteConfiguration:
    available_wake_words: list[AssistSatelliteWakeWord]
    active_wake_words: list[str]
    max_active_wake_words: int

@dataclass
class AssistSatelliteAnnouncement:
    message: str
    media_id: str
    original_media_id: str
    tts_token: str | None
    media_id_source: Literal['url', 'media_id', 'tts']
    preannounce_media_id: str | None = ...

@dataclass
class AssistSatelliteAnswer:
    id: str | None
    sentence: str
    slots: dict[str, Any] = field(default_factory=dict)

class AssistSatelliteEntity(entity.Entity, metaclass=abc.ABCMeta):
    entity_description: AssistSatelliteEntityDescription
    _attr_should_poll: bool
    _attr_supported_features: Incomplete
    _attr_pipeline_entity_id: str | None
    _attr_vad_sensitivity_entity_id: str | None
    _conversation_id: str | None
    _run_has_tts: bool
    _is_announcing: bool
    _extra_system_prompt: str | None
    _wake_word_intercept_future: asyncio.Future[str | None] | None
    _attr_tts_options: dict[str, Any] | None
    _pipeline_task: asyncio.Task | None
    _ask_question_future: asyncio.Future[str | None] | None
    __assist_satellite_state: Incomplete
    @final
    @property
    def state(self) -> str | None: ...
    @property
    def pipeline_entity_id(self) -> str | None: ...
    @property
    def vad_sensitivity_entity_id(self) -> str | None: ...
    @property
    def tts_options(self) -> dict[str, Any] | None: ...
    @callback
    @abstractmethod
    def async_get_configuration(self) -> AssistSatelliteConfiguration: ...
    @abstractmethod
    async def async_set_configuration(self, config: AssistSatelliteConfiguration) -> None: ...
    async def async_intercept_wake_word(self) -> str | None: ...
    async def async_internal_announce(self, message: str | None = None, media_id: str | None = None, preannounce: bool = True, preannounce_media_id: str = ...) -> None: ...
    async def async_announce(self, announcement: AssistSatelliteAnnouncement) -> None: ...
    async def async_internal_start_conversation(self, start_message: str | None = None, start_media_id: str | None = None, extra_system_prompt: str | None = None, preannounce: bool = True, preannounce_media_id: str = ...) -> None: ...
    async def async_start_conversation(self, start_announcement: AssistSatelliteAnnouncement) -> None: ...
    async def async_internal_ask_question(self, question: str | None = None, question_media_id: str | None = None, preannounce: bool = True, preannounce_media_id: str = ..., answers: list[dict[str, Any]] | None = None) -> AssistSatelliteAnswer | None: ...
    def _question_response_to_answer(self, response_text: str, answers: list[dict[str, Any]]) -> AssistSatelliteAnswer: ...
    async def async_accept_pipeline_from_satellite(self, audio_stream: AsyncIterable[bytes], start_stage: PipelineStage = ..., end_stage: PipelineStage = ..., wake_word_phrase: str | None = None) -> None: ...
    async def _cancel_running_pipeline(self) -> None: ...
    @abstractmethod
    def on_pipeline_event(self, event: PipelineEvent) -> None: ...
    @callback
    def _internal_on_pipeline_event(self, event: PipelineEvent) -> None: ...
    @callback
    def _set_state(self, state: AssistSatelliteState) -> None: ...
    @callback
    def tts_response_finished(self) -> None: ...
    @callback
    def _resolve_pipeline(self) -> str | None: ...
    @callback
    def _resolve_vad_sensitivity(self) -> float: ...
    async def _resolve_announcement_media_id(self, message: str, media_id: str | None, preannounce_media_id: str | None = None) -> AssistSatelliteAnnouncement: ...

def _collect_list_references(expression: Expression, list_names: set[str]) -> None: ...
