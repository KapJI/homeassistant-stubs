import dataclasses
from .const import ATTR_EVENT_ID as ATTR_EVENT_ID, EVENT_TYPE_DOORBELL_RING as EVENT_TYPE_DOORBELL_RING, EVENT_TYPE_FINGERPRINT_IDENTIFIED as EVENT_TYPE_FINGERPRINT_IDENTIFIED, EVENT_TYPE_FINGERPRINT_NOT_IDENTIFIED as EVENT_TYPE_FINGERPRINT_NOT_IDENTIFIED, EVENT_TYPE_NFC_SCANNED as EVENT_TYPE_NFC_SCANNED
from .data import ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import EventEntityMixin as EventEntityMixin, ProtectDeviceEntity as ProtectDeviceEntity, ProtectEventMixin as ProtectEventMixin
from _typeshed import Incomplete
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from uiprotect.data import ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel

@dataclasses.dataclass(frozen=True, kw_only=True)
class ProtectEventEntityDescription(ProtectEventMixin, EventEntityDescription):
    entity_class: type[ProtectDeviceEntity]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., event_types=..., ufp_required_field=..., ufp_value=..., ufp_value_fn=..., ufp_enabled=..., ufp_perm=..., has_required=..., get_ufp_enabled=..., ufp_event_obj=..., ufp_obj_type=..., entity_class) -> None: ...

class ProtectDeviceRingEventEntity(EventEntityMixin, ProtectDeviceEntity, EventEntity):
    entity_description: ProtectEventEntityDescription
    _event: Incomplete
    _event_end: Incomplete
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

class ProtectDeviceNFCEventEntity(EventEntityMixin, ProtectDeviceEntity, EventEntity):
    entity_description: ProtectEventEntityDescription
    _event: Incomplete
    _event_end: Incomplete
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

class ProtectDeviceFingerprintEventEntity(EventEntityMixin, ProtectDeviceEntity, EventEntity):
    entity_description: ProtectEventEntityDescription
    _event: Incomplete
    _event_end: Incomplete
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

EVENT_DESCRIPTIONS: tuple[ProtectEventEntityDescription, ...]

def _async_event_entities(data: ProtectData, ufp_device: ProtectAdoptableDeviceModel | None = None) -> list[ProtectDeviceEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
