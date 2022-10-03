from .const import DOMAIN as DOMAIN, TYPE_TO_PLATFORM as TYPE_TO_PLATFORM
from .coordinator import LookinDataUpdateCoordinator as LookinDataUpdateCoordinator
from .entity import LookinPowerPushRemoteEntity as LookinPowerPushRemoteEntity
from .models import LookinData as LookinData
from _typeshed import Incomplete
from aiolookin import Remote as Remote
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

LOGGER: Incomplete
_TYPE_TO_DEVICE_CLASS: Incomplete
_FUNCTION_NAME_TO_FEATURE: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LookinMedia(LookinPowerPushRemoteEntity, MediaPlayerEntity):
    _attr_should_poll: bool
    _attr_device_class: Incomplete
    _attr_supported_features: int
    def __init__(self, coordinator: LookinDataUpdateCoordinator, uuid: str, device: Remote, lookin_data: LookinData, device_class: str) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    _attr_is_volume_muted: Incomplete
    async def async_mute_volume(self, mute: bool) -> None: ...
    _attr_state: Incomplete
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    def _update_from_status(self, status: str) -> None: ...
