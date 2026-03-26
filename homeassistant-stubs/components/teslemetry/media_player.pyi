from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .entity import TeslemetryRootEntity as TeslemetryRootEntity, TeslemetryVehiclePollingEntity as TeslemetryVehiclePollingEntity, TeslemetryVehicleStreamEntity as TeslemetryVehicleStreamEntity
from .helpers import handle_vehicle_command as handle_vehicle_command
from .models import TeslemetryVehicleData as TeslemetryVehicleData
from _typeshed import Incomplete
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from tesla_fleet_api.const import Scope
from tesla_fleet_api.teslemetry import Vehicle as Vehicle

STATES: Incomplete
DISPLAY_STATES: Incomplete
VOLUME_STEP: Incomplete
VOLUME_FACTOR: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: TeslemetryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TeslemetryMediaEntity(TeslemetryRootEntity, MediaPlayerEntity):
    api: Vehicle
    _attr_device_class: Incomplete
    _attr_volume_step = VOLUME_STEP
    _attr_volume_level: Incomplete
    async def async_set_volume_level(self, volume: float) -> None: ...
    _attr_state: Incomplete
    async def async_media_play(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...

class TeslemetryVehiclePollingMediaEntity(TeslemetryVehiclePollingEntity, TeslemetryMediaEntity):
    _attr_supported_features: Incomplete
    scoped: Incomplete
    def __init__(self, data: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    _attr_state: Incomplete
    _attr_volume_level: Incomplete
    _attr_media_duration: Incomplete
    _attr_media_position: Incomplete
    _attr_media_title: Incomplete
    _attr_media_artist: Incomplete
    _attr_media_album_name: Incomplete
    _attr_media_playlist: Incomplete
    _attr_source: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingMediaEntity(TeslemetryVehicleStreamEntity, TeslemetryMediaEntity, RestoreEntity):
    _attr_supported_features: Incomplete
    scoped: Incomplete
    def __init__(self, data: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    _attr_state: Incomplete
    _attr_volume_level: Incomplete
    _attr_media_title: Incomplete
    _attr_media_artist: Incomplete
    _attr_media_album_name: Incomplete
    _attr_media_playlist: Incomplete
    _attr_media_duration: Incomplete
    _attr_media_position: Incomplete
    _attr_source: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _async_handle_center_display(self, value: str | None) -> None: ...
    def _async_handle_media_playback_status(self, value: str | None) -> None: ...
    def _async_handle_media_playback_source(self, value: str | None) -> None: ...
    def _async_handle_media_audio_volume(self, value: float | None) -> None: ...
    def _async_handle_media_now_playing_duration(self, value: int | None) -> None: ...
    def _async_handle_media_now_playing_elapsed(self, value: int | None) -> None: ...
    def _async_handle_media_now_playing_artist(self, value: str | None) -> None: ...
    def _async_handle_media_now_playing_album(self, value: str | None) -> None: ...
    def _async_handle_media_now_playing_title(self, value: str | None) -> None: ...
    _attr_media_channel: Incomplete
    def _async_handle_media_now_playing_station(self, value: str | None) -> None: ...
