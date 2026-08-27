from . import SimpliSafe as SimpliSafe, SimpliSafeConfigEntry as SimpliSafeConfigEntry, WEBSOCKET_EVENTS_TO_FIRE_HASS_EVENT as WEBSOCKET_EVENTS_TO_FIRE_HASS_EVENT
from .entity import SimpliSafeEntity as SimpliSafeEntity
from .typing import SystemType as SystemType
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.event import DoorbellEventType as DoorbellEventType, EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from simplipy.device import Device as Device
from simplipy.device.camera import CameraTypes
from simplipy.websocket import WebsocketEvent as WebsocketEvent
from typing import override

SYSTEM_EVENT_TYPES: Incomplete

@dataclass(frozen=True, kw_only=True)
class SimpliSafeCameraEventDescription(EventEntityDescription):
    raw_event_type: str

CAMERA_EVENT_DESCRIPTIONS: dict[CameraTypes, list[SimpliSafeCameraEventDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: SimpliSafeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SimpliSafeEvent(SimpliSafeEntity, EventEntity):
    entity_description: Incomplete
    _attr_translation_key: Incomplete
    _ws_serial: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, simplisafe: SimpliSafe, system: SystemType, *, entity_description: EventEntityDescription, device: Device | None = None, ws_serial: str | None = None, unique_id: str) -> None: ...
    @callback
    @override
    def _handle_websocket_update(self, event: WebsocketEvent) -> None: ...
    @callback
    @override
    def async_update_from_websocket_event(self, event: WebsocketEvent) -> None: ...
