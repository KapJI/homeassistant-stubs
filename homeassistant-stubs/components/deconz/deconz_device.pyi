from .gateway import DeconzGateway as DeconzGateway
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import CONNECTION_ZIGBEE as CONNECTION_ZIGBEE
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from pydeconz.models.group import Group as PydeconzGroup
from pydeconz.models.light import LightBase as PydeconzLightBase
from pydeconz.models.scene import Scene as PydeconzScene
from pydeconz.models.sensor import SensorBase as PydeconzSensorBase
from typing import TypeVar, Union

_DeviceT = TypeVar('_DeviceT', bound=Union[PydeconzGroup, PydeconzLightBase, PydeconzSensorBase, PydeconzScene])

class DeconzBase:
    unique_id_suffix: Union[str, None]
    _device: Incomplete
    gateway: Incomplete
    def __init__(self, device: _DeviceT, gateway: DeconzGateway) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def serial(self) -> Union[str, None]: ...
    @property
    def device_info(self) -> Union[DeviceInfo, None]: ...

class DeconzDevice(DeconzBase[_DeviceT], Entity):
    _attr_should_poll: bool
    _name_suffix: Union[str, None]
    _update_key: Union[str, None]
    _update_keys: Union[set[str], None]
    TYPE: str
    _attr_name: Incomplete
    def __init__(self, device: _DeviceT, gateway: DeconzGateway) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def async_update_connection_state(self) -> None: ...
    def async_update_callback(self) -> None: ...
    @property
    def available(self) -> bool: ...

class DeconzSceneMixin(DeconzDevice[PydeconzScene]):
    _attr_has_entity_name: bool
    group: Incomplete
    _attr_name: Incomplete
    _group_identifier: Incomplete
    def __init__(self, device: PydeconzScene, gateway: DeconzGateway) -> None: ...
    def get_device_identifier(self) -> str: ...
    def get_parent_identifier(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
