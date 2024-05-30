from .client import MqttClientSetup as MqttClientSetup
from .const import ATTR_PAYLOAD as ATTR_PAYLOAD, ATTR_QOS as ATTR_QOS, ATTR_RETAIN as ATTR_RETAIN, ATTR_TOPIC as ATTR_TOPIC, CONF_BIRTH_MESSAGE as CONF_BIRTH_MESSAGE, CONF_BROKER as CONF_BROKER, CONF_CERTIFICATE as CONF_CERTIFICATE, CONF_CLIENT_CERT as CONF_CLIENT_CERT, CONF_CLIENT_KEY as CONF_CLIENT_KEY, CONF_DISCOVERY_PREFIX as CONF_DISCOVERY_PREFIX, CONF_KEEPALIVE as CONF_KEEPALIVE, CONF_TLS_INSECURE as CONF_TLS_INSECURE, CONF_TRANSPORT as CONF_TRANSPORT, CONF_WILL_MESSAGE as CONF_WILL_MESSAGE, CONF_WS_HEADERS as CONF_WS_HEADERS, CONF_WS_PATH as CONF_WS_PATH, DEFAULT_BIRTH as DEFAULT_BIRTH, DEFAULT_DISCOVERY as DEFAULT_DISCOVERY, DEFAULT_ENCODING as DEFAULT_ENCODING, DEFAULT_KEEPALIVE as DEFAULT_KEEPALIVE, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_PREFIX as DEFAULT_PREFIX, DEFAULT_PROTOCOL as DEFAULT_PROTOCOL, DEFAULT_TRANSPORT as DEFAULT_TRANSPORT, DEFAULT_WILL as DEFAULT_WILL, DEFAULT_WS_PATH as DEFAULT_WS_PATH, DOMAIN as DOMAIN, SUPPORTED_PROTOCOLS as SUPPORTED_PROTOCOLS, TRANSPORT_TCP as TRANSPORT_TCP, TRANSPORT_WEBSOCKETS as TRANSPORT_WEBSOCKETS
from .util import async_create_certificate_temp_files as async_create_certificate_temp_files, get_file_path as get_file_path, valid_birth_will as valid_birth_will, valid_publish_topic as valid_publish_topic
from _typeshed import Incomplete
from collections import OrderedDict
from collections.abc import Callable as Callable, Mapping
from homeassistant.components.file_upload import process_uploaded_file as process_uploaded_file
from homeassistant.components.hassio import HassioServiceInfo as HassioServiceInfo
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_DISCOVERY as CONF_DISCOVERY, CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PAYLOAD as CONF_PAYLOAD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.helpers.json import json_dumps as json_dumps
from homeassistant.helpers.selector import BooleanSelector as BooleanSelector, FileSelector as FileSelector, FileSelectorConfig as FileSelectorConfig, NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads
from types import MappingProxyType
from typing import Any

MQTT_TIMEOUT: int
ADVANCED_OPTIONS: str
SET_CA_CERT: str
SET_CLIENT_CERT: str
BOOLEAN_SELECTOR: Incomplete
TEXT_SELECTOR: Incomplete
PUBLISH_TOPIC_SELECTOR: Incomplete
PORT_SELECTOR: Incomplete
PASSWORD_SELECTOR: Incomplete
QOS_SELECTOR: Incomplete
KEEPALIVE_SELECTOR: Incomplete
PROTOCOL_SELECTOR: Incomplete
SUPPORTED_TRANSPORTS: Incomplete
TRANSPORT_SELECTOR: Incomplete
WS_HEADERS_SELECTOR: Incomplete
CA_VERIFICATION_MODES: Incomplete
BROKER_VERIFICATION_SELECTOR: Incomplete
CA_CERT_UPLOAD_SELECTOR: Incomplete
CERT_UPLOAD_SELECTOR: Incomplete
KEY_UPLOAD_SELECTOR: Incomplete
REAUTH_SCHEMA: Incomplete
PWD_NOT_CHANGED: str

def update_password_from_user_input(entry_password: str | None, user_input: dict[str, Any]) -> dict[str, Any]: ...

class FlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    entry: ConfigEntry | None
    _hassio_discovery: dict[str, Any] | None
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> MQTTOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_broker(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> ConfigFlowResult: ...
    async def async_step_hassio_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class MQTTOptionsFlowHandler(OptionsFlow):
    config_entry: Incomplete
    broker_config: Incomplete
    options: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: None = None) -> ConfigFlowResult: ...
    async def async_step_broker(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_options(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

async def async_get_broker_settings(flow: ConfigFlow | OptionsFlow, fields: OrderedDict[Any, Any], entry_config: MappingProxyType[str, Any] | None, user_input: dict[str, Any] | None, validated_user_input: dict[str, Any], errors: dict[str, str]) -> bool: ...
def try_connection(user_input: dict[str, Any]) -> bool: ...
def check_certicate_chain() -> str | None: ...
