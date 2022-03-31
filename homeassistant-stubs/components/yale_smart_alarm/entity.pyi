from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, MODEL as MODEL
from .coordinator import YaleDataUpdateCoordinator as YaleDataUpdateCoordinator
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class YaleEntity(CoordinatorEntity[YaleDataUpdateCoordinator], Entity):
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, coordinator: YaleDataUpdateCoordinator, data: dict) -> None: ...

class YaleAlarmEntity(CoordinatorEntity[YaleDataUpdateCoordinator], Entity):
    _attr_device_info: Any
    def __init__(self, coordinator: YaleDataUpdateCoordinator) -> None: ...
