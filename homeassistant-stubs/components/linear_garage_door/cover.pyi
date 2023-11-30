from .const import DOMAIN as DOMAIN
from .coordinator import LinearUpdateCoordinator as LinearUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

SUPPORTED_SUBDEVICES: Incomplete
PARALLEL_UPDATES: int
SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LinearCoverEntity(CoordinatorEntity[LinearUpdateCoordinator], CoverEntity):
    _attr_supported_features: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _device_id: Incomplete
    _device_name: Incomplete
    _subdevice: Incomplete
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    _config_entry: Incomplete
    def __init__(self, device_id: str, device_name: str, subdevice: str, config_entry: ConfigEntry, coordinator: LinearUpdateCoordinator) -> None: ...
    def _get_data(self, data_property: str) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def is_closed(self) -> bool: ...
    @property
    def is_opened(self) -> bool: ...
    @property
    def is_opening(self) -> bool: ...
    @property
    def is_closing(self) -> bool: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
