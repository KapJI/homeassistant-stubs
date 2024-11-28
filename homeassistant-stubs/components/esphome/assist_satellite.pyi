import asyncio
from .const import DOMAIN as DOMAIN
from .entity import EsphomeAssistEntity as EsphomeAssistEntity
from .entry_data import ESPHomeConfigEntry as ESPHomeConfigEntry, RuntimeEntryData as RuntimeEntryData
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from .ffmpeg_proxy import async_create_proxy_url as async_create_proxy_url
from _typeshed import Incomplete
from aioesphomeapi import MediaPlayerSupportedFormat as MediaPlayerSupportedFormat, VoiceAssistantAnnounceFinished as VoiceAssistantAnnounceFinished, VoiceAssistantAudioSettings as VoiceAssistantAudioSettings, VoiceAssistantEventType, VoiceAssistantTimerEventType
from collections.abc import AsyncIterable
from homeassistant.components import assist_satellite as assist_satellite, tts as tts
from homeassistant.components.assist_pipeline import PipelineEvent as PipelineEvent, PipelineEventType as PipelineEventType, PipelineStage as PipelineStage
from homeassistant.components.intent import TimerEventType as TimerEventType, TimerInfo as TimerInfo, async_register_timer_handler as async_register_timer_handler
from homeassistant.components.media_player import async_process_play_media_url as async_process_play_media_url
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete
_VOICE_ASSISTANT_EVENT_TYPES: EsphomeEnumMapper[VoiceAssistantEventType, PipelineEventType]
_TIMER_EVENT_TYPES: EsphomeEnumMapper[VoiceAssistantTimerEventType, TimerEventType]
_ANNOUNCEMENT_TIMEOUT_SEC: Incomplete
_CONFIG_TIMEOUT_SEC: int

async def async_setup_entry(hass: HomeAssistant, entry: ESPHomeConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeAssistSatellite(EsphomeAssistEntity, assist_satellite.AssistSatelliteEntity):
    entity_description: Incomplete
    config_entry: Incomplete
    entry_data: Incomplete
    cli: Incomplete
    _is_running: bool
    _pipeline_task: Incomplete
    _audio_queue: Incomplete
    _tts_streaming_task: Incomplete
    _udp_server: Incomplete
    _satellite_config: Incomplete
    def __init__(self, config_entry: ConfigEntry, entry_data: RuntimeEntryData) -> None: ...
    @property
    def pipeline_entity_id(self) -> str | None: ...
    @property
    def vad_sensitivity_entity_id(self) -> str | None: ...
    def async_get_configuration(self) -> assist_satellite.AssistSatelliteConfiguration: ...
    async def async_set_configuration(self, config: assist_satellite.AssistSatelliteConfiguration) -> None: ...
    async def _update_satellite_config(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def on_pipeline_event(self, event: PipelineEvent) -> None: ...
    async def async_announce(self, announcement: assist_satellite.AssistSatelliteAnnouncement) -> None: ...
    _attr_tts_options: Incomplete
    async def handle_pipeline_start(self, conversation_id: str, flags: int, audio_settings: VoiceAssistantAudioSettings, wake_word_phrase: str | None) -> int | None: ...
    async def handle_audio(self, data: bytes) -> None: ...
    async def handle_pipeline_stop(self, abort: bool) -> None: ...
    def handle_pipeline_finished(self) -> None: ...
    def handle_timer_event(self, event_type: TimerEventType, timer_info: TimerInfo) -> None: ...
    async def handle_announcement_finished(self, announce_finished: VoiceAssistantAnnounceFinished) -> None: ...
    def async_set_wake_word(self, wake_word_id: str) -> None: ...
    def _update_tts_format(self) -> None: ...
    async def _stream_tts_audio(self, media_id: str, sample_rate: int = 16000, sample_width: int = 2, sample_channels: int = 1, samples_per_chunk: int = 512) -> None: ...
    async def _wrap_audio_stream(self) -> AsyncIterable[bytes]: ...
    def _stop_pipeline(self) -> None: ...
    def _abort_pipeline(self) -> None: ...
    async def _start_udp_server(self) -> int: ...
    def _stop_udp_server(self) -> None: ...

class VoiceAssistantUDPServer(asyncio.DatagramProtocol):
    transport: asyncio.DatagramTransport | None
    remote_addr: tuple[str, int] | None
    _audio_queue: Incomplete
    def __init__(self, audio_queue: asyncio.Queue[bytes | None], *args: Any, **kwargs: Any) -> None: ...
    def connection_made(self, transport: asyncio.BaseTransport) -> None: ...
    def datagram_received(self, data: bytes, addr: tuple[str, int]) -> None: ...
    def error_received(self, exc: Exception) -> None: ...
    def close(self) -> None: ...
    def send_audio_bytes(self, data: bytes) -> None: ...
