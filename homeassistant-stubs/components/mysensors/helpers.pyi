import voluptuous as vol
from .const import ATTR_DEVICES as ATTR_DEVICES, ATTR_GATEWAY_ID as ATTR_GATEWAY_ID, DOMAIN as DOMAIN, DevId as DevId, FLAT_PLATFORM_TYPES as FLAT_PLATFORM_TYPES, GatewayId as GatewayId, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY, MYSENSORS_ON_UNLOAD as MYSENSORS_ON_UNLOAD, SensorType as SensorType, TYPE_TO_PLATFORMS as TYPE_TO_PLATFORMS, ValueType as ValueType
from collections import defaultdict
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.util.decorator import Registry as Registry
from mysensors import BaseAsyncGateway as BaseAsyncGateway, Message as Message
from mysensors.sensor import ChildSensor as ChildSensor
from typing import Any, Callable

_LOGGER: Any
SCHEMAS: Any

def on_unload(hass: HomeAssistant, gateway_id: GatewayId, fnct: Callable) -> None: ...
def discover_mysensors_platform(hass: HomeAssistant, gateway_id: GatewayId, platform: str, new_devices: list[DevId]) -> None: ...
def default_schema(gateway: BaseAsyncGateway, child: ChildSensor, value_type_name: ValueType) -> vol.Schema: ...
def light_dimmer_schema(gateway: BaseAsyncGateway, child: ChildSensor, value_type_name: ValueType) -> vol.Schema: ...
def light_percentage_schema(gateway: BaseAsyncGateway, child: ChildSensor, value_type_name: ValueType) -> vol.Schema: ...
def light_rgb_schema(gateway: BaseAsyncGateway, child: ChildSensor, value_type_name: ValueType) -> vol.Schema: ...
def light_rgbw_schema(gateway: BaseAsyncGateway, child: ChildSensor, value_type_name: ValueType) -> vol.Schema: ...
def switch_ir_send_schema(gateway: BaseAsyncGateway, child: ChildSensor, value_type_name: ValueType) -> vol.Schema: ...
def get_child_schema(gateway: BaseAsyncGateway, child: ChildSensor, value_type_name: ValueType, schema: dict) -> vol.Schema: ...
def invalid_msg(gateway: BaseAsyncGateway, child: ChildSensor, value_type_name: ValueType) -> str: ...
def validate_set_msg(gateway_id: GatewayId, msg: Message) -> dict[str, list[DevId]]: ...
def validate_node(gateway: BaseAsyncGateway, node_id: int) -> bool: ...
def validate_child(gateway_id: GatewayId, gateway: BaseAsyncGateway, node_id: int, child: ChildSensor, value_type: Union[int, None] = ...) -> defaultdict[str, list[DevId]]: ...