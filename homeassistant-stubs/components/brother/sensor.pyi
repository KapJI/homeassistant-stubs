from . import BrotherDataUpdateCoordinator as BrotherDataUpdateCoordinator
from .const import DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from brother import BrotherSensors as BrotherSensors
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

ATTR_COUNTER: str
ATTR_REMAINING_PAGES: str
UNIT_PAGES: str
_LOGGER: Incomplete

class BrotherSensorRequiredKeysMixin:
    value: Callable[[BrotherSensors], StateType | datetime]
    def __init__(self, value) -> None: ...

class BrotherSensorEntityDescription(SensorEntityDescription, BrotherSensorRequiredKeysMixin):
    def __init__(self, value, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

SENSOR_TYPES: tuple[BrotherSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BrotherPrinterSensor(CoordinatorEntity[BrotherDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: BrotherSensorEntityDescription
    _attr_device_info: Incomplete
    _attr_native_value: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BrotherDataUpdateCoordinator, description: BrotherSensorEntityDescription, device_info: DeviceInfo) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
