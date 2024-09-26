from .const import DEVICES_THAT_ADOPT as DEVICES_THAT_ADOPT, DOMAIN as DOMAIN
from .data import ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import PermRequired as PermRequired, ProtectDeviceEntity as ProtectDeviceEntity, ProtectEntityDescription as ProtectEntityDescription, ProtectSetableKeysMixin as ProtectSetableKeysMixin, T as T, async_all_device_entities as async_all_device_entities
from _typeshed import Incomplete
from collections.abc import Sequence
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Final
from uiprotect.data import ModelType, ProtectAdoptableDeviceModel

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class ProtectButtonEntityDescription(ProtectSetableKeysMixin[T], ButtonEntityDescription):
    ufp_press: str | None = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., ufp_required_field=..., ufp_value=..., ufp_value_fn=..., ufp_enabled=..., ufp_perm=..., has_required=..., get_ufp_enabled=..., ufp_set_method=..., ufp_set_method_fn=..., ufp_press=...) -> None: ...

DEVICE_CLASS_CHIME_BUTTON: Final[str]
ALL_DEVICE_BUTTONS: tuple[ProtectButtonEntityDescription, ...]
ADOPT_BUTTON: Incomplete
SENSOR_BUTTONS: tuple[ProtectButtonEntityDescription, ...]
CHIME_BUTTONS: tuple[ProtectButtonEntityDescription, ...]
_MODEL_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]

def _async_remove_adopt_button(hass: HomeAssistant, device: ProtectAdoptableDeviceModel) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectButton(ProtectDeviceEntity, ButtonEntity):
    entity_description: ProtectButtonEntityDescription
    async def async_press(self) -> None: ...

class ProtectAdoptButton(ProtectButton):
    _attr_available: Incomplete
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
