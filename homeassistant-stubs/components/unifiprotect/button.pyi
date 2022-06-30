from .const import DISPATCH_ADOPT as DISPATCH_ADOPT, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity, async_all_device_entities as async_all_device_entities
from .models import PermRequired as PermRequired, ProtectSetableKeysMixin as ProtectSetableKeysMixin, T as T
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data import ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel
from typing import Final

class ProtectButtonEntityDescription(ProtectSetableKeysMixin[T], ButtonEntityDescription):
    ufp_press: Union[str, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_perm, ufp_set_method, ufp_set_method_fn, ufp_press) -> None: ...

DEVICE_CLASS_CHIME_BUTTON: Final[str]
ALL_DEVICE_BUTTONS: tuple[ProtectButtonEntityDescription, ...]
SENSOR_BUTTONS: tuple[ProtectButtonEntityDescription, ...]
CHIME_BUTTONS: tuple[ProtectButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectButton(ProtectDeviceEntity, ButtonEntity):
    entity_description: ProtectButtonEntityDescription
    _attr_name: Incomplete
    def __init__(self, data: ProtectData, device: ProtectAdoptableDeviceModel, description: ProtectButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
