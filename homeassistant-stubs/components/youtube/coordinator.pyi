from .api import AsyncConfigEntryAuth as AsyncConfigEntryAuth
from .const import ATTR_DESCRIPTION as ATTR_DESCRIPTION, ATTR_IS_SHORT as ATTR_IS_SHORT, ATTR_LATEST_SHORT as ATTR_LATEST_SHORT, ATTR_LATEST_VIDEO as ATTR_LATEST_VIDEO, ATTR_LATEST_VIDEO_NON_SHORT as ATTR_LATEST_VIDEO_NON_SHORT, ATTR_PUBLISHED_AT as ATTR_PUBLISHED_AT, ATTR_SUBSCRIBER_COUNT as ATTR_SUBSCRIBER_COUNT, ATTR_THUMBNAIL as ATTR_THUMBNAIL, ATTR_TITLE as ATTR_TITLE, ATTR_TOTAL_VIEWS as ATTR_TOTAL_VIEWS, ATTR_VIDEO_COUNT as ATTR_VIDEO_COUNT, ATTR_VIDEO_ID as ATTR_VIDEO_ID, CONF_CHANNELS as CONF_CHANNELS, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ICON as ATTR_ICON, ATTR_ID as ATTR_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, override

type YouTubeConfigEntry = ConfigEntry[YouTubeDataUpdateCoordinator]
def _build_video_dict(video: Any, is_short: bool) -> dict[str, Any]: ...

class YouTubeDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: YouTubeConfigEntry
    _auth: Incomplete
    _is_short_cache: dict[str, bool]
    def __init__(self, hass: HomeAssistant, config_entry: YouTubeConfigEntry, auth: AsyncConfigEntryAuth) -> None: ...
    @override
    async def _async_update_data(self) -> dict[str, Any]: ...
    async def _get_is_short_flags(self, youtube: Any, videos: list[Any]) -> list[bool]: ...
