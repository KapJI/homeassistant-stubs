import voluptuous as vol
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from zwave_js_server.model.node import Node as Node
from zwave_js_server.model.value import ConfigurationValue

NODE_STATUSES: Incomplete
CONF_SUBTYPE: str
CONF_VALUE_ID: str
VALUE_ID_REGEX: str

def get_config_parameter_value_schema(node: Node, value_id: str) -> Union[vol.Schema, None]: ...
def generate_config_parameter_subtype(config_value: ConfigurationValue) -> str: ...
def async_bypass_dynamic_config_validation(hass: HomeAssistant, device_id: str) -> bool: ...
