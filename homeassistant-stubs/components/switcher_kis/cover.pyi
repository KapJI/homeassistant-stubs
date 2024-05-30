from .const import SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from .coordinator import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from _typeshed import Incomplete
from aioswitcher.api import SwitcherBaseResponse as SwitcherBaseResponse
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete
API_SET_POSITON: str
API_STOP: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitcherCoverEntity(CoordinatorEntity[SwitcherDataUpdateCoordinator], CoverEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    _attr_current_cover_position: Incomplete
    _attr_is_closed: Incomplete
    _attr_is_closing: Incomplete
    _attr_is_opening: Incomplete
    def _update_data(self) -> None: ...
    async def _async_call_api(self, api: str, *args: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
