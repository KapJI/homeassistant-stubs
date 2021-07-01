from homeassistant import config_entries as config_entries
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType, UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from typing import Any, Awaitable, Callable, Union

DiscoveryFunctionType = Callable[[HomeAssistant], Union[Awaitable[bool], bool]]
_LOGGER: Any

class DiscoveryFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _domain: Any
    _title: Any
    _discovery_function: Any
    def __init__(self, domain: str, title: str, discovery_function: DiscoveryFunctionType) -> None: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_discovery(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async_step_zeroconf: Any
    async_step_ssdp: Any
    async_step_mqtt: Any
    async_step_homekit: Any
    async_step_dhcp: Any
    async def async_step_import(self, _: Union[dict[str, Any], None]) -> FlowResult: ...

def register_discovery_flow(domain: str, title: str, discovery_function: DiscoveryFunctionType, connection_class: Union[str, UndefinedType] = ...) -> None: ...

class WebhookFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _domain: Any
    _title: Any
    _description_placeholder: Any
    _allow_multiple: Any
    def __init__(self, domain: str, title: str, description_placeholder: dict, allow_multiple: bool) -> None: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

def register_webhook_flow(domain: str, title: str, description_placeholder: dict, allow_multiple: bool = ...) -> None: ...
async def webhook_async_remove_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> None: ...
