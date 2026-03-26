from .const import DOMAIN as DOMAIN
from .coordinator import ReolinkCoordinator as ReolinkCoordinator
from .util import ReolinkData as ReolinkData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from reolink_aio.api import Chime as Chime, Host as Host

@dataclass(frozen=True, kw_only=True)
class ReolinkEntityDescription(EntityDescription):
    cmd_key: str | None = ...
    cmd_id: int | list[int] | None = ...
    always_available: bool = ...

@dataclass(frozen=True, kw_only=True)
class ReolinkChannelEntityDescription(ReolinkEntityDescription):
    supported: Callable[[Host, int], bool] = ...

@dataclass(frozen=True, kw_only=True)
class ReolinkHostEntityDescription(ReolinkEntityDescription):
    supported: Callable[[Host], bool] = ...

@dataclass(frozen=True, kw_only=True)
class ReolinkChimeEntityDescription(ReolinkEntityDescription):
    supported: Callable[[Chime], bool] = ...

class ReolinkHostCoordinatorEntity(CoordinatorEntity[ReolinkCoordinator]):
    _attr_has_entity_name: bool
    entity_description: ReolinkEntityDescription
    _host: Incomplete
    _attr_unique_id: str
    _conf_url: Incomplete
    _dev_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, reolink_data: ReolinkData, coordinator: ReolinkCoordinator | None = None) -> None: ...
    @property
    def available(self) -> bool: ...
    @callback
    def _push_callback(self) -> None: ...
    def register_callback(self, callback_id: str, cmd_id: int) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_update(self) -> None: ...

class ReolinkChannelCoordinatorEntity(ReolinkHostCoordinatorEntity):
    _channel: Incomplete
    _attr_unique_id: Incomplete
    _dev_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, reolink_data: ReolinkData, channel: int, coordinator: ReolinkCoordinator | None = None) -> None: ...
    @property
    def available(self) -> bool: ...
    def register_callback(self, callback_id: str, cmd_id: int) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...

class ReolinkHostChimeCoordinatorEntity(ReolinkHostCoordinatorEntity):
    _channel: Incomplete
    _chime: Incomplete
    _attr_unique_id: Incomplete
    _dev_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, reolink_data: ReolinkData, chime: Chime, coordinator: ReolinkCoordinator | None = None) -> None: ...
    @property
    def available(self) -> bool: ...

class ReolinkChimeCoordinatorEntity(ReolinkChannelCoordinatorEntity):
    _chime: Incomplete
    _attr_unique_id: Incomplete
    _dev_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, reolink_data: ReolinkData, chime: Chime, coordinator: ReolinkCoordinator | None = None) -> None: ...
    @property
    def available(self) -> bool: ...
