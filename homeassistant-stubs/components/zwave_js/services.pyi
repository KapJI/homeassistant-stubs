from . import const as const
from .config_validation import BITMASK_SCHEMA as BITMASK_SCHEMA, VALUE_SCHEMA as VALUE_SCHEMA
from .helpers import async_get_node_from_device_id as async_get_node_from_device_id, async_get_node_from_entity_id as async_get_node_from_entity_id, async_get_nodes_from_area_id as async_get_nodes_from_area_id, async_get_nodes_from_targets as async_get_nodes_from_targets, get_value_id_from_unique_id as get_value_id_from_unique_id
from _typeshed import Incomplete
from collections.abc import Collection, Sequence
from homeassistant.const import ATTR_AREA_ID as ATTR_AREA_ID, ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import device_registry as dr, entity_registry as er
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.group import expand_entity_ids as expand_entity_ids
from typing import Any
from typing_extensions import Generator
from zwave_js_server.const import CommandClass

_LOGGER: Incomplete
_NodeOrEndpointType: Incomplete

def parameter_name_does_not_need_bitmask(val: dict[str, int | str | list[str]]) -> dict[str, int | str | list[str]]: ...
def check_base_2(val: int) -> int: ...
def broadcast_command(val: dict[str, Any]) -> dict[str, Any]: ...
def get_valid_responses_from_results(zwave_objects: Sequence[_T], results: Sequence[Any]) -> Generator[tuple[_T, Any]]: ...
def raise_exceptions_from_results(zwave_objects: Sequence[_NodeOrEndpointType], results: Sequence[Any]) -> None: ...
async def _async_invoke_cc_api(nodes_or_endpoints: Collection[_NodeOrEndpointType], command_class: CommandClass, method_name: str, *args: Any) -> None: ...

class ZWaveServices:
    _hass: Incomplete
    _ent_reg: Incomplete
    _dev_reg: Incomplete
    def __init__(self, hass: HomeAssistant, ent_reg: er.EntityRegistry, dev_reg: dr.DeviceRegistry) -> None: ...
    def async_register(self) -> None: ...
    async def async_set_config_parameter(self, service: ServiceCall) -> None: ...
    async def async_bulk_set_partial_config_parameters(self, service: ServiceCall) -> None: ...
    async def async_poll_value(self, service: ServiceCall) -> None: ...
    async def async_set_value(self, service: ServiceCall) -> None: ...
    async def async_multicast_set_value(self, service: ServiceCall) -> None: ...
    async def async_ping(self, service: ServiceCall) -> None: ...
    async def async_invoke_cc_api(self, service: ServiceCall) -> None: ...
    async def async_refresh_notifications(self, service: ServiceCall) -> None: ...
