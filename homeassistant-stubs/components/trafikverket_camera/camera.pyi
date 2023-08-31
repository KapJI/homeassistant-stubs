from .const import ATTR_DESCRIPTION as ATTR_DESCRIPTION, ATTR_TYPE as ATTR_TYPE, DOMAIN as DOMAIN
from .coordinator import TVDataUpdateCoordinator as TVDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.camera import Camera as Camera
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LOCATION as ATTR_LOCATION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TVCamera(CoordinatorEntity[TVDataUpdateCoordinator], Camera):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_translation_key: str
    coordinator: TVDataUpdateCoordinator
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TVDataUpdateCoordinator, name: str, entry_id: str) -> None: ...
    async def async_camera_image(self, width: int | None = ..., height: int | None = ...) -> bytes | None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
