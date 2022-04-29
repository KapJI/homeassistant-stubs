from .coordinator import RokuDataUpdateCoordinator as RokuDataUpdateCoordinator
from .helpers import format_channel_name as format_channel_name
from _typeshed import Incomplete
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseMedia as BrowseMedia
from homeassistant.components.media_player.const import MEDIA_CLASS_APP as MEDIA_CLASS_APP, MEDIA_CLASS_CHANNEL as MEDIA_CLASS_CHANNEL, MEDIA_CLASS_DIRECTORY as MEDIA_CLASS_DIRECTORY, MEDIA_TYPE_APP as MEDIA_TYPE_APP, MEDIA_TYPE_APPS as MEDIA_TYPE_APPS, MEDIA_TYPE_CHANNEL as MEDIA_TYPE_CHANNEL, MEDIA_TYPE_CHANNELS as MEDIA_TYPE_CHANNELS
from homeassistant.components.media_player.errors import BrowseError as BrowseError
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.network import is_internal_request as is_internal_request

CONTENT_TYPE_MEDIA_CLASS: Incomplete
CONTAINER_TYPES_SPECIFIC_MEDIA_CLASS: Incomplete
PLAYABLE_MEDIA_TYPES: Incomplete
EXPANDABLE_MEDIA_TYPES: Incomplete
GetBrowseImageUrlType: Incomplete

def get_thumbnail_url_full(coordinator: RokuDataUpdateCoordinator, is_internal: bool, get_browse_image_url: GetBrowseImageUrlType, media_content_type: str, media_content_id: str, media_image_id: Union[str, None] = ...) -> Union[str, None]: ...
async def async_browse_media(hass: HomeAssistant, coordinator: RokuDataUpdateCoordinator, get_browse_image_url: GetBrowseImageUrlType, media_content_id: Union[str, None], media_content_type: Union[str, None]) -> BrowseMedia: ...
async def root_payload(hass: HomeAssistant, coordinator: RokuDataUpdateCoordinator, get_browse_image_url: GetBrowseImageUrlType) -> BrowseMedia: ...
def build_item_response(coordinator: RokuDataUpdateCoordinator, payload: dict, get_browse_image_url: GetBrowseImageUrlType) -> Union[BrowseMedia, None]: ...
def item_payload(item: dict, coordinator: RokuDataUpdateCoordinator, get_browse_image_url: GetBrowseImageUrlType) -> BrowseMedia: ...
