import asyncio
from .addon import AddonError as AddonError, AddonManager as AddonManager, AddonState as AddonState, get_addon_manager as get_addon_manager
from .api import async_register_api as async_register_api
from .const import ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_COMMAND_CLASS_NAME as ATTR_COMMAND_CLASS_NAME, ATTR_DATA_TYPE as ATTR_DATA_TYPE, ATTR_ENDPOINT as ATTR_ENDPOINT, ATTR_EVENT as ATTR_EVENT, ATTR_EVENT_DATA as ATTR_EVENT_DATA, ATTR_EVENT_LABEL as ATTR_EVENT_LABEL, ATTR_EVENT_TYPE as ATTR_EVENT_TYPE, ATTR_HOME_ID as ATTR_HOME_ID, ATTR_LABEL as ATTR_LABEL, ATTR_NODE_ID as ATTR_NODE_ID, ATTR_PARAMETERS as ATTR_PARAMETERS, ATTR_PROPERTY as ATTR_PROPERTY, ATTR_PROPERTY_KEY as ATTR_PROPERTY_KEY, ATTR_PROPERTY_KEY_NAME as ATTR_PROPERTY_KEY_NAME, ATTR_PROPERTY_NAME as ATTR_PROPERTY_NAME, ATTR_TYPE as ATTR_TYPE, ATTR_VALUE as ATTR_VALUE, ATTR_VALUE_RAW as ATTR_VALUE_RAW, CONF_ADDON_DEVICE as CONF_ADDON_DEVICE, CONF_ADDON_NETWORK_KEY as CONF_ADDON_NETWORK_KEY, CONF_DATA_COLLECTION_OPTED_IN as CONF_DATA_COLLECTION_OPTED_IN, CONF_INTEGRATION_CREATED_ADDON as CONF_INTEGRATION_CREATED_ADDON, CONF_NETWORK_KEY as CONF_NETWORK_KEY, CONF_USB_PATH as CONF_USB_PATH, CONF_USE_ADDON as CONF_USE_ADDON, DATA_CLIENT as DATA_CLIENT, DATA_PLATFORM_SETUP as DATA_PLATFORM_SETUP, DOMAIN as DOMAIN, EVENT_DEVICE_ADDED_TO_REGISTRY as EVENT_DEVICE_ADDED_TO_REGISTRY, LOGGER as LOGGER, ZWAVE_JS_NOTIFICATION_EVENT as ZWAVE_JS_NOTIFICATION_EVENT, ZWAVE_JS_VALUE_NOTIFICATION_EVENT as ZWAVE_JS_VALUE_NOTIFICATION_EVENT, ZWAVE_JS_VALUE_UPDATED_EVENT as ZWAVE_JS_VALUE_UPDATED_EVENT
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo, async_discover_values as async_discover_values
from .helpers import async_enable_statistics as async_enable_statistics, get_device_id as get_device_id, get_unique_id as get_unique_id
from .migrate import async_migrate_discovered_value as async_migrate_discovered_value
from .services import ZWaveServices as ZWaveServices
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_DOMAIN as ATTR_DOMAIN, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_URL as CONF_URL, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as device_registry, entity_registry as entity_registry
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.model.node import Node as ZwaveNode
from zwave_js_server.model.notification import NotificationNotification as NotificationNotification
from zwave_js_server.model.value import Value as Value, ValueNotification as ValueNotification

CONNECT_TIMEOUT: int
DATA_CLIENT_LISTEN_TASK: str
DATA_START_PLATFORM_TASK: str
DATA_CONNECT_FAILED_LOGGED: str
DATA_INVALID_SERVER_VERSION_LOGGED: str

async def async_setup(hass: HomeAssistant, config: dict) -> bool: ...
def register_node_in_dev_reg(hass: HomeAssistant, entry: ConfigEntry, dev_reg: device_registry.DeviceRegistry, client: ZwaveClient, node: ZwaveNode) -> device_registry.DeviceEntry: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def client_listen(hass: HomeAssistant, entry: ConfigEntry, client: ZwaveClient, driver_ready: asyncio.Event) -> None: ...
async def disconnect_client(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_ensure_addon_running(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
def async_ensure_addon_updated(hass: HomeAssistant) -> None: ...
