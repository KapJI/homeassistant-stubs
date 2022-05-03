from .const import CONTENT_AUTH_EXPIRY_TIME as CONTENT_AUTH_EXPIRY_TIME, MEDIA_CLASS_DIRECTORY as MEDIA_CLASS_DIRECTORY
from _typeshed import Incomplete
from homeassistant.components.http.auth import async_sign_path as async_sign_path
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_supervisor_network_url as get_supervisor_network_url, get_url as get_url, is_hass_url as is_hass_url

PATHS_WITHOUT_AUTH: Incomplete

def async_process_play_media_url(hass: HomeAssistant, media_content_id: str, *, allow_relative_url: bool = ..., for_supervisor_network: bool = ...) -> str: ...

class BrowseMedia:
    media_class: Incomplete
    media_content_id: Incomplete
    media_content_type: Incomplete
    title: Incomplete
    can_play: Incomplete
    can_expand: Incomplete
    children: Incomplete
    children_media_class: Incomplete
    thumbnail: Incomplete
    not_shown: Incomplete
    def __init__(self, *, media_class: str, media_content_id: str, media_content_type: str, title: str, can_play: bool, can_expand: bool, children: Union[list[BrowseMedia], None] = ..., children_media_class: Union[str, None] = ..., thumbnail: Union[str, None] = ..., not_shown: int = ...) -> None: ...
    def as_dict(self, *, parent: bool = ...) -> dict: ...
    def calculate_children_class(self) -> None: ...
    def __repr__(self) -> str: ...
