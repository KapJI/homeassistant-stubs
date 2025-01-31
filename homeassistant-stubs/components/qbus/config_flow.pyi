from .const import CONF_SERIAL_NUMBER as CONF_SERIAL_NUMBER, DOMAIN as DOMAIN
from .coordinator import QbusConfigCoordinator as QbusConfigCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.helpers.service_info.mqtt import MqttServiceInfo as MqttServiceInfo
from qbusmqttapi.discovery import QbusMqttDevice as QbusMqttDevice
from typing import Any

_LOGGER: Incomplete

class QbusFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _message_factory: Incomplete
    _topic_factory: Incomplete
    _gateway_topic: Incomplete
    _config_topic: Incomplete
    _device_topic: Incomplete
    _device: QbusMqttDevice | None
    def __init__(self) -> None: ...
    async def async_step_mqtt(self, discovery_info: MqttServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_handle_gateway_topic(self, discovery_info: MqttServiceInfo) -> ConfigFlowResult: ...
    async def _async_handle_config_topic(self, discovery_info: MqttServiceInfo) -> ConfigFlowResult: ...
    async def _async_handle_device_topic(self, discovery_info: MqttServiceInfo) -> ConfigFlowResult: ...
