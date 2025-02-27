from .const import ATTR_BUTTON as ATTR_BUTTON, ATTR_PAYLOAD as ATTR_PAYLOAD, ATTR_SOUND_OUTPUT as ATTR_SOUND_OUTPUT, CONF_SOURCES as CONF_SOURCES, DOMAIN as DOMAIN, LIVE_TV_APP_ID as LIVE_TV_APP_ID, SERVICE_BUTTON as SERVICE_BUTTON, SERVICE_COMMAND as SERVICE_COMMAND, SERVICE_SELECT_SOUND_OUTPUT as SERVICE_SELECT_SOUND_OUTPUT, WEBOSTV_EXCEPTIONS as WEBOSTV_EXCEPTIONS
from .helpers import WebOsTvConfigEntry as WebOsTvConfigEntry, update_client_key as update_client_key
from .triggers.turn_on import async_get_turn_on_trigger as async_get_turn_on_trigger
from _typeshed import Incomplete
from aiowebostv import WebOsTvState as WebOsTvState
from collections.abc import Callable as Callable, Coroutine
from homeassistant import util as util
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType
from homeassistant.const import ATTR_COMMAND as ATTR_COMMAND, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.trigger import PluggableAction as PluggableAction
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any, Concatenate

_LOGGER: Incomplete
SUPPORT_WEBOSTV: Incomplete
SUPPORT_WEBOSTV_VOLUME: Incomplete
MIN_TIME_BETWEEN_SCANS: Incomplete
MIN_TIME_BETWEEN_FORCED_SCANS: Incomplete
PARALLEL_UPDATES: int
SCAN_INTERVAL: Incomplete
BUTTON_SCHEMA: VolDictType
COMMAND_SCHEMA: VolDictType
SOUND_OUTPUT_SCHEMA: VolDictType
SERVICES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: WebOsTvConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def cmd[_R, **_P](func: Callable[Concatenate[LgWebOSMediaPlayerEntity, _P], Coroutine[Any, Any, _R]]) -> Callable[Concatenate[LgWebOSMediaPlayerEntity, _P], Coroutine[Any, Any, _R]]: ...

class LgWebOSMediaPlayerEntity(RestoreEntity, MediaPlayerEntity):
    _attr_device_class: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _entry: Incomplete
    _client: Incomplete
    _attr_assumed_state: bool
    _device_name: Incomplete
    _attr_unique_id: Incomplete
    _sources: Incomplete
    _paused: bool
    _turn_on: Incomplete
    _current_source: Incomplete
    _source_list: dict
    _supported_features: Incomplete
    def __init__(self, entry: WebOsTvConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_handle_state_update(self, tv_state: WebOsTvState) -> None: ...
    _attr_state: Incomplete
    _attr_is_volume_muted: Incomplete
    _attr_volume_level: Incomplete
    _attr_source: Incomplete
    _attr_source_list: Incomplete
    _attr_media_content_type: Incomplete
    _attr_media_title: Incomplete
    _attr_media_image_url: Incomplete
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _update_states(self) -> None: ...
    def _update_sources(self) -> None: ...
    async def async_update(self) -> None: ...
    @property
    def supported_features(self) -> MediaPlayerEntityFeature: ...
    @cmd
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    @cmd
    async def async_volume_up(self) -> None: ...
    @cmd
    async def async_volume_down(self) -> None: ...
    @cmd
    async def async_set_volume_level(self, volume: float) -> None: ...
    @cmd
    async def async_mute_volume(self, mute: bool) -> None: ...
    @cmd
    async def async_select_sound_output(self, sound_output: str) -> ServiceResponse: ...
    @cmd
    async def async_media_play_pause(self) -> None: ...
    @cmd
    async def async_select_source(self, source: str) -> None: ...
    @cmd
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    @cmd
    async def async_media_play(self) -> None: ...
    @cmd
    async def async_media_pause(self) -> None: ...
    @cmd
    async def async_media_stop(self) -> None: ...
    @cmd
    async def async_media_next_track(self) -> None: ...
    @cmd
    async def async_media_previous_track(self) -> None: ...
    @cmd
    async def async_button(self, button: str) -> None: ...
    @cmd
    async def async_command(self, command: str, **kwargs: Any) -> ServiceResponse: ...
    async def _async_fetch_image(self, url: str) -> tuple[bytes | None, str | None]: ...
