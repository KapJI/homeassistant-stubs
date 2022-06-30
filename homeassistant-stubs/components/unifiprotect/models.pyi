from .utils import get_nested_attr as get_nested_attr
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from enum import Enum
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from pyunifiprotect.data import NVR, ProtectAdoptableDeviceModel
from typing import Any, TypeVar, Union

_LOGGER: Incomplete
T = TypeVar('T', bound=Union[ProtectAdoptableDeviceModel, NVR])

class PermRequired(int, Enum):
    NO_WRITE: int
    WRITE: int

class ProtectRequiredKeysMixin(EntityDescription):
    ufp_required_field: Union[str, None]
    ufp_value: Union[str, None]
    ufp_value_fn: Union[Callable[[T], Any], None]
    ufp_enabled: Union[str, None]
    ufp_perm: Union[PermRequired, None]
    def get_ufp_value(self, obj: T) -> Any: ...
    def get_ufp_enabled(self, obj: T) -> bool: ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_perm) -> None: ...

class ProtectSetableKeysMixin(ProtectRequiredKeysMixin[T]):
    ufp_set_method: Union[str, None]
    ufp_set_method_fn: Union[Callable[[T, Any], Coroutine[Any, Any, None]], None]
    async def ufp_set(self, obj: T, value: Any) -> None: ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_perm, ufp_set_method, ufp_set_method_fn) -> None: ...
