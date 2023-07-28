from . import subscription as subscription
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import ATTR_DISCOVERY_HASH as ATTR_DISCOVERY_HASH, CONF_QOS as CONF_QOS, CONF_TOPIC as CONF_TOPIC
from .discovery import MQTTDiscoveryPayload as MQTTDiscoveryPayload
from .mixins import MQTT_ENTITY_DEVICE_INFO_SCHEMA as MQTT_ENTITY_DEVICE_INFO_SCHEMA, MqttDiscoveryDeviceUpdate as MqttDiscoveryDeviceUpdate, async_handle_schema_error as async_handle_schema_error, async_setup_entry_helper as async_setup_entry_helper, send_discovery_done as send_discovery_done, update_device as update_device
from .models import MqttValueTemplate as MqttValueTemplate, ReceiveMessage as ReceiveMessage, ReceivePayloadType as ReceivePayloadType
from .subscription import EntitySubscription as EntitySubscription
from .util import get_mqtt_data as get_mqtt_data, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import tag as tag
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_PLATFORM as CONF_PLATFORM, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

LOG_NAME: str
TAG: str
PLATFORM_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
async def _async_setup_tag(hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType) -> None: ...
def async_has_tags(hass: HomeAssistant, device_id: str) -> bool: ...

class MQTTTagScanner(MqttDiscoveryDeviceUpdate):
    _value_template: Callable[[ReceivePayloadType, str], ReceivePayloadType]
    _config: Incomplete
    _config_entry: Incomplete
    device_id: Incomplete
    discovery_data: Incomplete
    hass: Incomplete
    _sub_state: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType, device_id: str | None, discovery_data: DiscoveryInfoType, config_entry: ConfigEntry) -> None: ...
    async def async_update(self, discovery_data: MQTTDiscoveryPayload) -> None: ...
    async def subscribe_topics(self) -> None: ...
    async def async_tear_down(self) -> None: ...
