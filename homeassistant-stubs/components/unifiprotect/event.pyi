import dataclasses
from . import Bootstrap as Bootstrap
from .const import ATTR_EVENT_ID as ATTR_EVENT_ID, EVENT_TYPE_DOORBELL_RING as EVENT_TYPE_DOORBELL_RING, EVENT_TYPE_FINGERPRINT_IDENTIFIED as EVENT_TYPE_FINGERPRINT_IDENTIFIED, EVENT_TYPE_FINGERPRINT_NOT_IDENTIFIED as EVENT_TYPE_FINGERPRINT_NOT_IDENTIFIED, EVENT_TYPE_NFC_SCANNED as EVENT_TYPE_NFC_SCANNED, EVENT_TYPE_VEHICLE_DETECTED as EVENT_TYPE_VEHICLE_DETECTED, KEYRINGS_KEY_TYPE_ID_NFC as KEYRINGS_KEY_TYPE_ID_NFC, KEYRINGS_ULP_ID as KEYRINGS_ULP_ID, KEYRINGS_USER_FULL_NAME as KEYRINGS_USER_FULL_NAME, KEYRINGS_USER_STATUS as KEYRINGS_USER_STATUS, VEHICLE_EVENT_DELAY_SECONDS as VEHICLE_EVENT_DELAY_SECONDS
from .data import Camera as Camera, EventType as EventType, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import EventEntityMixin as EventEntityMixin, ProtectDeviceEntity as ProtectDeviceEntity, ProtectEventMixin as ProtectEventMixin
from _typeshed import Incomplete
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.event import async_call_at as async_call_at
from typing import Any
from uiprotect.data.nvr import Event as Event, EventDetectedThumbnail as EventDetectedThumbnail

PARALLEL_UPDATES: int

def _thumbnail_sort_key(t: EventDetectedThumbnail) -> tuple[bool, float, float]: ...
def _add_ulp_user_infos(bootstrap: Bootstrap, event_data: dict[str, str], ulp_id: str) -> None: ...

@dataclasses.dataclass(frozen=True, kw_only=True)
class ProtectEventEntityDescription(ProtectEventMixin, EventEntityDescription):
    entity_class: type[ProtectDeviceEntity]

class ProtectDeviceRingEventEntity(EventEntityMixin, ProtectDeviceEntity, EventEntity):
    entity_description: ProtectEventEntityDescription
    _event: Incomplete
    _event_end: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

class ProtectDeviceNFCEventEntity(EventEntityMixin, ProtectDeviceEntity, EventEntity):
    entity_description: ProtectEventEntityDescription
    _event: Incomplete
    _event_end: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

class ProtectDeviceFingerprintEventEntity(EventEntityMixin, ProtectDeviceEntity, EventEntity):
    entity_description: ProtectEventEntityDescription
    _event: Incomplete
    _event_end: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

class ProtectDeviceVehicleEventEntity(EventEntityMixin, ProtectDeviceEntity, EventEntity):
    entity_description: ProtectEventEntityDescription
    _thumbnail_timer_cancel: CALLBACK_TYPE | None
    _latest_event_id: str | None
    _latest_thumbnails: list[EventDetectedThumbnail] | None
    _thumbnail_timer_due: float
    _fired_event_id: str | None
    _fired_event_data: dict[str, Any] | None
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _cancel_thumbnail_timer(self) -> None: ...
    @callback
    def _async_timer_callback(self, *_: Any) -> None: ...
    @staticmethod
    def _get_vehicle_thumbnails(event: Event) -> list[EventDetectedThumbnail]: ...
    @staticmethod
    def _build_event_data(event_id: str, thumbnails: list[EventDetectedThumbnail]) -> dict[str, Any]: ...
    @callback
    def _fire_vehicle_event(self, event_id: str, thumbnails: list[EventDetectedThumbnail] | None = None) -> None: ...
    @callback
    def _async_set_thumbnail_timer(self) -> None: ...
    _event: Incomplete
    _event_end: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

EVENT_DESCRIPTIONS: tuple[ProtectEventEntityDescription, ...]

@callback
def _async_event_entities(data: ProtectData, ufp_device: ProtectAdoptableDeviceModel | None = None) -> list[ProtectDeviceEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
