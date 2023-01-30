import abc
from .const import DOMAIN as DOMAIN
from .utils import BondDevice as BondDevice, BondHub as BondHub
from _typeshed import Incomplete
from abc import abstractmethod
from bond_async import BPUPSubscriptions as BPUPSubscriptions
from datetime import datetime
from homeassistant.const import ATTR_HW_VERSION as ATTR_HW_VERSION, ATTR_MODEL as ATTR_MODEL, ATTR_NAME as ATTR_NAME, ATTR_SUGGESTED_AREA as ATTR_SUGGESTED_AREA, ATTR_SW_VERSION as ATTR_SW_VERSION, ATTR_VIA_DEVICE as ATTR_VIA_DEVICE
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval

_LOGGER: Incomplete
_FALLBACK_SCAN_INTERVAL: Incomplete

class BondEntity(Entity, metaclass=abc.ABCMeta):
    _attr_should_poll: bool
    _hub: Incomplete
    _device: Incomplete
    _device_id: Incomplete
    _sub_device: Incomplete
    _attr_available: bool
    _bpup_subs: Incomplete
    _update_lock: Incomplete
    _initialized: bool
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_assumed_state: Incomplete
    def __init__(self, hub: BondHub, device: BondDevice, bpup_subs: BPUPSubscriptions, sub_device: Union[str, None] = ..., sub_device_id: Union[str, None] = ...) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_update(self) -> None: ...
    def _async_update_if_bpup_not_alive(self, now: datetime) -> None: ...
    async def _async_update(self) -> None: ...
    async def _async_update_from_api(self) -> None: ...
    @abstractmethod
    def _apply_state(self) -> None: ...
    def _async_state_callback(self, state: dict) -> None: ...
    def _async_bpup_callback(self, json_msg: dict) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
