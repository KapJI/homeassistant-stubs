import abc
from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class AirzoneEntity(CoordinatorEntity[AirzoneUpdateCoordinator], ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def get_airzone_value(self, key: str) -> Any: ...

class AirzoneAidooEntity(AirzoneEntity):
    aidoo_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, entry: ConfigEntry, aidoo_id: str, aidoo_data: dict[str, Any]) -> None: ...
    def get_airzone_value(self, key: str) -> Any: ...

class AirzoneWebServerEntity(AirzoneEntity):
    ws_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, entry: ConfigEntry, ws_id: str, ws_data: dict[str, Any]) -> None: ...
    def get_airzone_value(self, key: str) -> Any: ...

class AirzoneZoneEntity(AirzoneEntity):
    system_id: Incomplete
    zone_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, entry: ConfigEntry, zone_id: str, zone_data: dict[str, Any]) -> None: ...
    def get_airzone_value(self, key: str) -> Any: ...
