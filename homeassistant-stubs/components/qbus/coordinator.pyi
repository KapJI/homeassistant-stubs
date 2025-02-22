from .const import CONF_SERIAL_NUMBER as CONF_SERIAL_NUMBER, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from _typeshed import Incomplete
from homeassistant.components.mqtt import ReceiveMessage as ReceiveMessage, async_wait_for_mqtt_client as async_wait_for_mqtt_client
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.hass_dict import HassKey as HassKey
from qbusmqttapi.discovery import QbusDiscovery as QbusDiscovery, QbusMqttDevice as QbusMqttDevice, QbusMqttOutput

_LOGGER: Incomplete
type QbusConfigEntry = ConfigEntry[QbusControllerCoordinator]
QBUS_KEY: HassKey[QbusConfigCoordinator]

class QbusControllerCoordinator(DataUpdateCoordinator[list[QbusMqttOutput]]):
    _STATE_REQUEST_DELAY: int
    config_entry: QbusConfigEntry
    _message_factory: Incomplete
    _topic_factory: Incomplete
    _controller_activated: bool
    _subscribed_to_controller_state: bool
    _controller: QbusMqttDevice | None
    def __init__(self, hass: HomeAssistant, entry: QbusConfigEntry) -> None: ...
    async def _async_update_data(self) -> list[QbusMqttOutput]: ...
    def shutdown(self, event: Event | None = None) -> None: ...
    async def async_update_controller_config(self, config: QbusDiscovery) -> None: ...
    def _update_device_info(self) -> None: ...
    async def _async_subscribe_to_controller_state(self) -> None: ...
    async def _controller_state_received(self, msg: ReceiveMessage) -> None: ...
    def _request_entity_states(self) -> None: ...
    def _request_controller_state(self) -> None: ...

class QbusConfigCoordinator:
    _qbus_config: QbusDiscovery | None
    _hass: Incomplete
    _message_factory: Incomplete
    _topic_factory: Incomplete
    _cleanup_callbacks: list[CALLBACK_TYPE]
    def __init__(self, hass: HomeAssistant) -> None: ...
    @classmethod
    def get_or_create(cls, hass: HomeAssistant) -> QbusConfigCoordinator: ...
    def shutdown(self, event: Event | None = None) -> None: ...
    async def async_subscribe_to_config(self) -> None: ...
    async def async_get_or_request_config(self) -> QbusDiscovery | None: ...
    def store_config(self, config: QbusDiscovery) -> None: ...
    async def _config_received(self, msg: ReceiveMessage) -> None: ...
