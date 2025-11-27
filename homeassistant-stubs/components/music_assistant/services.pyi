from .const import ATTR_ALBUM as ATTR_ALBUM, ATTR_ALBUMS as ATTR_ALBUMS, ATTR_ALBUM_ARTISTS_ONLY as ATTR_ALBUM_ARTISTS_ONLY, ATTR_ALBUM_TYPE as ATTR_ALBUM_TYPE, ATTR_ANNOUNCE_VOLUME as ATTR_ANNOUNCE_VOLUME, ATTR_ARTIST as ATTR_ARTIST, ATTR_ARTISTS as ATTR_ARTISTS, ATTR_AUDIOBOOKS as ATTR_AUDIOBOOKS, ATTR_AUTO_PLAY as ATTR_AUTO_PLAY, ATTR_FAVORITE as ATTR_FAVORITE, ATTR_ITEMS as ATTR_ITEMS, ATTR_LIBRARY_ONLY as ATTR_LIBRARY_ONLY, ATTR_LIMIT as ATTR_LIMIT, ATTR_MEDIA_ID as ATTR_MEDIA_ID, ATTR_MEDIA_TYPE as ATTR_MEDIA_TYPE, ATTR_OFFSET as ATTR_OFFSET, ATTR_ORDER_BY as ATTR_ORDER_BY, ATTR_PLAYLISTS as ATTR_PLAYLISTS, ATTR_PODCASTS as ATTR_PODCASTS, ATTR_RADIO as ATTR_RADIO, ATTR_RADIO_MODE as ATTR_RADIO_MODE, ATTR_SEARCH as ATTR_SEARCH, ATTR_SEARCH_ALBUM as ATTR_SEARCH_ALBUM, ATTR_SEARCH_ARTIST as ATTR_SEARCH_ARTIST, ATTR_SEARCH_NAME as ATTR_SEARCH_NAME, ATTR_SOURCE_PLAYER as ATTR_SOURCE_PLAYER, ATTR_TRACKS as ATTR_TRACKS, ATTR_URL as ATTR_URL, ATTR_USE_PRE_ANNOUNCE as ATTR_USE_PRE_ANNOUNCE, DOMAIN as DOMAIN
from .helpers import get_music_assistant_client as get_music_assistant_client
from .schemas import LIBRARY_RESULTS_SCHEMA as LIBRARY_RESULTS_SCHEMA, SEARCH_RESULT_SCHEMA as SEARCH_RESULT_SCHEMA, media_item_dict_from_mass_item as media_item_dict_from_mass_item
from homeassistant.components.media_player import ATTR_MEDIA_ENQUEUE as ATTR_MEDIA_ENQUEUE
from homeassistant.const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import service as service
from music_assistant_models.media_items import Album as Album, Artist as Artist, Audiobook as Audiobook, Playlist as Playlist, Podcast as Podcast, Radio as Radio, Track as Track

SERVICE_SEARCH: str
SERVICE_GET_LIBRARY: str
SERVICE_PLAY_MEDIA_ADVANCED: str
SERVICE_PLAY_ANNOUNCEMENT: str
SERVICE_TRANSFER_QUEUE: str
SERVICE_GET_QUEUE: str
DEFAULT_OFFSET: int
DEFAULT_LIMIT: int
DEFAULT_SORT_ORDER: str

@callback
def register_actions(hass: HomeAssistant) -> None: ...
async def handle_search(call: ServiceCall) -> ServiceResponse: ...
async def handle_get_library(call: ServiceCall) -> ServiceResponse: ...
