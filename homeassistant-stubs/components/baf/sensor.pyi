from .const import DOMAIN as DOMAIN
from .entity import BAFEntity as BAFEntity
from .models import BAFData as BAFData
from _typeshed import Incomplete
from aiobafi6 import Device as Device
from collections.abc import Callable as Callable
from homeassistant import config_entries as config_entries
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

class BAFSensorDescriptionMixin:
    value_fn: Callable[[Device], Union[int, float, str, None]]
    def __init__(self, value_fn) -> None: ...

class BAFSensorDescription(SensorEntityDescription, BAFSensorDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

AUTO_COMFORT_SENSORS: Incomplete
DEFINED_ONLY_SENSORS: Incomplete
FAN_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BAFSensor(BAFEntity, SensorEntity):
    entity_description: BAFSensorDescription
    _attr_unique_id: Incomplete
    def __init__(self, device: Device, description: BAFSensorDescription) -> None: ...
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...
