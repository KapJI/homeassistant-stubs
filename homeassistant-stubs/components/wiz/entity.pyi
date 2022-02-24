import abc
from .models import WizData as WizData
from abc import abstractmethod
from homeassistant.const import ATTR_HW_VERSION as ATTR_HW_VERSION, ATTR_MODEL as ATTR_MODEL
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, ToggleEntity as ToggleEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pywizlight.bulblibrary import BulbType as BulbType
from typing import Any

class WizEntity(CoordinatorEntity, Entity, metaclass=abc.ABCMeta):
    _device: Any
    _attr_unique_id: Any
    _attr_name: Any
    _attr_device_info: Any
    def __init__(self, wiz_data: WizData, name: str) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    @abstractmethod
    def _async_update_attrs(self) -> None: ...

class WizToggleEntity(WizEntity, ToggleEntity):
    _attr_is_on: Any
    def _async_update_attrs(self) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
