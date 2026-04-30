from .const import BINARY_SENSOR_OFF_ID as BINARY_SENSOR_OFF_ID, BINARY_SENSOR_ON_ID as BINARY_SENSOR_ON_ID
from .entity import VictronBaseEntity as VictronBaseEntity
from .hub import VictronGxConfigEntry as VictronGxConfigEntry
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any
from victron_mqtt import Device as VictronVenusDevice, Metric as VictronVenusMetric, MetricType

PARALLEL_UPDATES: int
METRIC_TYPE_TO_DEVICE_CLASS: dict[MetricType, BinarySensorDeviceClass]

async def async_setup_entry(hass: HomeAssistant, config_entry: VictronGxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VictronBinarySensor(VictronBaseEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, device: VictronVenusDevice, metric: VictronVenusMetric, device_info: DeviceInfo, installation_id: str) -> None: ...
    @callback
    def _on_update_cb(self, value: Any) -> None: ...
    @staticmethod
    def convert_metric_value_to_is_on(value: Any) -> bool | None: ...
