import asyncio
from .const import DOMAIN as DOMAIN
from .entry_data import RuntimeEntryData as RuntimeEntryData
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import VoiceAssistantEventType
from collections.abc import AsyncIterable, Callable as Callable
from homeassistant.components import stt as stt, tts as tts
from homeassistant.components.assist_pipeline import PipelineEvent as PipelineEvent, PipelineEventType as PipelineEventType, async_pipeline_from_audio_stream as async_pipeline_from_audio_stream
from homeassistant.components.media_player import async_process_play_media_url as async_process_play_media_url
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, callback as callback

_LOGGER: Incomplete
UDP_PORT: int
UDP_MAX_PACKET_SIZE: int
_VOICE_ASSISTANT_EVENT_TYPES: EsphomeEnumMapper[VoiceAssistantEventType, PipelineEventType]

class VoiceAssistantUDPServer(asyncio.DatagramProtocol):
    started: bool
    queue: asyncio.Queue[bytes] | None
    transport: asyncio.DatagramTransport | None
    remote_addr: tuple[str, int] | None
    context: Incomplete
    hass: Incomplete
    device_info: Incomplete
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
    async def run_pipeline(self, pipeline_timeout: float = ...) -> None: ...
    async def _send_tts(self, media_id: str) -> None: ...
