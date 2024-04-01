from .const import CONF_ACTIONS as CONF_ACTIONS, CONF_ACTION_BACKGROUND_COLOR as CONF_ACTION_BACKGROUND_COLOR, CONF_ACTION_ICON as CONF_ACTION_ICON, CONF_ACTION_ICON_COLOR as CONF_ACTION_ICON_COLOR, CONF_ACTION_ICON_ICON as CONF_ACTION_ICON_ICON, CONF_ACTION_LABEL as CONF_ACTION_LABEL, CONF_ACTION_LABEL_COLOR as CONF_ACTION_LABEL_COLOR, CONF_ACTION_LABEL_TEXT as CONF_ACTION_LABEL_TEXT, CONF_ACTION_NAME as CONF_ACTION_NAME, CONF_ACTION_SHOW_IN_CARPLAY as CONF_ACTION_SHOW_IN_CARPLAY, CONF_ACTION_SHOW_IN_WATCH as CONF_ACTION_SHOW_IN_WATCH, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiohttp import web as web
from homeassistant import config_entries as config_entries
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.json import save_json as save_json
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.json import load_json_object as load_json_object
from typing import Any

CONF_PUSH: str
CONF_PUSH_CATEGORIES: str
CONF_PUSH_CATEGORIES_NAME: str
CONF_PUSH_CATEGORIES_IDENTIFIER: str
CONF_PUSH_CATEGORIES_ACTIONS: str
CONF_PUSH_ACTIONS_IDENTIFIER: str
CONF_PUSH_ACTIONS_TITLE: str
CONF_PUSH_ACTIONS_ACTIVATION_MODE: str
CONF_PUSH_ACTIONS_AUTHENTICATION_REQUIRED: str
CONF_PUSH_ACTIONS_DESTRUCTIVE: str
CONF_PUSH_ACTIONS_BEHAVIOR: str
CONF_PUSH_ACTIONS_CONTEXT: str
CONF_PUSH_ACTIONS_TEXT_INPUT_BUTTON_TITLE: str
CONF_PUSH_ACTIONS_TEXT_INPUT_PLACEHOLDER: str
CONF_USER: str
ATTR_FOREGROUND: str
ATTR_BACKGROUND: str
ACTIVATION_MODES: Incomplete
ATTR_DEFAULT_BEHAVIOR: str
ATTR_TEXT_INPUT_BEHAVIOR: str
BEHAVIORS: Incomplete
ATTR_LAST_SEEN_AT: str
ATTR_DEVICE: str
ATTR_PUSH_TOKEN: str
ATTR_APP: str
ATTR_PERMISSIONS: str
ATTR_PUSH_ID: str
ATTR_DEVICE_ID: str
ATTR_PUSH_SOUNDS: str
ATTR_BATTERY: str
ATTR_DEVICE_NAME: str
ATTR_DEVICE_LOCALIZED_MODEL: str
ATTR_DEVICE_MODEL: str
ATTR_DEVICE_PERMANENT_ID: str
ATTR_DEVICE_SYSTEM_VERSION: str
ATTR_DEVICE_TYPE: str
ATTR_DEVICE_SYSTEM_NAME: str
ATTR_APP_BUNDLE_IDENTIFIER: str
ATTR_APP_BUILD_NUMBER: str
ATTR_APP_VERSION_NUMBER: str
ATTR_LOCATION_PERMISSION: str
ATTR_NOTIFICATIONS_PERMISSION: str
PERMISSIONS: Incomplete
ATTR_BATTERY_STATE: str
ATTR_BATTERY_LEVEL: str
ATTR_BATTERY_STATE_UNPLUGGED: str
ATTR_BATTERY_STATE_CHARGING: str
ATTR_BATTERY_STATE_FULL: str
ATTR_BATTERY_STATE_UNKNOWN: str
BATTERY_STATES: Incomplete
ATTR_DEVICES: str
PUSH_ACTION_SCHEMA: Incomplete
PUSH_ACTION_LIST_SCHEMA: Incomplete
PUSH_CATEGORY_SCHEMA: Incomplete
PUSH_CATEGORY_LIST_SCHEMA: Incomplete
ACTION_SCHEMA: Incomplete
ACTION_LIST_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
IDENTIFY_DEVICE_SCHEMA: Incomplete
IDENTIFY_DEVICE_SCHEMA_CONTAINER: Incomplete
IDENTIFY_APP_SCHEMA: Incomplete
IDENTIFY_APP_SCHEMA_CONTAINER: Incomplete
IDENTIFY_BATTERY_SCHEMA: Incomplete
IDENTIFY_BATTERY_SCHEMA_CONTAINER: Incomplete
IDENTIFY_SCHEMA: Incomplete
CONFIGURATION_FILE: str
PLATFORMS: Incomplete

def devices_with_push(hass: HomeAssistant) -> dict[str, str]: ...
def enabled_push_ids(hass: HomeAssistant) -> list[str]: ...
def devices(hass: HomeAssistant) -> dict[str, dict[str, Any]]: ...
def device_name_for_push_id(hass: HomeAssistant, push_id: str) -> str | None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool: ...

class iOSPushConfigView(HomeAssistantView):
    url: str
    name: str
    push_config: Incomplete
    def __init__(self, push_config: dict[str, Any]) -> None: ...
    def get(self, request: web.Request) -> web.Response: ...

class iOSConfigView(HomeAssistantView):
    url: str
    name: str
    config: Incomplete
    def __init__(self, config: dict[str, Any]) -> None: ...
    def get(self, request: web.Request) -> web.Response: ...

class iOSIdentifyDeviceView(HomeAssistantView):
    url: str
    name: str
    _config_path: Incomplete
    def __init__(self, config_path: str) -> None: ...
    async def post(self, request: web.Request) -> web.Response: ...
