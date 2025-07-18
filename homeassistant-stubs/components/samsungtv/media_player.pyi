import asyncio
from .bridge import SamsungTVWSBridge as SamsungTVWSBridge
from .const import CONF_SSDP_RENDERING_CONTROL_LOCATION as CONF_SSDP_RENDERING_CONTROL_LOCATION, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import SamsungTVConfigEntry as SamsungTVConfigEntry, SamsungTVDataUpdateCoordinator as SamsungTVDataUpdateCoordinator
from .entity import SamsungTVEntity as SamsungTVEntity
from _typeshed import Incomplete
from async_upnp_client.aiohttp import AiohttpNotifyServer
from async_upnp_client.client import UpnpDevice as UpnpDevice, UpnpService as UpnpService, UpnpStateVariable as UpnpStateVariable
from async_upnp_client.profiles.dlna import DmrDevice
from collections.abc import Sequence
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.async_ import create_eager_task as create_eager_task
from typing import Any

SOURCES: Incomplete
SUPPORT_SAMSUNGTV: Incomplete
APP_LIST_DELAY: int
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: SamsungTVConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SamsungTVDevice(SamsungTVEntity, MediaPlayerEntity):
    _attr_source_list: list[str]
    _attr_name: Incomplete
    _attr_device_class: Incomplete
    _ssdp_rendering_control_location: str | None
    _playing: bool
    _attr_is_volume_muted: bool
    _app_list: dict[str, str] | None
    _app_list_event: asyncio.Event
    _attr_supported_features: Incomplete
    _dmr_device: DmrDevice | None
    _upnp_server: AiohttpNotifyServer | None
    def __init__(self, coordinator: SamsungTVDataUpdateCoordinator) -> None: ...
    @property
    def supported_features(self) -> MediaPlayerEntityFeature: ...
    def _update_sources(self) -> None: ...
    def _app_list_callback(self, app_list: dict[str, str]) -> None: ...
    _attr_state: Incomplete
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def _async_extra_update(self) -> None: ...
    _attr_volume_level: Incomplete
    @callback
    def _update_from_upnp(self) -> bool: ...
    async def _async_startup_app_list(self) -> None: ...
    async def _async_startup_dmr(self) -> None: ...
    async def _async_resubscribe_dmr(self) -> None: ...
    async def _async_shutdown_dmr(self) -> None: ...
    def _on_upnp_event(self, service: UpnpService, state_variables: Sequence[UpnpStateVariable]) -> None: ...
    async def _async_launch_app(self, app_id: str) -> None: ...
    async def _async_send_keys(self, keys: list[str]) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_media_play_pause(self) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
