import voluptuous as vol
from typing import Any
from zwave_js_server.model.node import Node as Node
from zwave_js_server.model.value import ConfigurationValue

NODE_STATUSES: Any
CONF_SUBTYPE: str
CONF_VALUE_ID: str
VALUE_ID_REGEX: str

def get_config_parameter_value_schema(node: Node, value_id: str) -> Union[vol.Schema, None]: ...
def generate_config_parameter_subtype(config_value: ConfigurationValue) -> str: ...
