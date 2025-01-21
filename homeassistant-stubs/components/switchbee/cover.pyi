from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBeeCoordinator as SwitchBeeCoordinator
from .entity import SwitchBeeDeviceEntity as SwitchBeeDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from switchbee.device import SwitchBeeShutter, SwitchBeeSomfy
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitchBeeSomfyEntity(SwitchBeeDeviceEntity[SwitchBeeSomfy], CoverEntity):
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_is_closed: Incomplete
    async def _fire_somfy_command(self, command: str) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...

class SwitchBeeCoverEntity(SwitchBeeDeviceEntity[SwitchBeeShutter], CoverEntity):
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_is_closed: bool | None
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_current_cover_position: Incomplete
    def _update_from_coordinator(self) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
