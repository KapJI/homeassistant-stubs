import abc
from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete

class AirzoneEntity(CoordinatorEntity[AirzoneUpdateCoordinator], ABC, metaclass=abc.ABCMeta):
    @property
    def available(self) -> bool: ...
    @abstractmethod
    def get_airzone_value(self, key: str) -> Any: ...
    async def _async_update_params(self, params: dict[str, Any]) -> None: ...

class AirzoneAidooEntity(AirzoneEntity):
    aidoo_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, aidoo_id: str, aidoo_data: dict[str, Any]) -> None: ...
    def get_airzone_value(self, key: str) -> Any: ...

class AirzoneSystemEntity(AirzoneEntity):
    system_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, system_id: str, system_data: dict[str, Any]) -> None: ...
    def get_airzone_value(self, key: str) -> Any: ...

class AirzoneWebServerEntity(AirzoneEntity):
    ws_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, ws_id: str, ws_data: dict[str, Any]) -> None: ...
    def get_airzone_value(self, key: str) -> Any: ...

class AirzoneZoneEntity(AirzoneEntity):
    system_id: Incomplete
    zone_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, zone_id: str, zone_data: dict[str, Any]) -> None: ...
    def get_airzone_value(self, key: str) -> Any: ...
    async def _async_update_params(self, params: dict[str, Any]) -> None: ...
