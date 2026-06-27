import dataclasses
from .util import get_instance as get_instance
from enum import StrEnum
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

def is_entity_recorded(hass: HomeAssistant, entity_id: str) -> bool: ...
@callback
def async_setup(hass: HomeAssistant) -> None: ...

class EntityRecordingDisabler(StrEnum):
    USER = 'user'

@dataclasses.dataclass(frozen=True)
class RecorderEntityOptions:
    recording_disabled_by: EntityRecordingDisabler | None = ...
    def to_json(self) -> dict[str, Any]: ...

@websocket_api.require_admin
@callback
def ws_get_entity_options(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
