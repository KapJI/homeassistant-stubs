from .const import DOMAIN as DOMAIN, TYPE_TO_PLATFORM as TYPE_TO_PLATFORM
from .coordinator import LookinDataUpdateCoordinator as LookinDataUpdateCoordinator
from .entity import LookinPowerPushRemoteEntity as LookinPowerPushRemoteEntity
from .models import LookinData as LookinData
from aiolookin import Remote as Remote
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity
from homeassistant.components.media_player.const import SUPPORT_NEXT_TRACK as SUPPORT_NEXT_TRACK, SUPPORT_PREVIOUS_TRACK as SUPPORT_PREVIOUS_TRACK, SUPPORT_TURN_OFF as SUPPORT_TURN_OFF, SUPPORT_TURN_ON as SUPPORT_TURN_ON, SUPPORT_VOLUME_MUTE as SUPPORT_VOLUME_MUTE, SUPPORT_VOLUME_STEP as SUPPORT_VOLUME_STEP
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform, STATE_ON as STATE_ON, STATE_STANDBY as STATE_STANDBY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

LOGGER: Any
_TYPE_TO_DEVICE_CLASS: Any
_FUNCTION_NAME_TO_FEATURE: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LookinMedia(LookinPowerPushRemoteEntity, MediaPlayerEntity):
    _attr_should_poll: bool
    _attr_device_class: Any
    _attr_supported_features: int
    def __init__(self, coordinator: LookinDataUpdateCoordinator, uuid: str, device: Remote, lookin_data: LookinData, device_class: str) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    _attr_is_volume_muted: Any
    async def async_mute_volume(self, mute: bool) -> None: ...
    _attr_state: Any
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    def _update_from_status(self, status: str) -> None: ...
