from . import AladdinConnectConfigEntry as AladdinConnectConfigEntry, AladdinConnectCoordinator as AladdinConnectCoordinator
from .entity import AladdinConnectEntity as AladdinConnectEntity
from _typeshed import Incomplete
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: AladdinConnectConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AladdinDevice(AladdinConnectEntity, CoverEntity):
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AladdinConnectCoordinator, device: GarageDoor) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    @property
    def is_closed(self) -> bool | None: ...
    @property
    def is_closing(self) -> bool | None: ...
    @property
    def is_opening(self) -> bool | None: ...
