from .const import DISPATCH_ADOPT as DISPATCH_ADOPT, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity, ProtectNVREntity as ProtectNVREntity, async_all_device_entities as async_all_device_entities
from .models import PermRequired as PermRequired, ProtectSetableKeysMixin as ProtectSetableKeysMixin, T as T
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from pyunifiprotect.data import Camera, NVR as NVR, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, ProtectModelWithId as ProtectModelWithId
from typing import Any

ATTR_PREV_MIC: str
ATTR_PREV_RECORD: str

class ProtectSwitchEntityDescription(ProtectSetableKeysMixin[T], SwitchEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_perm, ufp_set_method, ufp_set_method_fn) -> None: ...

async def _set_highfps(obj: Camera, value: bool) -> None: ...

CAMERA_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
PRIVACY_MODE_SWITCH: Incomplete
SENSE_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
LIGHT_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
DOORLOCK_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
VIEWER_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
NVR_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectSwitch(ProtectDeviceEntity, SwitchEntity):
    entity_description: ProtectSwitchEntityDescription
    _attr_name: Incomplete
    _switch_type: Incomplete
    def __init__(self, data: ProtectData, device: ProtectAdoptableDeviceModel, description: ProtectSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class ProtectNVRSwitch(ProtectNVREntity, SwitchEntity):
    entity_description: ProtectSwitchEntityDescription
    _attr_name: Incomplete
    def __init__(self, data: ProtectData, device: NVR, description: ProtectSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class ProtectPrivacyModeSwitch(RestoreEntity, ProtectSwitch):
    device: Camera
    _previous_mic_level: Incomplete
    _previous_record_mode: Incomplete
    def __init__(self, data: ProtectData, device: ProtectAdoptableDeviceModel, description: ProtectSwitchEntityDescription) -> None: ...
    _attr_extra_state_attributes: Incomplete
    def _update_previous_attr(self) -> None: ...
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
