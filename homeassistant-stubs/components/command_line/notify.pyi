from .const import CONF_COMMAND_TIMEOUT as CONF_COMMAND_TIMEOUT, DOMAIN as DOMAIN, LOGGER as LOGGER
from .utils import async_run_shell_command as async_run_shell_command, create_platform_yaml_not_supported_issue as create_platform_yaml_not_supported_issue, render_template_args as render_template_args
from _typeshed import Incomplete
from homeassistant.components.notify import BaseNotificationService as BaseNotificationService
from homeassistant.const import CONF_COMMAND as CONF_COMMAND, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, override

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> CommandLineNotificationService | None: ...

class CommandLineNotificationService(BaseNotificationService):
    command: Incomplete
    _timeout: Incomplete
    _name: Incomplete
    def __init__(self, command: str, timeout: int, name: str) -> None: ...
    @override
    async def async_send_message(self, message: str = '', **kwargs: Any) -> None: ...
