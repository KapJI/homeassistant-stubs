from . import AmcrestDevice as AmcrestDevice
from .const import BINARY_SENSOR_SCAN_INTERVAL_SECS as BINARY_SENSOR_SCAN_INTERVAL_SECS, DATA_AMCREST as DATA_AMCREST, DEVICES as DEVICES, SERVICE_EVENT as SERVICE_EVENT, SERVICE_UPDATE as SERVICE_UPDATE
from .helpers import log_update_error as log_update_error, service_signal as service_signal
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, DEVICE_CLASS_CONNECTIVITY as DEVICE_CLASS_CONNECTIVITY, DEVICE_CLASS_MOTION as DEVICE_CLASS_MOTION, DEVICE_CLASS_SOUND as DEVICE_CLASS_SOUND
from homeassistant.const import CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import Throttle as Throttle
from typing import Any

class AmcrestSensorEntityDescription(BinarySensorEntityDescription):
    event_code: Union[str, None]
    should_poll: bool

_LOGGER: Any
SCAN_INTERVAL: Any
_ONLINE_SCAN_INTERVAL: Any
_AUDIO_DETECTED_KEY: str
_AUDIO_DETECTED_POLLED_KEY: str
_AUDIO_DETECTED_NAME: str
_AUDIO_DETECTED_EVENT_CODE: str
_CROSSLINE_DETECTED_KEY: str
_CROSSLINE_DETECTED_POLLED_KEY: str
_CROSSLINE_DETECTED_NAME: str
_CROSSLINE_DETECTED_EVENT_CODE: str
_MOTION_DETECTED_KEY: str
_MOTION_DETECTED_POLLED_KEY: str
_MOTION_DETECTED_NAME: str
_MOTION_DETECTED_EVENT_CODE: str
_ONLINE_KEY: str
BINARY_SENSORS: tuple[AmcrestSensorEntityDescription, ...]
BINARY_SENSOR_KEYS: Any
_EXCLUSIVE_OPTIONS: Any
_UPDATE_MSG: str

def check_binary_sensors(value: list[str]) -> list[str]: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class AmcrestBinarySensor(BinarySensorEntity):
    _signal_name: Any
    _api: Any
    _channel: Any
    entity_description: Any
    _attr_name: Any
    _attr_should_poll: Any
    _unsub_dispatcher: Any
    def __init__(self, name: str, device: AmcrestDevice, entity_description: AmcrestSensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    def update(self) -> None: ...
    _attr_is_on: Any
    def _update_online(self) -> None: ...
    def _update_others(self) -> None: ...
    _attr_unique_id: Any
    def _update_unique_id(self) -> None: ...
    async def async_on_demand_update(self) -> None: ...
    def async_event_received(self, state: bool) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
