from . import MusicAssistantConfigEntry as MusicAssistantConfigEntry
from .const import DOMAIN as DOMAIN
from collections.abc import Callable as Callable, Coroutine, Generator
from contextlib import contextmanager
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from music_assistant_client import MusicAssistantClient as MusicAssistantClient
from typing import Any

def catch_musicassistant_error[**_P, _R](func: Callable[_P, Coroutine[Any, Any, _R]]) -> Callable[_P, Coroutine[Any, Any, _R]]: ...
@contextmanager
def catch_user_not_found(username: str | None) -> Generator[None]: ...
@callback
def get_music_assistant_client(hass: HomeAssistant, config_entry_id: str) -> MusicAssistantClient: ...
