from .bluetooth import async_connect_scanner as async_connect_scanner
from .const import DOMAIN as DOMAIN
from .dashboard import async_get_dashboard as async_get_dashboard
from .domain_data import DomainData as DomainData
from .entry_data import RuntimeEntryData as RuntimeEntryData
from _typeshed import Incomplete
from aioesphomeapi import APIClient, APIIntEnum, APIVersion as APIVersion, DeviceInfo as EsphomeDeviceInfo, EntityCategory as EsphomeEntityCategory, EntityInfo, EntityState, HomeassistantServiceCall as HomeassistantServiceCall, UserService as UserService
from collections.abc import Callable as Callable
from homeassistant.components import tag as tag, zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_HOST as CONF_HOST, CONF_MODE as CONF_MODE, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, State as State, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers import template as template
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.service import async_set_service_schema as async_set_service_schema
from homeassistant.helpers.template import Template as Template
from typing import Any, NamedTuple, TypeVar, overload

CONF_DEVICE_NAME: str
CONF_NOISE_PSK: str
_LOGGER: Incomplete
_R = TypeVar('_R')
STABLE_BLE_VERSION_STR: str
STABLE_BLE_VERSION: Incomplete
PROJECT_URLS: Incomplete
DEFAULT_URL: Incomplete

def _async_check_firmware_version(hass: HomeAssistant, device_info: EsphomeDeviceInfo) -> None: ...
def _async_check_using_api_password(hass: HomeAssistant, device_info: EsphomeDeviceInfo, has_password: bool) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _async_setup_device_registry(hass: HomeAssistant, entry: ConfigEntry, device_info: EsphomeDeviceInfo) -> str: ...

class ServiceMetadata(NamedTuple):
    validator: Any
    example: str
    selector: dict[str, Any]
    description: Union[str, None]

ARG_TYPE_METADATA: Incomplete

async def _register_service(hass: HomeAssistant, entry_data: RuntimeEntryData, service: UserService) -> None: ...
async def _setup_services(hass: HomeAssistant, entry_data: RuntimeEntryData, services: list[UserService]) -> None: ...
async def _cleanup_instance(hass: HomeAssistant, entry: ConfigEntry) -> RuntimeEntryData: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
_InfoT = TypeVar('_InfoT', bound=EntityInfo)
_EntityT = TypeVar('_EntityT', bound='EsphomeEntity[Any,Any]')
_StateT = TypeVar('_StateT', bound=EntityState)

async def platform_async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback, *, component_key: str, info_type: type[_InfoT], entity_type: type[_EntityT], state_type: type[_StateT]) -> None: ...
def esphome_state_property(func: Callable[[_EntityT], _R]) -> Callable[[_EntityT], Union[_R, None]]: ...
_EnumT = TypeVar('_EnumT', bound=APIIntEnum)
_ValT = TypeVar('_ValT')

class EsphomeEnumMapper:
    _mapping: Incomplete
    _inverse: Incomplete
    def __init__(self, mapping: dict[_EnumT, _ValT]) -> None: ...
    @overload
    def from_esphome(self, value: _EnumT) -> _ValT: ...
    @overload
    def from_esphome(self, value: Union[_EnumT, None]) -> Union[_ValT, None]: ...
    def from_hass(self, value: _ValT) -> _EnumT: ...

ICON_SCHEMA: Incomplete
ENTITY_CATEGORIES: EsphomeEnumMapper[EsphomeEntityCategory, Union[EntityCategory, None]]

class EsphomeEntity(Entity):
    _attr_should_poll: bool
    _entry_data: Incomplete
    _component_key: Incomplete
    _key: Incomplete
    _state_type: Incomplete
    _attr_has_entity_name: bool
    def __init__(self, entry_data: RuntimeEntryData, component_key: str, key: int, state_type: type[_StateT]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _on_state_update(self) -> None: ...
    def _on_device_update(self) -> None: ...
    @property
    def _entry_id(self) -> str: ...
    @property
    def _api_version(self) -> APIVersion: ...
    @property
    def _static_info(self) -> _InfoT: ...
    @property
    def _device_info(self) -> EsphomeDeviceInfo: ...
    @property
    def _client(self) -> APIClient: ...
    @property
    def _state(self) -> _StateT: ...
    @property
    def _has_state(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @property
    def unique_id(self) -> Union[str, None]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def name(self) -> str: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def entity_category(self) -> Union[EntityCategory, None]: ...
