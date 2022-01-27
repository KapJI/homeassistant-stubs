from .const import DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity, async_all_device_entities as async_all_device_entities
from .models import ProtectSetableKeysMixin as ProtectSetableKeysMixin, T as T
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import TIME_SECONDS as TIME_SECONDS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data.devices import Camera as Camera, Doorlock, Light
from typing import Any

class NumberKeysMixin:
    ufp_max: int
    ufp_min: int
    ufp_step: int
    def __init__(self, ufp_max, ufp_min, ufp_step) -> None: ...

class ProtectNumberEntityDescription(ProtectSetableKeysMixin, NumberEntityDescription, NumberKeysMixin):
    def __init__(self, ufp_max, ufp_min, ufp_step, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, max_value, min_value, step, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_set_method, ufp_set_method_fn) -> None: ...

def _get_pir_duration(obj: Light) -> int: ...
async def _set_pir_duration(obj: Light, value: float) -> None: ...
def _get_auto_close(obj: Doorlock) -> int: ...
async def _set_auto_close(obj: Doorlock, value: float) -> None: ...

CAMERA_NUMBERS: tuple[ProtectNumberEntityDescription, ...]
LIGHT_NUMBERS: tuple[ProtectNumberEntityDescription, ...]
SENSE_NUMBERS: tuple[ProtectNumberEntityDescription, ...]
DOORLOCK_NUMBERS: tuple[ProtectNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectNumbers(ProtectDeviceEntity, NumberEntity):
    device: Union[Camera, Light]
    entity_description: ProtectNumberEntityDescription
    _attr_max_value: Any
    _attr_min_value: Any
    _attr_step: Any
    def __init__(self, data: ProtectData, device: Union[Camera, Light], description: ProtectNumberEntityDescription) -> None: ...
    _attr_value: Any
    def _async_update_device_from_protect(self) -> None: ...
    async def async_set_value(self, value: float) -> None: ...
