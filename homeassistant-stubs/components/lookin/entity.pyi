from .const import DOMAIN as DOMAIN
from .models import LookinData as LookinData
from aiolookin import Climate as Climate, Remote as Remote
from aiolookin.models import Device as Device
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

def _lookin_device_to_device_info(lookin_device: Device) -> DeviceInfo: ...
def _lookin_controlled_device_to_device_info(lookin_device: Device, uuid: str, device: Union[Climate, Remote]) -> DeviceInfo: ...

class LookinDeviceMixIn:
    _lookin_device: Any
    _lookin_protocol: Any
    _lookin_udp_subs: Any
    def _set_lookin_device_attrs(self, lookin_data: LookinData) -> None: ...

class LookinDeviceEntity(LookinDeviceMixIn, Entity):
    _attr_should_poll: bool
    _attr_device_info: Any
    def __init__(self, lookin_data: LookinData) -> None: ...

class LookinDeviceCoordinatorEntity(LookinDeviceMixIn, CoordinatorEntity):
    _attr_should_poll: bool
    _attr_device_info: Any
    def __init__(self, lookin_data: LookinData) -> None: ...

class LookinEntityMixIn:
    _device: Any
    _uuid: Any
    _meteo_coordinator: Any
    _function_names: Any
    def _set_lookin_entity_attrs(self, uuid: str, device: Union[Remote, Climate], lookin_data: LookinData) -> None: ...

class LookinEntity(LookinDeviceMixIn, LookinEntityMixIn, Entity):
    _attr_should_poll: bool
    _attr_assumed_state: bool
    _attr_device_info: Any
    _attr_unique_id: Any
    _attr_name: Any
    def __init__(self, uuid: str, device: Union[Remote, Climate], lookin_data: LookinData) -> None: ...
    async def _async_send_command(self, command: str) -> None: ...

class LookinCoordinatorEntity(LookinDeviceMixIn, LookinEntityMixIn, CoordinatorEntity):
    _attr_should_poll: bool
    _attr_assumed_state: bool
    _attr_device_info: Any
    _attr_unique_id: Any
    _attr_name: Any
    def __init__(self, coordinator: DataUpdateCoordinator, uuid: str, device: Union[Remote, Climate], lookin_data: LookinData) -> None: ...
    async def _async_send_command(self, command: str) -> None: ...

class LookinPowerEntity(LookinEntity):
    _power_on_command: Any
    _power_off_command: Any
    def __init__(self, uuid: str, device: Union[Remote, Climate], lookin_data: LookinData) -> None: ...
