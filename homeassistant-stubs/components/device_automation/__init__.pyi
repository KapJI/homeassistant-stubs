from .exceptions import DeviceNotFound as DeviceNotFound, InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from collections.abc import Iterable, Mapping
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, bind_hass as bind_hass
from homeassistant.requirements import async_get_integration_with_requirements as async_get_integration_with_requirements
from types import ModuleType
from typing import Any

DOMAIN: str
DEVICE_TRIGGER_BASE_SCHEMA: Any
TYPES: Any

async def async_get_device_automations(hass: HomeAssistant, automation_type: str, device_ids: Union[Iterable[str], None] = ...) -> Mapping[str, Any]: ...
async def async_setup(hass, config): ...
async def async_get_device_automation_platform(hass: HomeAssistant, domain: str, automation_type: str) -> ModuleType: ...
async def _async_get_device_automations_from_domain(hass, domain, automation_type, device_ids, return_exceptions): ...
async def _async_get_device_automations(hass: HomeAssistant, automation_type: str, device_ids: Union[Iterable[str], None]) -> Mapping[str, list[dict[str, Any]]]: ...
async def _async_get_device_automation_capabilities(hass, automation_type, automation): ...
def handle_device_errors(func): ...
async def websocket_device_automation_list_actions(hass, connection, msg) -> None: ...
async def websocket_device_automation_list_conditions(hass, connection, msg) -> None: ...
async def websocket_device_automation_list_triggers(hass, connection, msg) -> None: ...
async def websocket_device_automation_get_action_capabilities(hass, connection, msg) -> None: ...
async def websocket_device_automation_get_condition_capabilities(hass, connection, msg) -> None: ...
async def websocket_device_automation_get_trigger_capabilities(hass, connection, msg) -> None: ...
