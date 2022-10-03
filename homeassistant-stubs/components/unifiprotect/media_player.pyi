from .const import DISPATCH_ADOPT as DISPATCH_ADOPT, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity
from _typeshed import Incomplete
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityDescription as MediaPlayerEntityDescription, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, async_process_play_media_url as async_process_play_media_url
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data import Camera, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, ProtectModelWithId as ProtectModelWithId
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectMediaPlayer(ProtectDeviceEntity, MediaPlayerEntity):
    device: Camera
    entity_description: MediaPlayerEntityDescription
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    _attr_media_content_type: Incomplete
    def __init__(self, data: ProtectData, camera: Camera) -> None: ...
    _attr_volume_level: Incomplete
    _attr_state: Incomplete
    _attr_available: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_play_media(self, media_type: Union[MediaType, str], media_id: str, **kwargs: Any) -> None: ...
    async def async_browse_media(self, media_content_type: Union[MediaType, str, None] = ..., media_content_id: Union[str, None] = ...) -> BrowseMedia: ...
