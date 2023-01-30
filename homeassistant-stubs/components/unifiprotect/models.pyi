from .utils import get_nested_attr as get_nested_attr
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from enum import Enum
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from pyunifiprotect.data import Event, NVR, ProtectAdoptableDeviceModel
from typing import Any, TypeVar

_LOGGER: Incomplete
T = TypeVar('T', bound=ProtectAdoptableDeviceModel | NVR)

class PermRequired(int, Enum):
    NO_WRITE: int
    WRITE: int
    DELETE: int

class ProtectRequiredKeysMixin(EntityDescription):
    ufp_required_field: Union[str, None]
    ufp_value: Union[str, None]
    ufp_value_fn: Union[Callable[[T], Any], None]
    ufp_enabled: Union[str, None]
    ufp_perm: Union[PermRequired, None]
    def get_ufp_value(self, obj: T) -> Any: ...
    def get_ufp_enabled(self, obj: T) -> bool: ...
    def has_required(self, obj: T) -> bool: ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_perm) -> None: ...

class ProtectEventMixin(ProtectRequiredKeysMixin[T]):
    ufp_event_obj: Union[str, None]
    ufp_smart_type: Union[str, None]
    def get_event_obj(self, obj: T) -> Union[Event, None]: ...
    def get_is_on(self, obj: T) -> bool: ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_perm, ufp_event_obj, ufp_smart_type) -> None: ...

class ProtectSetableKeysMixin(ProtectRequiredKeysMixin[T]):
    ufp_set_method: Union[str, None]
    ufp_set_method_fn: Union[Callable[[T, Any], Coroutine[Any, Any, None]], None]
    async def ufp_set(self, obj: T, value: Any) -> None: ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_perm, ufp_set_method, ufp_set_method_fn) -> None: ...
