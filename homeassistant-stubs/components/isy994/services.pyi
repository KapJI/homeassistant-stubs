from .const import DOMAIN as DOMAIN, ISY994_ISY as ISY994_ISY, _LOGGER as _LOGGER
from .util import unique_ids_for_config_entry_id as unique_ids_for_config_entry_id
from _typeshed import Incomplete
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_COMMAND as CONF_COMMAND, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import async_get_platforms as async_get_platforms
from homeassistant.helpers.service import entity_service_call as entity_service_call
from typing import Any

SERVICE_SYSTEM_QUERY: str
SERVICE_SET_VARIABLE: str
SERVICE_SEND_PROGRAM_COMMAND: str
SERVICE_RUN_NETWORK_RESOURCE: str
SERVICE_CLEANUP: str
INTEGRATION_SERVICES: Incomplete
SERVICE_SEND_RAW_NODE_COMMAND: str
SERVICE_SEND_NODE_COMMAND: str
SERVICE_GET_ZWAVE_PARAMETER: str
SERVICE_SET_ZWAVE_PARAMETER: str
SERVICE_RENAME_NODE: str
SERVICE_SET_ON_LEVEL: str
SERVICE_SET_RAMP_RATE: str
CONF_PARAMETER: str
CONF_PARAMETERS: str
CONF_VALUE: str
CONF_INIT: str
CONF_ISY: str
CONF_SIZE: str
VALID_NODE_COMMANDS: Incomplete
VALID_PROGRAM_COMMANDS: Incomplete
VALID_PARAMETER_SIZES: Incomplete

def valid_isy_commands(value: Any) -> str: ...

SCHEMA_GROUP: str
SERVICE_SYSTEM_QUERY_SCHEMA: Incomplete
SERVICE_SET_RAMP_RATE_SCHEMA: Incomplete
SERVICE_SET_VALUE_SCHEMA: Incomplete
SERVICE_SEND_RAW_NODE_COMMAND_SCHEMA: Incomplete
SERVICE_SEND_NODE_COMMAND_SCHEMA: Incomplete
SERVICE_RENAME_NODE_SCHEMA: Incomplete
SERVICE_GET_ZWAVE_PARAMETER_SCHEMA: Incomplete
SERVICE_SET_ZWAVE_PARAMETER_SCHEMA: Incomplete
SERVICE_SET_VARIABLE_SCHEMA: Incomplete
SERVICE_SEND_PROGRAM_COMMAND_SCHEMA: Incomplete
SERVICE_RUN_NETWORK_RESOURCE_SCHEMA: Incomplete

def async_setup_services(hass: HomeAssistant) -> None: ...
def async_unload_services(hass: HomeAssistant) -> None: ...
def async_setup_light_services(hass: HomeAssistant) -> None: ...
