import asyncio
from .const import DOMAIN as DOMAIN
from .entry_data import RuntimeEntryData as RuntimeEntryData
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import VoiceAssistantAudioSettings, VoiceAssistantEventType
from collections.abc import AsyncIterable, Callable as Callable
from homeassistant.components import stt as stt, tts as tts
from homeassistant.components.assist_pipeline import AudioSettings as AudioSettings, PipelineEvent as PipelineEvent, PipelineEventType as PipelineEventType, PipelineNotFound as PipelineNotFound, PipelineStage as PipelineStage, WakeWordSettings as WakeWordSettings, async_pipeline_from_audio_stream as async_pipeline_from_audio_stream
from homeassistant.components.assist_pipeline.error import WakeWordDetectionAborted as WakeWordDetectionAborted, WakeWordDetectionError as WakeWordDetectionError
from homeassistant.components.media_player import async_process_play_media_url as async_process_play_media_url
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, callback as callback

_LOGGER: Incomplete
UDP_PORT: int
UDP_MAX_PACKET_SIZE: int
_VOICE_ASSISTANT_EVENT_TYPES: EsphomeEnumMapper[VoiceAssistantEventType, PipelineEventType]

class VoiceAssistantUDPServer(asyncio.DatagramProtocol):
    started: bool
    stopped: bool
    transport: asyncio.DatagramTransport | None
    remote_addr: tuple[str, int] | None
    context: Incomplete
    hass: Incomplete
    entry_data: Incomplete
    device_info: Incomplete
    queue: Incomplete
    handle_event: Incomplete
    handle_finished: Incomplete
    _tts_done: Incomplete
    def __init__(self, hass: HomeAssistant, entry_data: RuntimeEntryData, handle_event: Callable[[VoiceAssistantEventType, dict[str, str] | None], None], handle_finished: Callable[[], None]) -> None: ...
    async def start_server(self) -> int: ...
    def connection_made(self, transport: asyncio.BaseTransport) -> None: ...
    def datagram_received(self, data: bytes, addr: tuple[str, int]) -> None: ...
    def error_received(self, exc: Exception) -> None: ...
    def stop(self) -> None: ...
    def close(self) -> None: ...
    async def _iterate_packets(self) -> AsyncIterable[bytes]: ...
    def _event_callback(self, event: PipelineEvent) -> None: ...
    async def run_pipeline(self, device_id: str, conversation_id: str | None, flags: int = ..., audio_settings: VoiceAssistantAudioSettings | None = ...) -> None: ...
    async def _send_tts(self, media_id: str) -> None: ...
