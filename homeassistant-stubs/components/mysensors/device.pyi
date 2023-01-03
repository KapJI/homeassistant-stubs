import abc
from .const import CHILD_CALLBACK as CHILD_CALLBACK, CONF_DEVICE as CONF_DEVICE, DOMAIN as DOMAIN, DevId as DevId, GatewayId as GatewayId, NODE_CALLBACK as NODE_CALLBACK, PLATFORM_TYPES as PLATFORM_TYPES, UPDATE_DELAY as UPDATE_DELAY
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, Platform as Platform, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from mysensors import BaseAsyncGateway as BaseAsyncGateway, Sensor as Sensor
from mysensors.sensor import ChildSensor as ChildSensor
from typing import Any

_LOGGER: Incomplete
ATTR_CHILD_ID: str
ATTR_DESCRIPTION: str
ATTR_DEVICE: str
ATTR_NODE_ID: str
ATTR_HEARTBEAT: str
MYSENSORS_PLATFORM_DEVICES: str

class MySensorsDevice(ABC, metaclass=abc.ABCMeta):
    hass: HomeAssistant
    gateway_id: Incomplete
    gateway: Incomplete
    node_id: Incomplete
    child_id: Incomplete
    value_type: Incomplete
    child_type: Incomplete
    _values: Incomplete
    _debouncer: Incomplete
    def __init__(self, gateway_id: GatewayId, gateway: BaseAsyncGateway, node_id: int, child_id: int, value_type: int) -> None: ...
    @property
    def dev_id(self) -> DevId: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def _node(self) -> Sensor: ...
    @property
    def _child(self) -> ChildSensor: ...
    @property
    def sketch_name(self) -> str: ...
    @property
    def sketch_version(self) -> str: ...
    @property
    def node_name(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def name(self) -> str: ...
    @property
    def _extra_attributes(self) -> dict[str, Any]: ...
    def _async_update(self) -> None: ...
    @abstractmethod
    def _async_update_callback(self) -> None: ...
    async def async_update_callback(self) -> None: ...

def get_mysensors_devices(hass: HomeAssistant, domain: Platform) -> dict[DevId, MySensorsDevice]: ...

class MySensorsEntity(MySensorsDevice, Entity):
    _attr_should_poll: bool
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def _async_update_callback(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
