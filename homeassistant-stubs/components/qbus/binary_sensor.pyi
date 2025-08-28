from .const import DOMAIN as DOMAIN
from .coordinator import QbusConfigEntry as QbusConfigEntry
from .entity import QbusEntity as QbusEntity, create_device_identifier as create_device_identifier, create_unique_id as create_unique_id, determine_new_outputs as determine_new_outputs
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from qbusmqttapi.discovery import QbusMqttDevice as QbusMqttDevice, QbusMqttOutput as QbusMqttOutput
from qbusmqttapi.state import QbusMqttDeviceState as QbusMqttDeviceState, QbusMqttWeatherState

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class QbusWeatherDescription(BinarySensorEntityDescription):
    property: str

_WEATHER_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: QbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class QbusWeatherBinarySensor(QbusEntity, BinarySensorEntity):
    _state_cls = QbusMqttWeatherState
    entity_description: QbusWeatherDescription
    def __init__(self, mqtt_output: QbusMqttOutput, description: QbusWeatherDescription) -> None: ...
    _attr_is_on: Incomplete
    async def _handle_state_received(self, state: QbusMqttWeatherState) -> None: ...

class QbusControllerConnectedBinarySensor(BinarySensorEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_device_class: Incomplete
    _controller: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, controller: QbusMqttDevice) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _state_received(self, state: QbusMqttDeviceState) -> None: ...
