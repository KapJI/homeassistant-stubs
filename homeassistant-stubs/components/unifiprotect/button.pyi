from .const import DEVICES_THAT_ADOPT as DEVICES_THAT_ADOPT, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data.base import ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectButton(ProtectDeviceEntity, ButtonEntity):
    _attr_entity_registry_enabled_default: bool
    _attr_device_class: Incomplete
    _attr_name: Incomplete
    def __init__(self, data: ProtectData, device: ProtectAdoptableDeviceModel) -> None: ...
    async def async_press(self) -> None: ...
