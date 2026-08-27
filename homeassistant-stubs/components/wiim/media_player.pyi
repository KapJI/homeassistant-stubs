from .const import DATA_WIIM as DATA_WIIM, DOMAIN as DOMAIN, LOGGER as LOGGER, WiimConfigEntry as WiimConfigEntry
from .entity import WiimBaseEntity as WiimBaseEntity
from .models import WiimData as WiimData
from _typeshed import Incomplete
from async_upnp_client.client import UpnpService as UpnpService, UpnpStateVariable as UpnpStateVariable
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseError as BrowseError, BrowseMedia as BrowseMedia, MediaClass as MediaClass, MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, RepeatMode as RepeatMode, async_process_play_media_url as async_process_play_media_url
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow
from typing import Any, Concatenate, override
from wiim.consts import PlayingStatus as SDKPlayingStatus
from wiim.exceptions import WiimException
from wiim.models import WiimGroupSnapshot as WiimGroupSnapshot, WiimTransportCapabilities as WiimTransportCapabilities
from wiim.wiim_device import WiimDevice as WiimDevice

MEDIA_TYPE_WIIM_LIBRARY: str
MEDIA_CONTENT_ID_ROOT: str
MEDIA_CONTENT_ID_FAVORITES: Incomplete
MEDIA_CONTENT_ID_PLAYLISTS: Incomplete
PARALLEL_UPDATES: int
MEDIA_IMAGE_FETCH_TIMEOUT: Incomplete
SDK_TO_HA_STATE: dict[SDKPlayingStatus, MediaPlayerState]
SUPPORT_WIIM_BASE: Incomplete

def _group_member_state_signal(member_udn: str) -> str: ...
def media_player_exception_wrap[_WiimMediaPlayerEntityT: WiimMediaPlayerEntity, **_P, _R](func: Callable[Concatenate[_WiimMediaPlayerEntityT, _P], Awaitable[_R]], *, update_ha_state: bool = True) -> Callable[Concatenate[_WiimMediaPlayerEntityT, _P], Coroutine[Any, Any, _R]]: ...
def browse_media_exception_wrap[_WiimMediaPlayerEntityT: WiimMediaPlayerEntity, **_P, _R](func: Callable[Concatenate[_WiimMediaPlayerEntityT, _P], Awaitable[_R]]) -> Callable[Concatenate[_WiimMediaPlayerEntityT, _P], Coroutine[Any, Any, _R]]: ...
async def async_setup_entry(hass: HomeAssistant, entry: WiimConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class WiimMediaPlayerEntity(WiimBaseEntity, MediaPlayerEntity):
    _attr_device_class: Incomplete
    _attr_media_image_remotely_accessible: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _entry: Incomplete
    _attr_unique_id: Incomplete
    _attr_source_list: Incomplete
    _attr_shuffle: bool
    _attr_repeat: Incomplete
    _transport_capabilities: WiimTransportCapabilities | None
    _supported_features_update_in_flight: bool
    def __init__(self, device: WiimDevice, entry: WiimConfigEntry) -> None: ...
    @property
    def _wiim_data(self) -> WiimData: ...
    @property
    @override
    def supported_features(self) -> MediaPlayerEntityFeature: ...
    @callback
    def _get_entity_id_for_udn(self, udn: str) -> str | None: ...
    def _get_group_snapshot(self) -> WiimGroupSnapshot: ...
    @property
    def _metadata_device(self) -> WiimDevice: ...
    _attr_media_title: Incomplete
    _attr_media_artist: Incomplete
    _attr_media_album_name: Incomplete
    _attr_media_image_url: Incomplete
    _attr_media_image_hash: Incomplete
    _attr_media_content_id: Incomplete
    _attr_media_content_type: Incomplete
    _attr_media_duration: Incomplete
    _attr_media_position: Incomplete
    _attr_media_position_updated_at: Incomplete
    @callback
    def _clear_media_metadata(self) -> None: ...
    @callback
    def _set_media_image_hash(self, *, image_url: str | None, media_uri: str | None, title: str | None, artist: str | None, album: str | None) -> None: ...
    @override
    async def async_get_media_image(self) -> tuple[bytes | None, str | None]: ...
    @override
    async def _async_fetch_image(self, url: str) -> tuple[bytes | None, str | None]: ...
    @callback
    def _get_command_target_device(self, action_name: str) -> WiimDevice: ...
    @callback
    def _async_handle_group_member_state_refresh(self) -> None: ...
    @callback
    def _async_propagate_group_state_update(self, group_snapshot: WiimGroupSnapshot) -> None: ...
    _attr_available: Incomplete
    _attr_state: Incomplete
    _attr_source: Incomplete
    _attr_volume_level: Incomplete
    _attr_is_volume_muted: Incomplete
    _attr_group_members: Incomplete
    @callback
    def _update_ha_state_from_sdk_cache(self, *, write_state: bool = True, update_supported_features: bool = True) -> None: ...
    @callback
    def _handle_sdk_general_device_update(self, device: WiimDevice) -> None: ...
    @callback
    def _handle_sdk_av_transport_event(self, service: UpnpService, state_variables: list[UpnpStateVariable]) -> None: ...
    @callback
    def _handle_sdk_refresh_event(self, _service: UpnpService, state_variables: list[UpnpStateVariable]) -> None: ...
    async def _async_get_transport_capabilities_for_device(self, device: WiimDevice) -> WiimTransportCapabilities | None: ...
    async def _from_device_update_supported_features(self, *, write_state: bool = True) -> None: ...
    @callback
    def _async_schedule_update_supported_features(self) -> None: ...
    @callback
    @override
    def _async_registry_updated(self, event: Event[er.EventEntityRegistryUpdatedData]) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_will_remove_from_hass(self) -> None: ...
    async def _async_handle_critical_error(self, error: WiimException) -> None: ...
    @media_player_exception_wrap
    @override
    async def async_set_volume_level(self, volume: float) -> None: ...
    @media_player_exception_wrap
    @override
    async def async_mute_volume(self, mute: bool) -> None: ...
    @media_player_exception_wrap
    @override
    async def async_media_play(self) -> None: ...
    @media_player_exception_wrap
    @override
    async def async_media_pause(self) -> None: ...
    @media_player_exception_wrap
    @override
    async def async_media_stop(self) -> None: ...
    @media_player_exception_wrap
    @override
    async def async_media_next_track(self) -> None: ...
    @media_player_exception_wrap
    @override
    async def async_media_previous_track(self) -> None: ...
    @media_player_exception_wrap
    @override
    async def async_media_seek(self, position: float) -> None: ...
    @media_player_exception_wrap
    @override
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    async def _async_play_url(self, target_device: WiimDevice, media_id: str) -> None: ...
    @media_player_exception_wrap
    @override
    async def async_set_repeat(self, repeat: RepeatMode) -> None: ...
    @media_player_exception_wrap
    @override
    async def async_set_shuffle(self, shuffle: bool) -> None: ...
    @media_player_exception_wrap
    @override
    async def async_select_source(self, source: str) -> None: ...
    @browse_media_exception_wrap
    @override
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
    @media_player_exception_wrap
    @override
    async def async_join_players(self, group_members: list[str]) -> None: ...
    @media_player_exception_wrap
    @override
    async def async_unjoin_player(self) -> None: ...
