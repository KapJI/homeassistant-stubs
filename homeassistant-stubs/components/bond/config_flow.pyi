from .const import DOMAIN as DOMAIN
from .utils import BondHub as BondHub
from homeassistant import config_entries as config_entries, exceptions as exceptions
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, HTTP_UNAUTHORIZED as HTTP_UNAUTHORIZED
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

USER_SCHEMA: Any
DISCOVERY_SCHEMA: Any
TOKEN_SCHEMA: Any

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int = ...
    CONNECTION_CLASS: Any = ...
    def __init__(self) -> None: ...
    async def async_step_zeroconf(self, discovery_info: DiscoveryInfoType) -> dict[str, Any]: ...
    async def async_step_confirm(self, user_input: Union[dict[str, Any], None]=...) -> dict[str, Any]: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None]=...) -> dict[str, Any]: ...

class InputValidationError(exceptions.HomeAssistantError):
    base: Any = ...
    def __init__(self, base: str) -> None: ...