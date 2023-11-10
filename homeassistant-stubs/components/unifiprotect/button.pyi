from .const import DEVICES_THAT_ADOPT as DEVICES_THAT_ADOPT, DISPATCH_ADD as DISPATCH_ADD, DISPATCH_ADOPT as DISPATCH_ADOPT, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity, async_all_device_entities as async_all_device_entities
from .models import PermRequired as PermRequired, ProtectSetableKeysMixin as ProtectSetableKeysMixin, T as T
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data import ProtectAdoptableDeviceModel, ProtectModelWithId as ProtectModelWithId
from typing import Final

_LOGGER: Incomplete

@dataclass
class ProtectButtonEntityDescription(ProtectSetableKeysMixin[T], ButtonEntityDescription):
    ufp_press: str | None = ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_perm, ufp_set_method, ufp_set_method_fn, ufp_press) -> None: ...

DEVICE_CLASS_CHIME_BUTTON: Final[str]
KEY_ADOPT: str
ALL_DEVICE_BUTTONS: tuple[ProtectButtonEntityDescription, ...]
ADOPT_BUTTON: Incomplete
SENSOR_BUTTONS: tuple[ProtectButtonEntityDescription, ...]
CHIME_BUTTONS: tuple[ProtectButtonEntityDescription, ...]

def _async_remove_adopt_button(hass: HomeAssistant, device: ProtectAdoptableDeviceModel) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectButton(ProtectDeviceEntity, ButtonEntity):
    entity_description: ProtectButtonEntityDescription
    _attr_name: Incomplete
    def __init__(self, data: ProtectData, device: ProtectAdoptableDeviceModel, description: ProtectButtonEntityDescription) -> None: ...
    _attr_available: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...
    async def async_press(self) -> None: ...
    def _async_updated_event(self, device: ProtectModelWithId) -> None: ...
