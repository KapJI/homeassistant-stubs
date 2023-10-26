import httpx
import voluptuous as vol
from . import subscription as subscription
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS
from .debug_info import log_messages as log_messages
from .mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MessageCallbackType as MessageCallbackType, MqttValueTemplate as MqttValueTemplate, ReceiveMessage as ReceiveMessage
from .util import get_mqtt_data as get_mqtt_data, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import image as image
from homeassistant.components.image import DEFAULT_CONTENT_TYPE as DEFAULT_CONTENT_TYPE, ImageEntity as ImageEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
CONF_CONTENT_TYPE: str
CONF_IMAGE_ENCODING: str
CONF_IMAGE_TOPIC: str
CONF_URL_TEMPLATE: str
CONF_URL_TOPIC: str
DEFAULT_NAME: str
GET_IMAGE_TIMEOUT: int

def validate_topic_required(config: ConfigType) -> ConfigType: ...

PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttImage(MqttEntity, ImageEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format: str
    _last_image: bytes | None
    _client: httpx.AsyncClient
    _url_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    _topic: dict[str, Any]
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None) -> None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_content_type: Incomplete
    _attr_image_url: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_image_last_updated: Incomplete
    _cached_image: Incomplete
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_image(self) -> bytes | None: ...
