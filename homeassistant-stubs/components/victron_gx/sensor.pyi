from .entity import VictronBaseEntity as VictronBaseEntity
from .hub import VictronGxConfigEntry as VictronGxConfigEntry
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any
from victron_mqtt import Device as VictronVenusDevice, Metric as VictronVenusMetric, MetricNature, MetricType

PARALLEL_UPDATES: int
METRIC_TYPE_TO_DEVICE_CLASS: dict[MetricType, SensorDeviceClass]
METRIC_NATURE_TO_STATE_CLASS: dict[MetricNature, SensorStateClass]

async def async_setup_entry(hass: HomeAssistant, config_entry: VictronGxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VictronSensor(VictronBaseEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_options: Incomplete
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, device: VictronVenusDevice, metric: VictronVenusMetric, device_info: DeviceInfo, installation_id: str) -> None: ...
    @callback
    def _on_update_cb(self, value: Any) -> None: ...
    @staticmethod
    def _normalize_value(value: Any) -> Any: ...
