from .const import DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .views import async_generate_event_video_url as async_generate_event_video_url, async_generate_thumbnail_url as async_generate_thumbnail_url
from _typeshed import Incomplete
from datetime import date, datetime, timedelta
from enum import Enum
from homeassistant.components.camera import CameraImageView as CameraImageView
from homeassistant.components.media_player import BrowseError as BrowseError, MediaClass as MediaClass
from homeassistant.components.media_source.models import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as er
from pyunifiprotect.data import Camera, Event, EventType
from typing import Any, NoReturn

VIDEO_FORMAT: str
THUMBNAIL_WIDTH: int
THUMBNAIL_HEIGHT: int

class SimpleEventType(str, Enum):
    ALL: str
    RING: str
    MOTION: str
    SMART: str

class IdentifierType(str, Enum):
    EVENT: str
    EVENT_THUMB: str
    BROWSE: str

class IdentifierTimeType(str, Enum):
    RECENT: str
    RANGE: str

EVENT_MAP: Incomplete
EVENT_NAME_MAP: Incomplete

def get_ufp_event(event_type: SimpleEventType) -> EventType | None: ...
async def async_get_media_source(hass: HomeAssistant) -> MediaSource: ...
def _get_month_start_end(start: datetime) -> tuple[datetime, datetime]: ...
def _bad_identifier(identifier: str, err: Exception | None = None) -> NoReturn: ...
def _format_duration(duration: timedelta) -> str: ...

class ProtectMediaSource(MediaSource):
    name: str
    _registry: er.EntityRegistry | None
    hass: Incomplete
    data_sources: Incomplete
    def __init__(self, hass: HomeAssistant, data_sources: dict[str, ProtectData]) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    def _parse_range(self, parts: list[str]) -> tuple[date, bool, bool]: ...
    async def _resolve_event(self, data: ProtectData, event_id: str, thumbnail_only: bool = False) -> BrowseMediaSource: ...
    def async_get_registry(self) -> er.EntityRegistry: ...
    def _breadcrumb(self, data: ProtectData, base_title: str, camera: Camera | None = None, event_type: SimpleEventType | None = None, count: int | None = None) -> str: ...
    async def _build_event(self, data: ProtectData, event: dict[str, Any] | Event, thumbnail_only: bool = False) -> BrowseMediaSource: ...
    async def _build_events(self, data: ProtectData, start: datetime, end: datetime, camera_id: str | None = None, event_type: EventType | None = None, reserve: bool = False) -> list[BrowseMediaSource]: ...
    async def _build_recent(self, data: ProtectData, camera_id: str, event_type: SimpleEventType, days: int, build_children: bool = False) -> BrowseMediaSource: ...
    async def _build_month(self, data: ProtectData, camera_id: str, event_type: SimpleEventType, start: date, build_children: bool = False) -> BrowseMediaSource: ...
    async def _build_days(self, data: ProtectData, camera_id: str, event_type: SimpleEventType, start: date, is_all: bool = True, build_children: bool = False) -> BrowseMediaSource: ...
    async def _build_events_type(self, data: ProtectData, camera_id: str, event_type: SimpleEventType, build_children: bool = False) -> BrowseMediaSource: ...
    async def _get_camera_thumbnail_url(self, camera: Camera) -> str | None: ...
    async def _build_camera(self, data: ProtectData, camera_id: str, build_children: bool = False) -> BrowseMediaSource: ...
    async def _build_cameras(self, data: ProtectData) -> list[BrowseMediaSource]: ...
    async def _build_console(self, data: ProtectData) -> BrowseMediaSource: ...
    async def _build_sources(self) -> BrowseMediaSource: ...
