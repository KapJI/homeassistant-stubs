from .bluetooth import async_connect_scanner as async_connect_scanner
from .const import CONF_ALLOW_SERVICE_CALLS as CONF_ALLOW_SERVICE_CALLS, DEFAULT_ALLOW_SERVICE_CALLS as DEFAULT_ALLOW_SERVICE_CALLS, DOMAIN as DOMAIN
from .dashboard import async_get_dashboard as async_get_dashboard
from .domain_data import DomainData as DomainData
from .entry_data import RuntimeEntryData as RuntimeEntryData
from .voice_assistant import VoiceAssistantUDPServer as VoiceAssistantUDPServer
from _typeshed import Incomplete
from aioesphomeapi import APIVersion as APIVersion, DeviceInfo as EsphomeDeviceInfo, HomeassistantServiceCall as HomeassistantServiceCall, UserService as UserService, VoiceAssistantEventType as VoiceAssistantEventType
from homeassistant.components import tag as tag, zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_HOST as CONF_HOST, CONF_MODE as CONF_MODE, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, State as State, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers import template as template
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.service import async_set_service_schema as async_set_service_schema
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, NamedTuple, TypeVar

CONF_DEVICE_NAME: str
CONF_NOISE_PSK: str
_LOGGER: Incomplete
_R = TypeVar('_R')
STABLE_BLE_VERSION_STR: str
STABLE_BLE_VERSION: Incomplete
PROJECT_URLS: Incomplete
DEFAULT_URL: Incomplete
CONFIG_SCHEMA: Incomplete

def _async_check_firmware_version(hass: HomeAssistant, device_info: EsphomeDeviceInfo, api_version: APIVersion) -> None: ...
def _async_check_using_api_password(hass: HomeAssistant, device_info: EsphomeDeviceInfo, has_password: bool) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _async_setup_device_registry(hass: HomeAssistant, entry: ConfigEntry, device_info: EsphomeDeviceInfo) -> str: ...

class ServiceMetadata(NamedTuple):
    validator: Any
    example: str
    selector: dict[str, Any]
    description: str | None

ARG_TYPE_METADATA: Incomplete

async def _register_service(hass: HomeAssistant, entry_data: RuntimeEntryData, service: UserService) -> None: ...
async def _setup_services(hass: HomeAssistant, entry_data: RuntimeEntryData, services: list[UserService]) -> None: ...
async def _cleanup_instance(hass: HomeAssistant, entry: ConfigEntry) -> RuntimeEntryData: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
