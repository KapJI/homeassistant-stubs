from .const import CONF_NICKNAME as CONF_NICKNAME, CONF_USE_PSK as CONF_USE_PSK, DOMAIN as DOMAIN, LEGACY_CLIENT_ID as LEGACY_CLIENT_ID, NICKNAME_PREFIX as NICKNAME_PREFIX, SourceType as SourceType
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine, Iterable
from datetime import datetime
from homeassistant.components.media_player import MediaType as MediaType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_PIN as CONF_PIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pybravia import BraviaClient as BraviaClient
from typing import Any, Concatenate, Final

_LOGGER: Incomplete
SCAN_INTERVAL: Final[Incomplete]
type BraviaTVConfigEntry = ConfigEntry[BraviaTVCoordinator]

def catch_braviatv_errors[_BraviaTVCoordinatorT: BraviaTVCoordinator, **_P](func: Callable[Concatenate[_BraviaTVCoordinatorT, _P], Awaitable[None]]) -> Callable[Concatenate[_BraviaTVCoordinatorT, _P], Coroutine[Any, Any, None]]: ...

class BraviaTVCoordinator(DataUpdateCoordinator[None]):
    config_entry: BraviaTVConfigEntry
    client: Incomplete
    pin: Incomplete
    use_psk: Incomplete
    client_id: Incomplete
    nickname: Incomplete
    source: str | None
    source_list: list[str]
    source_map: dict[str, dict]
    media_title: str | None
    media_channel: str | None
    media_content_id: str | None
    media_content_type: MediaType | None
    media_uri: str | None
    media_duration: int | None
    media_position: int | None
    media_position_updated_at: datetime | None
    volume_level: float | None
    volume_target: str | None
    volume_muted: bool
    is_on: bool
    connected: bool
    skipped_updates: int
    def __init__(self, hass: HomeAssistant, config_entry: BraviaTVConfigEntry, client: BraviaClient) -> None: ...
    def _sources_extend(self, sources: list[dict], source_type: SourceType, add_to_list: bool = False, sort_by: str | None = None) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def async_update_volume(self) -> None: ...
    async def async_update_playing(self) -> None: ...
    async def async_update_sources(self) -> None: ...
    async def async_source_start(self, uri: str, source_type: SourceType | str) -> None: ...
    async def async_source_find(self, query: str, source_type: SourceType | str) -> None: ...
    @catch_braviatv_errors
    async def async_turn_on(self) -> None: ...
    @catch_braviatv_errors
    async def async_turn_off(self) -> None: ...
    @catch_braviatv_errors
    async def async_set_volume_level(self, volume: float) -> None: ...
    @catch_braviatv_errors
    async def async_volume_up(self) -> None: ...
    @catch_braviatv_errors
    async def async_volume_down(self) -> None: ...
    @catch_braviatv_errors
    async def async_volume_mute(self, mute: bool) -> None: ...
    @catch_braviatv_errors
    async def async_media_play(self) -> None: ...
    @catch_braviatv_errors
    async def async_media_pause(self) -> None: ...
    @catch_braviatv_errors
    async def async_media_stop(self) -> None: ...
    @catch_braviatv_errors
    async def async_media_next_track(self) -> None: ...
    @catch_braviatv_errors
    async def async_media_previous_track(self) -> None: ...
    @catch_braviatv_errors
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    @catch_braviatv_errors
    async def async_select_source(self, source: str) -> None: ...
    @catch_braviatv_errors
    async def async_send_command(self, command: Iterable[str], repeats: int) -> None: ...
    @catch_braviatv_errors
    async def async_reboot_device(self) -> None: ...
    @catch_braviatv_errors
    async def async_terminate_apps(self) -> None: ...
