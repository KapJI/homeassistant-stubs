from .browse_media import build_item_response as build_item_response
from .const import DOMAIN as DOMAIN
from .coordinator import XboxConfigEntry as XboxConfigEntry
from .entity import XboxConsoleBaseEntity as XboxConsoleBaseEntity, to_https as to_https
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pythonxbox.api.provider.catalog.models import Image as Image
from pythonxbox.api.provider.smartglass.models import PlaybackState, PowerState
from typing import Any, Concatenate, override

_LOGGER: Incomplete
PARALLEL_UPDATES: int
SUPPORT_XBOX: Incomplete
XBOX_STATE_MAP: dict[PlaybackState | PowerState, MediaPlayerState | None]

async def async_setup_entry(hass: HomeAssistant, entry: XboxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def exception_handler[**_P, _R](func: Callable[Concatenate[XboxMediaPlayer, _P], Awaitable[_R]]) -> Callable[Concatenate[XboxMediaPlayer, _P], Coroutine[Any, Any, _R]]: ...

class XboxMediaPlayer(XboxConsoleBaseEntity, MediaPlayerEntity):
    _attr_media_image_remotely_accessible: bool
    _attr_translation_key: str
    @property
    @override
    def state(self) -> MediaPlayerState | None: ...
    @property
    @override
    def supported_features(self) -> MediaPlayerEntityFeature: ...
    @property
    @override
    def media_content_type(self) -> MediaType: ...
    @property
    @override
    def media_content_id(self) -> str | None: ...
    @property
    @override
    def media_title(self) -> str | None: ...
    @property
    @override
    def media_image_url(self) -> str | None: ...
    @exception_handler
    @override
    async def async_turn_on(self) -> None: ...
    @exception_handler
    @override
    async def async_turn_off(self) -> None: ...
    _attr_is_volume_muted: Incomplete
    @exception_handler
    @override
    async def async_mute_volume(self, mute: bool) -> None: ...
    @exception_handler
    @override
    async def async_volume_up(self) -> None: ...
    @exception_handler
    @override
    async def async_volume_down(self) -> None: ...
    @exception_handler
    @override
    async def async_media_play(self) -> None: ...
    @exception_handler
    @override
    async def async_media_pause(self) -> None: ...
    @exception_handler
    @override
    async def async_media_previous_track(self) -> None: ...
    @exception_handler
    @override
    async def async_media_next_track(self) -> None: ...
    @override
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
    @exception_handler
    @override
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...

def _find_media_image(images: list[Image]) -> Image | None: ...
