import dataclasses
from _typeshed import Incomplete
from collections.abc import AsyncGenerator, Awaitable, Callable as Callable
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.frame import ReportBehavior as ReportBehavior, report_usage as report_usage
from homeassistant.helpers.integration_platform import LazyIntegrationPlatforms as LazyIntegrationPlatforms
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Protocol

_LOGGER: Incomplete
DOMAIN: str
INFO_CALLBACK_TIMEOUT: int
CONFIG_SCHEMA: Incomplete
DATA_SYSTEM_HEALTH_PLATFORMS: HassKey[LazyIntegrationPlatforms[SystemHealthRegistration]]

class SystemHealthProtocol(Protocol):
    def async_register(self, hass: HomeAssistant, register: SystemHealthRegistration) -> None: ...

@callback
def async_register_info(hass: HomeAssistant, domain: str, info_callback: Callable[[HomeAssistant], Awaitable[dict]]) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@callback
def _process_system_health_platform(hass: HomeAssistant, integration_domain: str, platform: SystemHealthProtocol) -> SystemHealthRegistration: ...
async def get_integration_info(hass: HomeAssistant, registration: SystemHealthRegistration) -> dict[str, Any]: ...
async def _registered_domain_data(hass: HomeAssistant) -> AsyncGenerator[tuple[str, dict[str, Any]]]: ...
async def get_info(hass: HomeAssistant) -> dict[str, dict[str, str]]: ...
@callback
def _format_value(val: Any) -> Any: ...
@websocket_api.async_response
async def handle_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

@dataclasses.dataclass(slots=True)
class SystemHealthRegistration:
    hass: HomeAssistant
    domain: str
    info_callback: Callable[[HomeAssistant], Awaitable[dict]] | None = ...
    manage_url: str | None = ...
    @callback
    def async_register_info(self, info_callback: Callable[[HomeAssistant], Awaitable[dict]], manage_url: str | None = None) -> None: ...

async def async_check_can_reach_url(hass: HomeAssistant, url: str, more_info: str | None = None) -> str | dict[str, str]: ...
