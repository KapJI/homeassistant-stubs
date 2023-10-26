from . import DeskData as DeskData, IdasenDeskCoordinator as IdasenDeskCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IdasenDeskCover(CoordinatorEntity[IdasenDeskCoordinator], CoverEntity):
    _attr_device_class: Incomplete
    _attr_icon: str
    _attr_supported_features: Incomplete
    _desk: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_current_cover_position: Incomplete
    def __init__(self, address: str, device_info: DeviceInfo, coordinator: IdasenDeskCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_closed(self) -> bool: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    def _handle_coordinator_update(self, *args: Any) -> None: ...
