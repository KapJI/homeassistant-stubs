from .const import ANALYTICS_ENDPOINT_URL as ANALYTICS_ENDPOINT_URL, ANALYTICS_ENDPOINT_URL_DEV as ANALYTICS_ENDPOINT_URL_DEV, ATTR_ADDONS as ATTR_ADDONS, ATTR_ADDON_COUNT as ATTR_ADDON_COUNT, ATTR_ARCH as ATTR_ARCH, ATTR_AUTOMATION_COUNT as ATTR_AUTOMATION_COUNT, ATTR_AUTO_UPDATE as ATTR_AUTO_UPDATE, ATTR_BASE as ATTR_BASE, ATTR_BOARD as ATTR_BOARD, ATTR_CERTIFICATE as ATTR_CERTIFICATE, ATTR_CONFIGURED as ATTR_CONFIGURED, ATTR_CUSTOM_INTEGRATIONS as ATTR_CUSTOM_INTEGRATIONS, ATTR_DIAGNOSTICS as ATTR_DIAGNOSTICS, ATTR_ENERGY as ATTR_ENERGY, ATTR_ENGINE as ATTR_ENGINE, ATTR_HEALTHY as ATTR_HEALTHY, ATTR_INTEGRATIONS as ATTR_INTEGRATIONS, ATTR_INTEGRATION_COUNT as ATTR_INTEGRATION_COUNT, ATTR_OPERATING_SYSTEM as ATTR_OPERATING_SYSTEM, ATTR_PROTECTED as ATTR_PROTECTED, ATTR_RECORDER as ATTR_RECORDER, ATTR_SLUG as ATTR_SLUG, ATTR_STATE_COUNT as ATTR_STATE_COUNT, ATTR_STATISTICS as ATTR_STATISTICS, ATTR_SUPERVISOR as ATTR_SUPERVISOR, ATTR_SUPPORTED as ATTR_SUPPORTED, ATTR_USAGE as ATTR_USAGE, ATTR_USER_COUNT as ATTR_USER_COUNT, ATTR_UUID as ATTR_UUID, ATTR_VERSION as ATTR_VERSION, DOMAIN as DOMAIN, LOGGER as LOGGER, PREFERENCE_SCHEMA as PREFERENCE_SCHEMA, STORAGE_KEY as STORAGE_KEY, STORAGE_VERSION as STORAGE_VERSION
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable, Iterable, Mapping
from dataclasses import dataclass, field
from datetime import datetime
from homeassistant.components import hassio as hassio
from homeassistant.components.api import ATTR_INSTALLATION_TYPE as ATTR_INSTALLATION_TYPE
from homeassistant.config_entries import SOURCE_IGNORE as SOURCE_IGNORE
from homeassistant.const import ATTR_ASSUMED_STATE as ATTR_ASSUMED_STATE, ATTR_DOMAIN as ATTR_DOMAIN, BASE_PLATFORMS as BASE_PLATFORMS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.hassio import is_hassio as is_hassio
from homeassistant.helpers.singleton import singleton as singleton
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.system_info import async_get_system_info as async_get_system_info
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED
from homeassistant.loader import Integration as Integration, IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration, async_get_integrations as async_get_integrations
from homeassistant.setup import async_get_loaded_integrations as async_get_loaded_integrations
from typing import Any, Protocol

DATA_ANALYTICS_MODIFIERS: str
type AnalyticsModifier = Callable[[HomeAssistant, AnalyticsInput], Awaitable[AnalyticsModifications]]

def _async_get_modifiers(hass: HomeAssistant) -> dict[str, AnalyticsModifier | None]: ...

@dataclass
class AnalyticsInput:
    device_ids: Iterable[str] = field(default_factory=list)
    entity_ids: Iterable[str] = field(default_factory=list)

@dataclass
class AnalyticsModifications:
    remove: bool = ...
    devices: Mapping[str, DeviceAnalyticsModifications] | None = ...
    entities: Mapping[str, EntityAnalyticsModifications] | None = ...

@dataclass
class DeviceAnalyticsModifications:
    remove: bool = ...

@dataclass
class EntityAnalyticsModifications:
    remove: bool = ...

class AnalyticsPlatformProtocol(Protocol):
    async def async_modify_analytics(self, hass: HomeAssistant, analytics_input: AnalyticsInput) -> AnalyticsModifications: ...

async def _async_get_analytics_platform(hass: HomeAssistant, domain: str) -> AnalyticsPlatformProtocol | None: ...
async def _async_get_modifier(hass: HomeAssistant, domain: str) -> AnalyticsModifier | None: ...
def gen_uuid() -> str: ...

@dataclass
class AnalyticsData:
    onboarded: bool
    preferences: dict[str, bool]
    uuid: str | None
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AnalyticsData: ...

class Analytics:
    hass: HomeAssistant
    session: Incomplete
    _data: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @property
    def preferences(self) -> dict: ...
    @property
    def onboarded(self) -> bool: ...
    @property
    def uuid(self) -> str | None: ...
    @property
    def endpoint(self) -> str: ...
    @property
    def supervisor(self) -> bool: ...
    async def load(self) -> None: ...
    async def save_preferences(self, preferences: dict) -> None: ...
    async def send_analytics(self, _: datetime | None = None) -> None: ...
    @callback
    def _async_should_report_integration(self, integration: Integration, yaml_domains: set[str], entity_registry_platforms: set[str]) -> bool: ...

def _domains_from_yaml_config(yaml_configuration: dict[str, Any]) -> set[str]: ...

DEFAULT_ANALYTICS_CONFIG: Incomplete
DEFAULT_DEVICE_ANALYTICS_CONFIG: Incomplete
DEFAULT_ENTITY_ANALYTICS_CONFIG: Incomplete

async def async_devices_payload(hass: HomeAssistant) -> dict: ...
