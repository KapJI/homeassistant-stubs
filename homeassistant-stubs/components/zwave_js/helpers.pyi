import voluptuous as vol
from .const import ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_ENDPOINT as ATTR_ENDPOINT, ATTR_PROPERTY as ATTR_PROPERTY, ATTR_PROPERTY_KEY as ATTR_PROPERTY_KEY, CONF_DATA_COLLECTION_OPTED_IN as CONF_DATA_COLLECTION_OPTED_IN, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import device_registry as dr, entity_registry as er
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.model.node import Node as ZwaveNode
from zwave_js_server.model.value import Value as ZwaveValue

def get_value_of_zwave_value(value: Union[ZwaveValue, None]) -> Union[Any, None]: ...
async def async_enable_statistics(client: ZwaveClient) -> None: ...
def update_data_collection_preference(hass: HomeAssistant, entry: ConfigEntry, preference: bool) -> None: ...
def get_unique_id(home_id: str, value_id: str) -> str: ...
def get_device_id(client: ZwaveClient, node: ZwaveNode) -> tuple[str, str]: ...
def get_device_id_ext(client: ZwaveClient, node: ZwaveNode) -> Union[tuple[str, str], None]: ...
def get_home_and_node_id_from_device_id(device_id: tuple[str, ...]) -> list[str]: ...
def async_get_node_from_device_id(hass: HomeAssistant, device_id: str, dev_reg: Union[dr.DeviceRegistry, None] = ...) -> ZwaveNode: ...
def async_get_node_from_entity_id(hass: HomeAssistant, entity_id: str, ent_reg: Union[er.EntityRegistry, None] = ..., dev_reg: Union[dr.DeviceRegistry, None] = ...) -> ZwaveNode: ...
def async_get_nodes_from_area_id(hass: HomeAssistant, area_id: str, ent_reg: Union[er.EntityRegistry, None] = ..., dev_reg: Union[dr.DeviceRegistry, None] = ...) -> set[ZwaveNode]: ...
def get_zwave_value_from_config(node: ZwaveNode, config: ConfigType) -> ZwaveValue: ...
def async_get_node_status_sensor_entity_id(hass: HomeAssistant, device_id: str, ent_reg: Union[er.EntityRegistry, None] = ..., dev_reg: Union[dr.DeviceRegistry, None] = ...) -> str: ...
def remove_keys_with_empty_values(config: ConfigType) -> ConfigType: ...
def check_type_schema_map(schema_map: dict[str, vol.Schema]) -> Callable: ...
def copy_available_params(input_dict: dict[str, Any], output_dict: dict[str, Any], params: list[str]) -> None: ...
def async_is_device_config_entry_not_loaded(hass: HomeAssistant, device_id: str) -> bool: ...
def get_value_state_schema(value: ZwaveValue) -> Union[vol.Schema, None]: ...
