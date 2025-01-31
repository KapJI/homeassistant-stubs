import abc
from . import get_device_name as get_device_name, legacy_device_id as legacy_device_id
from .const import ATTR_CURRENT_A as ATTR_CURRENT_A, ATTR_CURRENT_POWER_W as ATTR_CURRENT_POWER_W, ATTR_TODAY_ENERGY_KWH as ATTR_TODAY_ENERGY_KWH, ATTR_TOTAL_ENERGY_KWH as ATTR_TOTAL_ENERGY_KWH, DOMAIN as DOMAIN, PRIMARY_STATE_ID as PRIMARY_STATE_ID
from .coordinator import TPLinkConfigEntry as TPLinkConfigEntry, TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .deprecate import DeprecatedInfo as DeprecatedInfo, async_check_create_deprecated as async_check_create_deprecated, async_process_deprecated as async_process_deprecated
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Awaitable, Callable as Callable, Coroutine, Iterable, Mapping
from dataclasses import dataclass
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from kasa import Device, Feature
from typing import Any, Concatenate

_LOGGER: Incomplete
FEATURE_CATEGORY_TO_ENTITY_CATEGORY: Incomplete
DEVICETYPES_WITH_SPECIALIZED_PLATFORMS: Incomplete
FEATURES_ALLOW_LIST: Incomplete
EXCLUDED_FEATURES: Incomplete
LEGACY_KEY_MAPPING: Incomplete

@dataclass(frozen=True, kw_only=True)
class TPLinkEntityDescription(EntityDescription):
    deprecated_info: DeprecatedInfo | None = ...
    available_fn: Callable[[Device], bool] = ...

@dataclass(frozen=True, kw_only=True)
class TPLinkFeatureEntityDescription(TPLinkEntityDescription): ...

@dataclass(frozen=True, kw_only=True)
class TPLinkModuleEntityDescription(TPLinkEntityDescription):
    exists_fn: Callable[[Device, TPLinkConfigEntry], bool]
    unique_id_fn: Callable[[Device, TPLinkModuleEntityDescription], str] = ...
    entity_name_fn: Callable[[Device, TPLinkModuleEntityDescription], str | None] | None = ...

def async_refresh_after[_T: CoordinatedTPLinkEntity, **_P](func: Callable[Concatenate[_T, _P], Awaitable[None]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]: ...

class CoordinatedTPLinkEntity(CoordinatorEntity[TPLinkDataUpdateCoordinator], ABC, metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _device: Device
    entity_description: TPLinkEntityDescription
    _parent: Incomplete
    _feature: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, description: TPLinkEntityDescription, *, feature: Feature | None = None, parent: Device | None = None) -> None: ...
    def _get_unique_id(self) -> str: ...
    async def async_added_to_hass(self) -> None: ...
    @abstractmethod
    @callback
    def _async_update_attrs(self) -> bool: ...
    _attr_available: bool
    @callback
    def _async_call_update_attrs(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def available(self) -> bool: ...

class CoordinatedTPLinkFeatureEntity(CoordinatedTPLinkEntity, ABC, metaclass=abc.ABCMeta):
    entity_description: TPLinkFeatureEntityDescription
    _feature: Feature
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, description: TPLinkFeatureEntityDescription, *, feature: Feature, parent: Device | None = None) -> None: ...
    def _get_unique_id(self) -> str: ...
    @staticmethod
    def _get_feature_unique_id(device: Device, entity_description: TPLinkFeatureEntityDescription) -> str: ...
    @classmethod
    def _category_for_feature(cls, feature: Feature | None) -> EntityCategory | None: ...
    @classmethod
    def _description_for_feature[_D: EntityDescription](cls, feature: Feature, descriptions: Mapping[str, _D], *, device: Device, parent: Device | None = None) -> _D | None: ...
    @classmethod
    def _entities_for_device[_E: CoordinatedTPLinkFeatureEntity, _D: TPLinkFeatureEntityDescription](cls, hass: HomeAssistant, device: Device, coordinator: TPLinkDataUpdateCoordinator, *, feature_type: Feature.Type, entity_class: type[_E], descriptions: Mapping[str, _D], platform_domain: str, parent: Device | None = None) -> list[_E]: ...
    @classmethod
    def entities_for_device_and_its_children[_E: CoordinatedTPLinkFeatureEntity, _D: TPLinkFeatureEntityDescription](cls, hass: HomeAssistant, device: Device, coordinator: TPLinkDataUpdateCoordinator, *, feature_type: Feature.Type, entity_class: type[_E], descriptions: Mapping[str, _D], platform_domain: str, known_child_device_ids: set[str], first_check: bool) -> list[_E]: ...

class CoordinatedTPLinkModuleEntity(CoordinatedTPLinkEntity, ABC, metaclass=abc.ABCMeta):
    entity_description: TPLinkModuleEntityDescription
    _attr_name: Incomplete
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, description: TPLinkModuleEntityDescription, *, parent: Device | None = None) -> None: ...
    def _get_unique_id(self) -> str: ...
    @classmethod
    def _entities_for_device[_E: CoordinatedTPLinkModuleEntity, _D: TPLinkModuleEntityDescription](cls, hass: HomeAssistant, device: Device, coordinator: TPLinkDataUpdateCoordinator, *, entity_class: type[_E], descriptions: Iterable[_D], platform_domain: str, parent: Device | None = None) -> list[_E]: ...
    @classmethod
    def entities_for_device_and_its_children[_E: CoordinatedTPLinkModuleEntity, _D: TPLinkModuleEntityDescription](cls, hass: HomeAssistant, device: Device, coordinator: TPLinkDataUpdateCoordinator, *, entity_class: type[_E], descriptions: Iterable[_D], platform_domain: str, known_child_device_ids: set[str], first_check: bool) -> list[_E]: ...

def _get_new_children(device: Device, coordinator: TPLinkDataUpdateCoordinator, known_child_device_ids: set[str], entity_class_name: str) -> list[Device]: ...
