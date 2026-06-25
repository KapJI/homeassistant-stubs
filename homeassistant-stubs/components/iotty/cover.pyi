from .api import IottyProxy as IottyProxy
from .coordinator import IottyConfigEntry as IottyConfigEntry, IottyDataUpdateCoordinator as IottyDataUpdateCoordinator
from .entity import IottyEntity as IottyEntity
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from iottycloud.device import Device as Device
from iottycloud.shutter import Shutter
from typing import Any, override

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: IottyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IottyShutter(IottyEntity, CoverEntity):
    _attr_device_class: Incomplete
    _iotty_device: Shutter
    _attr_supported_features: CoverEntityFeature
    def __init__(self, coordinator: IottyDataUpdateCoordinator, iotty_cloud: IottyProxy, iotty_device: Shutter) -> None: ...
    @property
    @override
    def current_cover_position(self) -> int | None: ...
    @property
    @override
    def is_closed(self) -> bool: ...
    @property
    @override
    def is_opening(self) -> bool: ...
    @property
    @override
    def is_closing(self) -> bool: ...
    @property
    @override
    def supported_features(self) -> CoverEntityFeature: ...
    @override
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    @override
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    @override
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    @override
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    @callback
    @override
    def _handle_coordinator_update(self) -> None: ...
