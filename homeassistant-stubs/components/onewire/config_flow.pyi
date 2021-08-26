from .const import CONF_MOUNT_DIR as CONF_MOUNT_DIR, CONF_TYPE_OWSERVER as CONF_TYPE_OWSERVER, CONF_TYPE_SYSBUS as CONF_TYPE_SYSBUS, DEFAULT_OWSERVER_HOST as DEFAULT_OWSERVER_HOST, DEFAULT_OWSERVER_PORT as DEFAULT_OWSERVER_PORT, DEFAULT_SYSBUS_MOUNT_DIR as DEFAULT_SYSBUS_MOUNT_DIR, DOMAIN as DOMAIN
from .onewirehub import CannotConnect as CannotConnect, InvalidPath as InvalidPath, OneWireHub as OneWireHub
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

DATA_SCHEMA_USER: Any
DATA_SCHEMA_OWSERVER: Any
DATA_SCHEMA_MOUNTDIR: Any

async def validate_input_owserver(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...
async def validate_input_mount_dir(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...

class OneWireFlowHandler(ConfigFlow):
    VERSION: int
    onewire_config: Any
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_owserver(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_mount_dir(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
