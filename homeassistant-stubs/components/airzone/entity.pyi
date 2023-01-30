from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete

class AirzoneEntity(CoordinatorEntity[AirzoneUpdateCoordinator]):
    def get_airzone_value(self, key: str) -> Any: ...

class AirzoneSystemEntity(AirzoneEntity):
    system_id: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, entry: ConfigEntry, system_data: dict[str, Any]) -> None: ...
    def get_airzone_value(self, key: str) -> Any: ...

class AirzoneWebServerEntity(AirzoneEntity):
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, entry: ConfigEntry) -> None: ...
    def get_airzone_value(self, key: str) -> Any: ...

class AirzoneZoneEntity(AirzoneEntity):
    system_id: Incomplete
    system_zone_id: Incomplete
    zone_id: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, entry: ConfigEntry, system_zone_id: str, zone_data: dict[str, Any]) -> None: ...
    def get_airzone_value(self, key: str) -> Any: ...
    async def _async_update_hvac_params(self, params: dict[str, Any]) -> None: ...
