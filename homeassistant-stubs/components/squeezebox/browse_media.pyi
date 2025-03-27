from .const import UNPLAYABLE_TYPES as UNPLAYABLE_TYPES
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseError as BrowseError, BrowseMedia as BrowseMedia, MediaClass as MediaClass, MediaPlayerEntity as MediaPlayerEntity, MediaType as MediaType
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.network import is_internal_request as is_internal_request
from pysqueezebox import Player as Player
from typing import Any

LIBRARY: Incomplete
MEDIA_TYPE_TO_SQUEEZEBOX: dict[str | MediaType, str]
SQUEEZEBOX_ID_BY_TYPE: dict[str | MediaType, str]
CONTENT_TYPE_MEDIA_CLASS: dict[str | MediaType, dict[str, MediaClass | str]]
CONTENT_TYPE_TO_CHILD_TYPE: dict[str | MediaType, str | MediaType | None]

@dataclass
class BrowseData:
    content_type_to_child_type: dict[str | MediaType, str | MediaType | None] = field(default_factory=dict)
    content_type_media_class: dict[str | MediaType, dict[str, MediaClass | str]] = field(default_factory=dict)
    squeezebox_id_by_type: dict[str | MediaType, str] = field(default_factory=dict)
    media_type_to_squeezebox: dict[str | MediaType, str] = field(default_factory=dict)
    known_apps_radios: set[str] = field(default_factory=set)
    def __post_init__(self) -> None: ...

def _add_new_command_to_browse_data(browse_data: BrowseData, cmd: str | MediaType, type: str) -> None: ...
def _build_response_apps_radios_category(browse_data: BrowseData, cmd: str | MediaType, item: dict[str, Any]) -> BrowseMedia: ...
def _build_response_known_app(browse_data: BrowseData, search_type: str, item: dict[str, Any]) -> BrowseMedia: ...
def _build_response_favorites(item: dict[str, Any]) -> BrowseMedia: ...
def _get_item_thumbnail(item: dict[str, Any], player: Player, entity: MediaPlayerEntity, item_type: str | MediaType | None, search_type: str, internal_request: bool) -> str | None: ...
async def build_item_response(entity: MediaPlayerEntity, player: Player, payload: dict[str, str | None], browse_limit: int, browse_data: BrowseData) -> BrowseMedia: ...
async def library_payload(hass: HomeAssistant, player: Player, browse_media: BrowseData) -> BrowseMedia: ...
def media_source_content_filter(item: BrowseMedia) -> bool: ...
async def generate_playlist(player: Player, payload: dict[str, str], browse_limit: int, browse_media: BrowseData) -> list | None: ...
