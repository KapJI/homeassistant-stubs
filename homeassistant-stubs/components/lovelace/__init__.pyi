from . import dashboard as dashboard, resources as resources, websocket as websocket
from .const import CONF_ALLOW_SINGLE_WORD as CONF_ALLOW_SINGLE_WORD, CONF_ICON as CONF_ICON, CONF_REQUIRE_ADMIN as CONF_REQUIRE_ADMIN, CONF_SHOW_IN_SIDEBAR as CONF_SHOW_IN_SIDEBAR, CONF_TITLE as CONF_TITLE, CONF_URL_PATH as CONF_URL_PATH, DASHBOARD_BASE_CREATE_FIELDS as DASHBOARD_BASE_CREATE_FIELDS, DEFAULT_ICON as DEFAULT_ICON, DOMAIN as DOMAIN, EVENT_LOVELACE_UPDATED as EVENT_LOVELACE_UPDATED, LOVELACE_DATA as LOVELACE_DATA, MODE_STORAGE as MODE_STORAGE, MODE_YAML as MODE_YAML, RESOURCE_CREATE_FIELDS as RESOURCE_CREATE_FIELDS, RESOURCE_RELOAD_SERVICE_SCHEMA as RESOURCE_RELOAD_SERVICE_SCHEMA, RESOURCE_SCHEMA as RESOURCE_SCHEMA, RESOURCE_UPDATE_FIELDS as RESOURCE_UPDATE_FIELDS, SERVICE_RELOAD_RESOURCES as SERVICE_RELOAD_RESOURCES, STORAGE_DASHBOARD_CREATE_FIELDS as STORAGE_DASHBOARD_CREATE_FIELDS, STORAGE_DASHBOARD_UPDATE_FIELDS as STORAGE_DASHBOARD_UPDATE_FIELDS
from .system_health import system_health_info as system_health_info
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components import frontend as frontend, onboarding as onboarding, websocket_api as websocket_api
from homeassistant.config import async_hass_config_yaml as async_hass_config_yaml, async_process_component_and_handle_errors as async_process_component_and_handle_errors
from homeassistant.const import CONF_FILENAME as CONF_FILENAME, CONF_MODE as CONF_MODE, CONF_RESOURCES as CONF_RESOURCES
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import collection as collection
from homeassistant.helpers.frame import report_usage as report_usage
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service
from homeassistant.helpers.translation import async_get_translations as async_get_translations
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import async_get_integration as async_get_integration
from homeassistant.util import slugify as slugify
from typing import Any

_LOGGER: Incomplete

def _validate_url_slug(value: Any) -> str: ...

CONF_DASHBOARDS: str
YAML_DASHBOARD_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

@dataclass
class LovelaceData:
    mode: str
    dashboards: dict[str | None, dashboard.LovelaceConfig]
    resources: resources.ResourceYAMLCollection | resources.ResourceStorageCollection
    yaml_dashboards: dict[str | None, ConfigType]
    def __getitem__(self, name: str) -> Any: ...
    def get(self, name: str, default: Any = None) -> Any: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def create_yaml_resource_col(hass: HomeAssistant, yaml_resources: list[ConfigType] | None) -> resources.ResourceYAMLCollection: ...
@callback
def _register_panel(hass: HomeAssistant, url_path: str | None, mode: str, config: dict, update: bool) -> None: ...
async def _create_map_dashboard(hass: HomeAssistant, dashboards_collection: dashboard.DashboardsCollection) -> None: ...
