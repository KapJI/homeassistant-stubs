from .const import DOMAIN as DOMAIN
from .model import DoorDevice as DoorDevice
from AIOAladdinConnect import AladdinConnectClient
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

class AccSensorEntityDescriptionMixin:
    value_fn: Callable
    def __init__(self, value_fn) -> None: ...

class AccSensorEntityDescription(SensorEntityDescription, AccSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

SENSORS: tuple[AccSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AladdinConnectSensor(SensorEntity):
    entity_description: AccSensorEntityDescription
    _attr_has_entity_name: bool
    _device_id: Incomplete
    _number: Incomplete
    _acc: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, acc: AladdinConnectClient, device: DoorDevice, description: AccSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
