from . import LovelaceData as LovelaceData
from _typeshed import Incomplete
from homeassistant.const import CONF_ICON as CONF_ICON, CONF_MODE as CONF_MODE, CONF_TYPE as CONF_TYPE, CONF_URL as CONF_URL, EVENT_LOVELACE_UPDATED as EVENT_LOVELACE_UPDATED
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import VolDictType as VolDictType
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
LOVELACE_DATA: HassKey[LovelaceData]
DEFAULT_ICON: str
MODE_YAML: str
MODE_STORAGE: str
MODE_AUTO: str
LOVELACE_CONFIG_FILE: str
CONF_ALLOW_SINGLE_WORD: str
CONF_URL_PATH: str
CONF_RESOURCE_TYPE_WS: str
RESOURCE_TYPES: Incomplete
RESOURCE_FIELDS: Incomplete
RESOURCE_SCHEMA: Incomplete
RESOURCE_CREATE_FIELDS: VolDictType
RESOURCE_UPDATE_FIELDS: VolDictType
SERVICE_RELOAD_RESOURCES: str
RESOURCE_RELOAD_SERVICE_SCHEMA: Incomplete
CONF_TITLE: str
CONF_REQUIRE_ADMIN: str
CONF_SHOW_IN_SIDEBAR: str
DASHBOARD_BASE_CREATE_FIELDS: VolDictType
DASHBOARD_BASE_UPDATE_FIELDS: VolDictType
STORAGE_DASHBOARD_CREATE_FIELDS: VolDictType
STORAGE_DASHBOARD_UPDATE_FIELDS = DASHBOARD_BASE_UPDATE_FIELDS

class ConfigNotFound(HomeAssistantError): ...
