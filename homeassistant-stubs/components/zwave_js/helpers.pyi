from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.model.node import Node as ZwaveNode

def get_unique_id(home_id: str, value_id: str) -> str: ...
def get_device_id(client: ZwaveClient, node: ZwaveNode) -> tuple[str, str]: ...
def get_home_and_node_id_from_device_id(device_id: tuple[str, str]) -> list[str]: ...
def async_get_node_from_device_id(hass: HomeAssistant, device_id: str) -> ZwaveNode: ...
def async_get_node_from_entity_id(hass: HomeAssistant, entity_id: str) -> ZwaveNode: ...
