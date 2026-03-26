from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from spotifyaio import Device, PlaybackState as PlaybackState, Playlist as Playlist, SpotifyClient as SpotifyClient, UserProfile as UserProfile

_LOGGER: Incomplete
type SpotifyConfigEntry = ConfigEntry[SpotifyData]

@dataclass
class SpotifyData:
    coordinator: SpotifyCoordinator
    session: OAuth2Session
    devices: SpotifyDeviceCoordinator

UPDATE_INTERVAL: Incomplete
FREE_API_BLOGPOST: str

@dataclass
class SpotifyCoordinatorData:
    current_playback: PlaybackState | None
    position_updated_at: datetime | None
    playlist: Playlist | None
    dj_playlist: bool = ...

SPOTIFY_DJ_PLAYLIST_URI: str

class SpotifyCoordinator(DataUpdateCoordinator[SpotifyCoordinatorData]):
    current_user: UserProfile
    config_entry: SpotifyConfigEntry
    client: Incomplete
    _playlist: Playlist | None
    _checked_playlist_id: str | None
    def __init__(self, hass: HomeAssistant, config_entry: SpotifyConfigEntry, client: SpotifyClient) -> None: ...
    async def _async_setup(self) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> SpotifyCoordinatorData: ...

class SpotifyDeviceCoordinator(DataUpdateCoordinator[list[Device]]):
    config_entry: SpotifyConfigEntry
    _client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: SpotifyConfigEntry, client: SpotifyClient) -> None: ...
    async def _async_update_data(self) -> list[Device]: ...
