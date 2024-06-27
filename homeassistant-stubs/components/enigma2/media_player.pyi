from . import Enigma2ConfigEntry as Enigma2ConfigEntry
from .const import CONF_DEEP_STANDBY as CONF_DEEP_STANDBY, CONF_MAC_ADDRESS as CONF_MAC_ADDRESS, CONF_SOURCE_BOUQUET as CONF_SOURCE_BOUQUET, CONF_USE_CHANNEL_ICON as CONF_USE_CHANNEL_ICON, DEFAULT_DEEP_STANDBY as DEFAULT_DEEP_STANDBY, DEFAULT_MAC_ADDRESS as DEFAULT_MAC_ADDRESS, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_PASSWORD as DEFAULT_PASSWORD, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_SOURCE_BOUQUET as DEFAULT_SOURCE_BOUQUET, DEFAULT_SSL as DEFAULT_SSL, DEFAULT_USERNAME as DEFAULT_USERNAME, DEFAULT_USE_CHANNEL_ICON as DEFAULT_USE_CHANNEL_ICON, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.media_player import MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from openwebif.api import OpenWebIfDevice as OpenWebIfDevice

ATTR_MEDIA_CURRENTLY_RECORDING: str
ATTR_MEDIA_DESCRIPTION: str
ATTR_MEDIA_END_TIME: str
ATTR_MEDIA_START_TIME: str
_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: Enigma2ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class Enigma2Device(MediaPlayerEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_media_content_type: Incomplete
    _attr_supported_features: Incomplete
    _device: Incomplete
    _entry: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry: ConfigEntry, device: OpenWebIfDevice, about: dict) -> None: ...
    _attr_available: bool
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
    _attr_extra_state_attributes: Incomplete
    _attr_media_title: Incomplete
    _attr_media_series_title: Incomplete
    _attr_media_channel: Incomplete
    _attr_is_volume_muted: Incomplete
    _attr_media_content_id: Incomplete
    _attr_media_image_url: Incomplete
    _attr_source: Incomplete
    _attr_source_list: Incomplete
    _attr_state: Incomplete
    _attr_volume_level: Incomplete
    async def async_update(self) -> None: ...
