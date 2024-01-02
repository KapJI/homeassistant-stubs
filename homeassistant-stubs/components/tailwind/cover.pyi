from .const import DOMAIN as DOMAIN
from .coordinator import TailwindDataUpdateCoordinator as TailwindDataUpdateCoordinator
from .entity import TailwindDoorEntity as TailwindDoorEntity
from _typeshed import Incomplete
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TailwindDoorCoverEntity(TailwindDoorEntity, CoverEntity):
    _attr_device_class: Incomplete
    _attr_is_closing: bool
    _attr_is_opening: bool
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    @property
    def is_closed(self) -> bool: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
