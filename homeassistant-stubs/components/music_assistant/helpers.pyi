from . import MusicAssistantConfigEntry as MusicAssistantConfigEntry
from collections.abc import Callable as Callable, Coroutine
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from music_assistant_client import MusicAssistantClient as MusicAssistantClient
from typing import Any

def catch_musicassistant_error[**_P, _R](func: Callable[_P, Coroutine[Any, Any, _R]]) -> Callable[_P, Coroutine[Any, Any, _R]]: ...
@callback
def get_music_assistant_client(hass: HomeAssistant, config_entry_id: str) -> MusicAssistantClient: ...
