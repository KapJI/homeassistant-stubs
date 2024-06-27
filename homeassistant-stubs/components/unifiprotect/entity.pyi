from .const import ATTR_EVENT_ID as ATTR_EVENT_ID, ATTR_EVENT_SCORE as ATTR_EVENT_SCORE, DEFAULT_ATTRIBUTION as DEFAULT_ATTRIBUTION, DEFAULT_BRAND as DEFAULT_BRAND, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .models import PermRequired as PermRequired, ProtectEntityDescription as ProtectEntityDescription, ProtectEventMixin as ProtectEventMixin
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Sequence
from datetime import datetime
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from uiprotect.data import Event as Event, ModelType, NVR as NVR, ProtectAdoptableDeviceModel, ProtectModelWithId as ProtectModelWithId

_LOGGER: Incomplete

def _async_device_entities(data: ProtectData, klass: type[BaseProtectEntity], model_type: ModelType, descs: Sequence[ProtectEntityDescription], unadopted_descs: Sequence[ProtectEntityDescription] | None = None, ufp_device: ProtectAdoptableDeviceModel | None = None) -> list[BaseProtectEntity]: ...

_ALL_MODEL_TYPES: Incomplete

def _combine_model_descs(model_type: ModelType, model_descriptions: dict[ModelType, Sequence[ProtectEntityDescription]] | None, all_descs: Sequence[ProtectEntityDescription] | None) -> list[ProtectEntityDescription]: ...
def async_all_device_entities(data: ProtectData, klass: type[BaseProtectEntity], model_descriptions: dict[ModelType, Sequence[ProtectEntityDescription]] | None = None, all_descs: Sequence[ProtectEntityDescription] | None = None, unadopted_descs: list[ProtectEntityDescription] | None = None, ufp_device: ProtectAdoptableDeviceModel | None = None) -> list[BaseProtectEntity]: ...

class BaseProtectEntity(Entity):
    device: ProtectAdoptableDeviceModel | NVR
    _attr_should_poll: bool
    _attr_attribution = DEFAULT_ATTRIBUTION
    _state_attrs: tuple[str, ...]
    _attr_has_entity_name: bool
    _async_get_ufp_enabled: Callable[[ProtectAdoptableDeviceModel], bool] | None
    data: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    entity_description: Incomplete
    _state_getters: Incomplete
    def __init__(self, data: ProtectData, device: ProtectAdoptableDeviceModel | NVR, description: EntityDescription | None = None) -> None: ...
    async def async_update(self) -> None: ...
    _attr_device_info: Incomplete
    def _async_set_device_info(self) -> None: ...
    _attr_available: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...
    def _async_updated_event(self, device: ProtectAdoptableDeviceModel | NVR) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class ProtectDeviceEntity(BaseProtectEntity):
    device: ProtectAdoptableDeviceModel

class ProtectNVREntity(BaseProtectEntity):
    device: NVR
    _attr_device_info: Incomplete
    def _async_set_device_info(self) -> None: ...
    _attr_available: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...

class EventEntityMixin(ProtectDeviceEntity):
    entity_description: ProtectEventMixin
    _unrecorded_attributes: Incomplete
    _event: Event | None
    _event_end: datetime | None
    def _set_event_done(self) -> None: ...
    _attr_extra_state_attributes: Incomplete
    def _set_event_attrs(self, event: Event) -> None: ...
    def _async_event_with_immediate_end(self) -> None: ...
    def _event_already_ended(self, prev_event: Event | None, prev_event_end: datetime | None) -> bool: ...
