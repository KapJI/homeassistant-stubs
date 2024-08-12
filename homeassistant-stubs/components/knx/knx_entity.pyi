import abc
from . import KNXModule as KNXModule
from .storage.config_store import PlatformControllerBase as PlatformControllerBase
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import EntityPlatform as EntityPlatform
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from typing import Any
from xknx.devices import Device as XknxDevice

class KnxUiEntityPlatformController(PlatformControllerBase):
    _knx_module: Incomplete
    _entity_platform: Incomplete
    _entity_class: Incomplete
    def __init__(self, knx_module: KNXModule, entity_platform: EntityPlatform, entity_class: type[KnxUiEntity]) -> None: ...
    async def create_entity(self, unique_id: str, config: dict[str, Any]) -> None: ...
    async def update_entity(self, entity_entry: RegistryEntry, config: dict[str, Any]) -> None: ...

class _KnxEntityBase(Entity):
    _attr_should_poll: bool
    _knx_module: KNXModule
    _device: XknxDevice
    @property
    def name(self) -> str: ...
    @property
    def available(self) -> bool: ...
    async def async_update(self) -> None: ...
    def after_update_callback(self, _device: XknxDevice) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...

class KnxYamlEntity(_KnxEntityBase):
    _knx_module: Incomplete
    _device: Incomplete
    def __init__(self, knx_module: KNXModule, device: XknxDevice) -> None: ...

class KnxUiEntity(_KnxEntityBase, ABC, metaclass=abc.ABCMeta):
    _attr_unique_id: str
    @abstractmethod
    def __init__(self, knx_module: KNXModule, unique_id: str, config: dict[str, Any]): ...
