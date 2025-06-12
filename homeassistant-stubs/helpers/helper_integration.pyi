from .event import async_track_entity_registry_updated_event as async_track_entity_registry_updated_event
from collections.abc import Callable as Callable, Coroutine
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, valid_entity_id as valid_entity_id
from typing import Any

def async_handle_source_entity_changes(hass: HomeAssistant, *, helper_config_entry_id: str, set_source_entity_id_or_uuid: Callable[[str], None], source_device_id: str | None, source_entity_id_or_uuid: str, source_entity_removed: Callable[[], Coroutine[Any, Any, None]]) -> CALLBACK_TYPE: ...
