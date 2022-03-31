import abc
from .const import DOMAIN as DOMAIN, MODEL_NAMES as MODEL_NAMES
from .coordinator import LookinDataUpdateCoordinator as LookinDataUpdateCoordinator
from .models import LookinData as LookinData
from abc import abstractmethod
from aiolookin import Climate as Climate, Remote
from aiolookin.models import Device as Device, UDPEvent as UDPEvent
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

LOGGER: Any

def _lookin_device_to_device_info(lookin_device: Device, host: str) -> DeviceInfo: ...
def _lookin_controlled_device_to_device_info(lookin_device: Device, uuid: str, device: Union[Climate, Remote], host: str) -> DeviceInfo: ...

class LookinDeviceMixIn:
    _lookin_device: Any
    _lookin_protocol: Any
    _lookin_udp_subs: Any
    def _set_lookin_device_attrs(self, lookin_data: LookinData) -> None: ...

class LookinDeviceCoordinatorEntity(LookinDeviceMixIn, CoordinatorEntity[LookinDataUpdateCoordinator]):
    _attr_should_poll: bool
    _attr_device_info: Any
    def __init__(self, lookin_data: LookinData) -> None: ...

class LookinEntityMixIn:
    _device: Any
    _uuid: Any
    _meteo_coordinator: Any
    _function_names: Any
    def _set_lookin_entity_attrs(self, uuid: str, device: Union[Remote, Climate], lookin_data: LookinData) -> None: ...

class LookinCoordinatorEntity(LookinDeviceMixIn, LookinEntityMixIn, CoordinatorEntity[LookinDataUpdateCoordinator]):
    _attr_should_poll: bool
    _attr_assumed_state: bool
    _attr_device_info: Any
    _attr_unique_id: Any
    _attr_name: Any
    def __init__(self, coordinator: LookinDataUpdateCoordinator, uuid: str, device: Union[Remote, Climate], lookin_data: LookinData) -> None: ...
    async def _async_send_command(self, command: str) -> None: ...

class LookinPowerEntity(LookinCoordinatorEntity):
    _power_on_command: Any
    _power_off_command: Any
    def __init__(self, coordinator: LookinDataUpdateCoordinator, uuid: str, device: Union[Remote, Climate], lookin_data: LookinData) -> None: ...

class LookinPowerPushRemoteEntity(LookinPowerEntity, metaclass=abc.ABCMeta):
    _attr_name: Any
    def __init__(self, coordinator: LookinDataUpdateCoordinator, uuid: str, device: Remote, lookin_data: LookinData) -> None: ...
    @property
    def _remote(self) -> Remote: ...
    @abstractmethod
    def _update_from_status(self, status: str) -> None: ...
    def _async_push_update(self, event: UDPEvent) -> None: ...
    async def _async_push_update_device(self, event: UDPEvent) -> None: ...
    async def async_added_to_hass(self) -> None: ...
