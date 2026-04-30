from .const import DEFAULT_ATTRIBUTION as DEFAULT_ATTRIBUTION, DEFAULT_BRAND as DEFAULT_BRAND, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import BaseProtectEntity as BaseProtectEntity, PermRequired as PermRequired, ProtectDeviceEntity as ProtectDeviceEntity, ProtectEntityDescription as ProtectEntityDescription, ProtectIsOnEntity as ProtectIsOnEntity, ProtectNVREntity as ProtectNVREntity, ProtectSettableKeysMixin as ProtectSettableKeysMixin, T as T, async_all_device_entities as async_all_device_entities
from .utils import async_ufp_instance_command as async_ufp_instance_command
from _typeshed import Incomplete
from collections.abc import Sequence
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from typing import Any, Literal
from uiprotect.data import Camera, ModelType, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, PublicRelayOutput as PublicRelayOutput, Relay as Relay, RelayOutputState

ATTR_PREV_MIC: str
ATTR_PREV_RECORD: str
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ProtectSwitchEntityDescription(ProtectSettableKeysMixin[T], SwitchEntityDescription): ...

async def _set_highfps(obj: Camera, value: bool) -> None: ...

CAMERA_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
PRIVACY_MODE_SWITCH: Incomplete
SENSE_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
LIGHT_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
DOORLOCK_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
VIEWER_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
NVR_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
_RELAY_STATE_MAP: dict[RelayOutputState, bool]
_MODEL_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]
_PRIVACY_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]

class ProtectBaseSwitch(ProtectIsOnEntity):
    entity_description: ProtectSwitchEntityDescription
    @async_ufp_instance_command
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @async_ufp_instance_command
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class ProtectSwitch(ProtectDeviceEntity, ProtectBaseSwitch, SwitchEntity):
    entity_description: ProtectSwitchEntityDescription

class ProtectNVRSwitch(ProtectNVREntity, ProtectBaseSwitch, SwitchEntity):
    entity_description: ProtectSwitchEntityDescription

class ProtectPrivacyModeSwitch(RestoreEntity, ProtectSwitch):
    device: Camera
    entity_description: ProtectSwitchEntityDescription
    _previous_mic_level: Incomplete
    _previous_record_mode: Incomplete
    def __init__(self, data: ProtectData, device: Camera, description: ProtectSwitchEntityDescription) -> None: ...
    _attr_extra_state_attributes: Incomplete
    @callback
    def _update_previous_attr(self) -> None: ...
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
    @async_ufp_instance_command
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @async_ufp_instance_command
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ProtectRelayOutputSwitch(SwitchEntity):
    _attr_has_entity_name: bool
    _attr_attribution = DEFAULT_ATTRIBUTION
    _attr_should_poll: bool
    _attr_translation_key: str
    data: Incomplete
    _relay_id: Incomplete
    _relay_mac: Incomplete
    _output_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data: ProtectData, relay: Relay, output: PublicRelayOutput) -> None: ...
    @property
    def _relay(self) -> Relay | None: ...
    _attr_available: bool
    _attr_is_on: Incomplete
    @callback
    def _update_from_relay(self, relay: Relay) -> None: ...
    @callback
    def _async_updated(self, relay: Relay) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _activate_output(self, state: Literal['on', 'off']) -> None: ...
    @async_ufp_instance_command
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @async_ufp_instance_command
    async def async_turn_off(self, **kwargs: Any) -> None: ...
