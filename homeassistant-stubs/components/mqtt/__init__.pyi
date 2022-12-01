from . import debug_info as debug_info, discovery as discovery
from .client import MQTT as MQTT, async_publish as async_publish, async_subscribe as async_subscribe, publish as publish, subscribe as subscribe
from .config_integration import CONFIG_SCHEMA_BASE as CONFIG_SCHEMA_BASE, CONFIG_SCHEMA_ENTRY as CONFIG_SCHEMA_ENTRY, DEFAULT_VALUES as DEFAULT_VALUES, DEPRECATED_CERTIFICATE_CONFIG_KEYS as DEPRECATED_CERTIFICATE_CONFIG_KEYS, DEPRECATED_CONFIG_KEYS as DEPRECATED_CONFIG_KEYS
from .const import ATTR_PAYLOAD as ATTR_PAYLOAD, ATTR_QOS as ATTR_QOS, ATTR_RETAIN as ATTR_RETAIN, ATTR_TOPIC as ATTR_TOPIC, CONF_BIRTH_MESSAGE as CONF_BIRTH_MESSAGE, CONF_BROKER as CONF_BROKER, CONF_CERTIFICATE as CONF_CERTIFICATE, CONF_CLIENT_CERT as CONF_CLIENT_CERT, CONF_CLIENT_KEY as CONF_CLIENT_KEY, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_DISCOVERY_PREFIX as CONF_DISCOVERY_PREFIX, CONF_KEEPALIVE as CONF_KEEPALIVE, CONF_QOS as CONF_QOS, CONF_STATE_TOPIC as CONF_STATE_TOPIC, CONF_TLS_INSECURE as CONF_TLS_INSECURE, CONF_TLS_VERSION as CONF_TLS_VERSION, CONF_TOPIC as CONF_TOPIC, CONF_TRANSPORT as CONF_TRANSPORT, CONF_WILL_MESSAGE as CONF_WILL_MESSAGE, CONF_WS_HEADERS as CONF_WS_HEADERS, CONF_WS_PATH as CONF_WS_PATH, DATA_MQTT as DATA_MQTT, DEFAULT_ENCODING as DEFAULT_ENCODING, DEFAULT_QOS as DEFAULT_QOS, DEFAULT_RETAIN as DEFAULT_RETAIN, DOMAIN as DOMAIN, MQTT_CONNECTED as MQTT_CONNECTED, MQTT_DISCONNECTED as MQTT_DISCONNECTED, PLATFORMS as PLATFORMS, RELOADABLE_PLATFORMS as RELOADABLE_PLATFORMS
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage, ReceivePayloadType as ReceivePayloadType
from .util import async_create_certificate_temp_files as async_create_certificate_temp_files, get_mqtt_data as get_mqtt_data, migrate_certificate_file_to_content as migrate_certificate_file_to_content, mqtt_config_entry_enabled as mqtt_config_entry_enabled, valid_publish_topic as valid_publish_topic, valid_qos_schema as valid_qos_schema, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from collections.abc import Callable
from homeassistant import config_entries as config_entries
from homeassistant.components import websocket_api as websocket_api
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_DISCOVERY as CONF_DISCOVERY, CONF_PASSWORD as CONF_PASSWORD, CONF_PAYLOAD as CONF_PAYLOAD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HassJob as HassJob, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError, Unauthorized as Unauthorized
from homeassistant.helpers import discovery_flow as discovery_flow, event as event, template as template
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import async_get_platforms as async_get_platforms
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.reload import async_integration_yaml_config as async_integration_yaml_config, async_reload_integration_platforms as async_reload_integration_platforms
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
SERVICE_PUBLISH: str
SERVICE_DUMP: str
MANDATORY_DEFAULT_VALUES: Incomplete
ATTR_TOPIC_TEMPLATE: str
ATTR_PAYLOAD_TEMPLATE: str
MAX_RECONNECT_WAIT: int
CONNECTION_SUCCESS: str
CONNECTION_FAILED: str
CONNECTION_FAILED_RECOVERABLE: str
CONFIG_ENTRY_CONFIG_KEYS: Incomplete
CONFIG_SCHEMA: Incomplete
MQTT_PUBLISH_SCHEMA: Incomplete

async def _async_setup_discovery(hass: HomeAssistant, conf: ConfigType, config_entry: ConfigEntry) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _filter_entry_config(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def _async_merge_basic_config(hass: HomeAssistant, entry: ConfigEntry, yaml_config: dict[str, Any]) -> None: ...
def _merge_extended_config(entry: ConfigEntry, conf: ConfigType) -> dict[str, Any]: ...
async def _async_config_entry_updated(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_fetch_config(hass: HomeAssistant, entry: ConfigEntry) -> Union[dict[str, Any], None]: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_reload_manual_mqtt_items(hass: HomeAssistant) -> None: ...
def websocket_mqtt_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def websocket_subscribe(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
ConnectionStatusCallback = Callable[[bool], None]

def async_subscribe_connection_status(hass: HomeAssistant, connection_status_callback: ConnectionStatusCallback) -> Callable[[], None]: ...
def is_connected(hass: HomeAssistant) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
