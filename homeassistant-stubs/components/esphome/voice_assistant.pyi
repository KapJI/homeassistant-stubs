import asyncio
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import VoiceAssistantEventType
from collections.abc import AsyncIterable, Callable as Callable
from homeassistant.components import stt as stt
from homeassistant.components.assist_pipeline import PipelineEvent as PipelineEvent, PipelineEventType as PipelineEventType, async_pipeline_from_audio_stream as async_pipeline_from_audio_stream
from homeassistant.components.media_player import async_process_play_media_url as async_process_play_media_url
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, callback as callback

_LOGGER: Incomplete
UDP_PORT: int
_VOICE_ASSISTANT_EVENT_TYPES: EsphomeEnumMapper[VoiceAssistantEventType, PipelineEventType]

class VoiceAssistantUDPServer(asyncio.DatagramProtocol):
    started: bool
    queue: asyncio.Queue[bytes] | None
    transport: asyncio.DatagramTransport | None
    context: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def start_server(self) -> int: ...
    def connection_made(self, transport: asyncio.BaseTransport) -> None: ...
    def datagram_received(self, data: bytes, addr: tuple[str, int]) -> None: ...
    def error_received(self, exc: Exception) -> None: ...
    def stop(self) -> None: ...
    async def _iterate_packets(self) -> AsyncIterable[bytes]: ...
    async def run_pipeline(self, handle_event: Callable[[VoiceAssistantEventType, dict[str, str] | None], None]) -> None: ...
