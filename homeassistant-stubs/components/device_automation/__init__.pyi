from .action import DeviceAutomationActionProtocol as DeviceAutomationActionProtocol
from .condition import DeviceAutomationConditionProtocol as DeviceAutomationConditionProtocol
from .exceptions import DeviceNotFound as DeviceNotFound, InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from .trigger import DeviceAutomationTriggerProtocol as DeviceAutomationTriggerProtocol
from collections.abc import Iterable, Mapping
from enum import Enum
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, bind_hass as bind_hass
from homeassistant.requirements import async_get_integration_with_requirements as async_get_integration_with_requirements
from types import ModuleType
from typing import Any, Literal, NamedTuple, Union, overload

DeviceAutomationPlatformType = Union[ModuleType, DeviceAutomationTriggerProtocol, DeviceAutomationConditionProtocol, DeviceAutomationActionProtocol]
DOMAIN: str
DEVICE_TRIGGER_BASE_SCHEMA: Any

class DeviceAutomationDetails(NamedTuple):
    section: str
    get_automations_func: str
    get_capabilities_func: str

class DeviceAutomationType(Enum):
    TRIGGER: Any
    CONDITION: Any
    ACTION: Any

TYPES: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@overload
async def async_get_device_automation_platform(hass: HomeAssistant, domain: str, automation_type: Literal[DeviceAutomationType.TRIGGER]) -> DeviceAutomationTriggerProtocol: ...
@overload
async def async_get_device_automation_platform(hass: HomeAssistant, domain: str, automation_type: Literal[DeviceAutomationType.CONDITION]) -> DeviceAutomationConditionProtocol: ...
@overload
async def async_get_device_automation_platform(hass: HomeAssistant, domain: str, automation_type: Literal[DeviceAutomationType.ACTION]) -> DeviceAutomationActionProtocol: ...
@overload
async def async_get_device_automation_platform(hass: HomeAssistant, domain: str, automation_type: DeviceAutomationType) -> DeviceAutomationPlatformType: ...
async def _async_get_device_automations_from_domain(hass, domain, automation_type, device_ids, return_exceptions): ...
async def async_get_device_automations(hass: HomeAssistant, automation_type: DeviceAutomationType, device_ids: Union[Iterable[str], None] = ...) -> Mapping[str, list[dict[str, Any]]]: ...
async def _async_get_device_automation_capabilities(hass: HomeAssistant, automation_type: DeviceAutomationType, automation: Mapping[str, Any]) -> dict[str, Any]: ...
def handle_device_errors(func): ...
async def websocket_device_automation_list_actions(hass, connection, msg) -> None: ...
async def websocket_device_automation_list_conditions(hass, connection, msg) -> None: ...
async def websocket_device_automation_list_triggers(hass, connection, msg) -> None: ...
async def websocket_device_automation_get_action_capabilities(hass, connection, msg) -> None: ...
async def websocket_device_automation_get_condition_capabilities(hass, connection, msg) -> None: ...
async def websocket_device_automation_get_trigger_capabilities(hass, connection, msg) -> None: ...
