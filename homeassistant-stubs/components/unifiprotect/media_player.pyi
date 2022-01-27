from .const import DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityDescription as MediaPlayerEntityDescription
from homeassistant.components.media_player.const import MEDIA_TYPE_MUSIC as MEDIA_TYPE_MUSIC, SUPPORT_PLAY_MEDIA as SUPPORT_PLAY_MEDIA, SUPPORT_STOP as SUPPORT_STOP, SUPPORT_VOLUME_SET as SUPPORT_VOLUME_SET, SUPPORT_VOLUME_STEP as SUPPORT_VOLUME_STEP
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_IDLE as STATE_IDLE, STATE_PLAYING as STATE_PLAYING
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data import Camera as Camera
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectMediaPlayer(ProtectDeviceEntity, MediaPlayerEntity):
    device: Camera
    entity_description: MediaPlayerEntityDescription
    _attr_name: Any
    _attr_supported_features: Any
    _attr_media_content_type: Any
    def __init__(self, data: ProtectData, camera: Camera) -> None: ...
    _attr_volume_level: Any
    _attr_state: Any
    def _async_update_device_from_protect(self) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_play_media(self, media_type: str, media_id: str, **kwargs: Any) -> None: ...
