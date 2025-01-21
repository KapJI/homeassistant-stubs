from . import IottyConfigEntry as IottyConfigEntry
from .api import IottyProxy as IottyProxy
from .coordinator import IottyDataUpdateCoordinator as IottyDataUpdateCoordinator
from .entity import IottyEntity as IottyEntity
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from iottycloud.device import Device as Device
from iottycloud.shutter import Shutter
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: IottyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IottyShutter(IottyEntity, CoverEntity):
    _attr_device_class: Incomplete
    _iotty_device: Shutter
    _attr_supported_features: CoverEntityFeature
    def __init__(self, coordinator: IottyDataUpdateCoordinator, iotty_cloud: IottyProxy, iotty_device: Shutter) -> None: ...
    @property
    def current_cover_position(self) -> int | None: ...
    @property
    def is_closed(self) -> bool: ...
    @property
    def is_opening(self) -> bool: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def supported_features(self) -> CoverEntityFeature: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
