from .const import DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity, async_all_device_entities as async_all_device_entities
from .models import ProtectSetableKeysMixin as ProtectSetableKeysMixin, T as T
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data import Camera
from pyunifiprotect.data.base import ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel
from typing import Any

_LOGGER: Any

class ProtectSwitchEntityDescription(ProtectSetableKeysMixin, SwitchEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_set_method, ufp_set_method_fn) -> None: ...

_KEY_PRIVACY_MODE: str

def _get_is_highfps(obj: Camera) -> bool: ...
async def _set_highfps(obj: Camera, value: bool) -> None: ...

ALL_DEVICES_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
CAMERA_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
SENSE_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
LIGHT_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
DOORLOCK_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectSwitch(ProtectDeviceEntity, SwitchEntity):
    entity_description: ProtectSwitchEntityDescription
    _attr_name: Any
    _switch_type: Any
    _previous_mic_level: int
    _previous_record_mode: Any
    def __init__(self, data: ProtectData, device: ProtectAdoptableDeviceModel, description: ProtectSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
