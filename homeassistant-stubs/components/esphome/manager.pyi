from .bluetooth import async_connect_scanner as async_connect_scanner
from .const import CONF_ALLOW_SERVICE_CALLS as CONF_ALLOW_SERVICE_CALLS, CONF_DEVICE_NAME as CONF_DEVICE_NAME, DEFAULT_ALLOW_SERVICE_CALLS as DEFAULT_ALLOW_SERVICE_CALLS, DEFAULT_URL as DEFAULT_URL, DOMAIN as DOMAIN, PROJECT_URLS as PROJECT_URLS, STABLE_BLE_VERSION as STABLE_BLE_VERSION, STABLE_BLE_VERSION_STR as STABLE_BLE_VERSION_STR
from .dashboard import async_get_dashboard as async_get_dashboard
from .domain_data import DomainData as DomainData
from .entry_data import RuntimeEntryData as RuntimeEntryData
from .voice_assistant import VoiceAssistantUDPServer as VoiceAssistantUDPServer
from _typeshed import Incomplete
from aioesphomeapi import APIClient as APIClient, APIVersion as APIVersion, DeviceInfo as EsphomeDeviceInfo, HomeassistantServiceCall as HomeassistantServiceCall, UserService as UserService, VoiceAssistantAudioSettings as VoiceAssistantAudioSettings, VoiceAssistantEventType as VoiceAssistantEventType
from homeassistant.components import tag as tag, zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_MODE as CONF_MODE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, State as State, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers import template as template
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.event import EventStateChangedData as EventStateChangedData, async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.service import async_set_service_schema as async_set_service_schema
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import EventType as EventType
from typing import Any, NamedTuple

_LOGGER: Incomplete

def _async_check_firmware_version(hass: HomeAssistant, device_info: EsphomeDeviceInfo, api_version: APIVersion) -> None: ...
def _async_check_using_api_password(hass: HomeAssistant, device_info: EsphomeDeviceInfo, has_password: bool) -> None: ...

class ESPHomeManager:
    __slots__: Incomplete
    hass: Incomplete
    host: Incomplete
    password: Incomplete
    entry: Incomplete
    cli: Incomplete
    device_id: Incomplete
    domain_data: Incomplete
    voice_assistant_udp_server: Incomplete
    reconnect_logic: Incomplete
    zeroconf_instance: Incomplete
    entry_data: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, host: str, password: str | None, cli: APIClient, zeroconf_instance: zeroconf.HaZeroconf, domain_data: DomainData, entry_data: RuntimeEntryData) -> None: ...
    async def on_stop(self, event: Event) -> None: ...
    @property
    def services_issue(self) -> str: ...
    def async_on_service_call(self, service: HomeassistantServiceCall) -> None: ...
    async def _send_home_assistant_state(self, entity_id: str, attribute: str | None, state: State | None) -> None: ...
    def async_on_state_subscription(self, entity_id: str, attribute: str | None = ...) -> None: ...
    def _handle_pipeline_event(self, event_type: VoiceAssistantEventType, data: dict[str, str] | None) -> None: ...
    def _handle_pipeline_finished(self) -> None: ...
    async def _handle_pipeline_start(self, conversation_id: str, flags: int, audio_settings: VoiceAssistantAudioSettings) -> int | None: ...
    async def _handle_pipeline_stop(self) -> None: ...
    async def on_connect(self) -> None: ...
    async def on_disconnect(self, expected_disconnect: bool) -> None: ...
    async def on_connect_error(self, err: Exception) -> None: ...
    async def async_start(self) -> None: ...

def _async_setup_device_registry(hass: HomeAssistant, entry: ConfigEntry, entry_data: RuntimeEntryData) -> str: ...

class ServiceMetadata(NamedTuple):
    validator: Any
    example: str
    selector: dict[str, Any]
    description: str | None

ARG_TYPE_METADATA: Incomplete

async def _register_service(hass: HomeAssistant, entry_data: RuntimeEntryData, service: UserService) -> None: ...
async def _setup_services(hass: HomeAssistant, entry_data: RuntimeEntryData, services: list[UserService]) -> None: ...
async def cleanup_instance(hass: HomeAssistant, entry: ConfigEntry) -> RuntimeEntryData: ...
