from .const import ANTHEMAV_UDATE_SIGNAL as ANTHEMAV_UDATE_SIGNAL, CONF_MODEL as CONF_MODEL, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from _typeshed import Incomplete
from anthemav.connection import Connection as Connection
from anthemav.protocol import AVR as AVR
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

_LOGGER: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AnthemAVR(MediaPlayerEntity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_device_class: Incomplete
    _attr_icon: str
    _attr_supported_features: Incomplete
    avr: Incomplete
    _entry_id: Incomplete
    _zone_number: Incomplete
    _zone: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, avr: AVR, name: str, mac_address: str, model: str, zone_number: int, entry_id: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def update_states(self) -> None: ...
    _attr_state: Incomplete
    _attr_is_volume_muted: Incomplete
    _attr_volume_level: Incomplete
    _attr_media_title: Incomplete
    _attr_app_name: Incomplete
    _attr_source: Incomplete
    _attr_source_list: Incomplete
    def set_states(self) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
