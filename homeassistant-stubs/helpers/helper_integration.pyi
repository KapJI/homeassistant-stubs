from .event import async_track_entity_registry_updated_event as async_track_entity_registry_updated_event
from collections.abc import Callable as Callable
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, valid_entity_id as valid_entity_id

def async_handle_source_entity_changes(hass: HomeAssistant, *, helper_config_entry_id: str, get_helper_entity_id: Callable[[], str | None], set_source_entity_id_or_uuid: Callable[[str], None], source_device_id: str | None, source_entity_id_or_uuid: str) -> CALLBACK_TYPE: ...
