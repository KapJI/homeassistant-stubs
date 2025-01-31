from .const import ConfigNotFound as ConfigNotFound, DOMAIN as DOMAIN, LOVELACE_DATA as LOVELACE_DATA
from homeassistant.components.cast.home_assistant_cast import ATTR_URL_PATH as ATTR_URL_PATH, ATTR_VIEW_PATH as ATTR_VIEW_PATH, NO_URL_AVAILABLE_ERROR as NO_URL_AVAILABLE_ERROR, SERVICE_SHOW_VIEW as SERVICE_SHOW_VIEW
from homeassistant.components.media_player import BrowseError as BrowseError, BrowseMedia as BrowseMedia, MediaClass as MediaClass, MediaType as MediaType
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from pychromecast import Chromecast as Chromecast
from typing import Any

DEFAULT_DASHBOARD: str

async def async_get_media_browser_root_object(hass: HomeAssistant, cast_type: str) -> list[BrowseMedia]: ...
async def async_browse_media(hass: HomeAssistant, media_content_type: MediaType | str, media_content_id: str, cast_type: str) -> BrowseMedia | None: ...
async def async_play_media(hass: HomeAssistant, cast_entity_id: str, chromecast: Chromecast, media_type: MediaType | str, media_id: str) -> bool: ...
async def _get_dashboard_info(hass: HomeAssistant, url_path: str | None) -> dict[str, Any]: ...
@callback
def _item_from_info(info: dict) -> BrowseMedia: ...
