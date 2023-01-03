from .const import DISPATCH_ADOPT as DISPATCH_ADOPT, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity, async_all_device_entities as async_all_device_entities
from .models import PermRequired as PermRequired, ProtectSetableKeysMixin as ProtectSetableKeysMixin, T as T
from _typeshed import Incomplete
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, TIME_SECONDS as TIME_SECONDS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data import Camera as Camera, Doorlock, Light, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, ProtectModelWithId as ProtectModelWithId

class NumberKeysMixin:
    ufp_max: int
    ufp_min: int
    ufp_step: int
    def __init__(self, ufp_max, ufp_min, ufp_step) -> None: ...

class ProtectNumberEntityDescription(ProtectSetableKeysMixin[T], NumberEntityDescription, NumberKeysMixin):
    def __init__(self, ufp_max, ufp_min, ufp_step, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, max_value, min_value, native_max_value, native_min_value, native_unit_of_measurement, native_step, step, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_perm, ufp_set_method, ufp_set_method_fn) -> None: ...

def _get_pir_duration(obj: Light) -> int: ...
async def _set_pir_duration(obj: Light, value: float) -> None: ...
def _get_auto_close(obj: Doorlock) -> int: ...
async def _set_auto_close(obj: Doorlock, value: float) -> None: ...

CAMERA_NUMBERS: tuple[ProtectNumberEntityDescription, ...]
LIGHT_NUMBERS: tuple[ProtectNumberEntityDescription, ...]
SENSE_NUMBERS: tuple[ProtectNumberEntityDescription, ...]
DOORLOCK_NUMBERS: tuple[ProtectNumberEntityDescription, ...]
CHIME_NUMBERS: tuple[ProtectNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectNumbers(ProtectDeviceEntity, NumberEntity):
    device: Union[Camera, Light]
    entity_description: ProtectNumberEntityDescription
    _attr_native_max_value: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_step: Incomplete
    def __init__(self, data: ProtectData, device: Union[Camera, Light], description: ProtectNumberEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
