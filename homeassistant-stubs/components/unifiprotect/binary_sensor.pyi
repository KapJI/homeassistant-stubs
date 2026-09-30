import dataclasses
from .const import DEFAULT_ATTRIBUTION as DEFAULT_ATTRIBUTION, DEFAULT_BRAND as DEFAULT_BRAND, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import BaseProtectEntity as BaseProtectEntity, EventEntityMixin as EventEntityMixin, PermRequired as PermRequired, ProtectDeviceEntity as ProtectDeviceEntity, ProtectEntityDescription as ProtectEntityDescription, ProtectEventMixin as ProtectEventMixin, ProtectFobEntity as ProtectFobEntity, ProtectIsOnEntity as ProtectIsOnEntity, ProtectNVREntity as ProtectNVREntity, async_all_device_entities as async_all_device_entities, async_remove_unsupported_sense_entities as async_remove_unsupported_sense_entities
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Sequence
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, async_get_current_platform as async_get_current_platform
from typing import override
from uiprotect.data import Fob, ModelType, NVR as NVR, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, PublicRelayInput as PublicRelayInput, Relay as Relay, RelayInputState, Sensor as Sensor
from uiprotect.data.nvr import UOSDisk as UOSDisk
from uiprotect.data.public_devices import PublicDeviceModel as PublicDeviceModel, PublicSensor

_KEY_DOOR: str
PARALLEL_UPDATES: int
_RELAY_INPUT_STATE_MAP: dict[RelayInputState, bool]

@dataclasses.dataclass(frozen=True, kw_only=True)
class ProtectBinaryEntityDescription(ProtectEntityDescription, BinarySensorEntityDescription): ...
@dataclasses.dataclass(frozen=True, kw_only=True)
class ProtectBinaryEventEntityDescription(ProtectEventMixin, BinarySensorEntityDescription): ...

MOUNT_DEVICE_CLASS_MAP: Incomplete
CAMERA_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
LIGHT_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
MOUNTABLE_SENSE_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
SENSE_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
EVENT_SENSORS: tuple[ProtectBinaryEventEntityDescription, ...]
VIEWER_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
DISK_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
_MODEL_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]
_MOUNTABLE_MODEL_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]

class ProtectDeviceBinarySensor(ProtectIsOnEntity, ProtectDeviceEntity, BinarySensorEntity):
    entity_description: ProtectBinaryEntityDescription

class MountableProtectDeviceBinarySensor(ProtectDeviceBinarySensor):
    device: Sensor | PublicSensor
    _state_attrs: Incomplete
    _attr_device_class: Incomplete
    @callback
    @override
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

class ProtectDiskBinarySensor(ProtectNVREntity, BinarySensorEntity):
    _disk: UOSDisk
    entity_description: ProtectBinaryEntityDescription
    _state_attrs: Incomplete
    def __init__(self, data: ProtectData, device: NVR, description: ProtectBinaryEntityDescription, disk: UOSDisk) -> None: ...
    _attr_available: bool
    _attr_is_on: Incomplete
    @callback
    @override
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

class ProtectEventBinarySensor(EventEntityMixin, BinarySensorEntity):
    entity_description: ProtectBinaryEventEntityDescription
    _state_attrs: Incomplete
    _attr_is_on: bool
    _attr_extra_state_attributes: Incomplete
    @callback
    @override
    def _set_event_done(self) -> None: ...
    _event: Incomplete
    _event_end: Incomplete
    @callback
    @override
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

class ProtectRelayInputBinarySensor(BinarySensorEntity):
    _attr_has_entity_name: bool
    _attr_attribution = DEFAULT_ATTRIBUTION
    _attr_should_poll: bool
    _attr_translation_key: str
    data: Incomplete
    _relay_id: Incomplete
    _relay_mac: Incomplete
    _input_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data: ProtectData, relay: Relay, relay_input: PublicRelayInput) -> None: ...
    @property
    def _relay(self) -> Relay | None: ...
    _attr_available: bool
    _attr_is_on: Incomplete
    @callback
    def _update_from_relay(self, relay: Relay) -> None: ...
    @callback
    def _async_updated(self, _obj: PublicDeviceModel | None) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...

MODEL_DESCRIPTIONS_WITH_CLASS: Incomplete

@callback
def _async_model_entities(data: ProtectData, *, ufp_device: ProtectAdoptableDeviceModel | None = None, public_device: PublicDeviceModel | None = None) -> list[BaseProtectEntity]: ...
@callback
def _async_event_entities(data: ProtectData, ufp_device: ProtectAdoptableDeviceModel | None = None) -> list[ProtectDeviceEntity]: ...
@callback
def _async_nvr_entities(data: ProtectData) -> list[BaseProtectEntity]: ...
def _fob_battery_low(fob: Fob) -> bool | None: ...

@dataclasses.dataclass(frozen=True, kw_only=True)
class ProtectFobBinaryEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[Fob], bool | None]

FOB_BINARY_SENSORS: tuple[ProtectFobBinaryEntityDescription, ...]

class ProtectFobBinarySensor(ProtectFobEntity, BinarySensorEntity):
    entity_description: ProtectFobBinaryEntityDescription
    _fob_state_attrs: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, data: ProtectData, fob: Fob, description: ProtectFobBinaryEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    @callback
    @override
    def _async_update_from_fob(self, fob: Fob) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
