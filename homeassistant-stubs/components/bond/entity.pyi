import abc
from .const import DOMAIN as DOMAIN
from .utils import BondDevice as BondDevice, BondHub as BondHub
from abc import abstractmethod
from bond_api import BPUPSubscriptions as BPUPSubscriptions
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from typing import Any

_LOGGER: Any
_FALLBACK_SCAN_INTERVAL: Any

class BondEntity(Entity, metaclass=abc.ABCMeta):
    _attr_should_poll: bool
    _hub: Any
    _device: Any
    _device_id: Any
    _sub_device: Any
    _attr_available: bool
    _bpup_subs: Any
    _update_lock: Any
    _initialized: bool
    _attr_unique_id: Any
    _attr_name: Any
    def __init__(self, hub: BondHub, device: BondDevice, bpup_subs: BPUPSubscriptions, sub_device: Union[str, None] = ...) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_update(self) -> None: ...
    async def _async_update_if_bpup_not_alive(self, *_: Any) -> None: ...
    _attr_assumed_state: Any
    async def _async_update_from_api(self) -> None: ...
    @abstractmethod
    def _apply_state(self, state: dict) -> None: ...
    def _async_state_callback(self, state: dict) -> None: ...
    def _async_bpup_callback(self, state: dict) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
