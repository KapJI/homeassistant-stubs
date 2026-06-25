from . import DevoloHomeControlConfigEntry as DevoloHomeControlConfigEntry
from .entity import DevoloMultiLevelSwitchDeviceEntity as DevoloMultiLevelSwitchDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeControlConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DevoloCoverDeviceEntity(DevoloMultiLevelSwitchDeviceEntity, CoverEntity):
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    @property
    @override
    def current_cover_position(self) -> int: ...
    @property
    @override
    def is_closed(self) -> bool: ...
    @override
    def open_cover(self, **kwargs: Any) -> None: ...
    @override
    def close_cover(self, **kwargs: Any) -> None: ...
    @override
    def set_cover_position(self, **kwargs: Any) -> None: ...
