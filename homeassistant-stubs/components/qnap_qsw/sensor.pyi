from .const import ATTR_MAX as ATTR_MAX, DOMAIN as DOMAIN, QSW_COORD_DATA as QSW_COORD_DATA, RPM as RPM
from .coordinator import QswDataCoordinator as QswDataCoordinator
from .entity import QswEntityDescription as QswEntityDescription, QswSensorEntity as QswSensorEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DATA_BYTES as DATA_BYTES, DATA_RATE_BYTES_PER_SECOND as DATA_RATE_BYTES_PER_SECOND, TEMP_CELSIUS as TEMP_CELSIUS, TIME_SECONDS as TIME_SECONDS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Final

class QswSensorEntityDescription(SensorEntityDescription, QswEntityDescription):
    attributes: Union[dict[str, list[str]], None]
    def __init__(self, subkey, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class, attributes) -> None: ...

SENSOR_TYPES: Final[tuple[QswSensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class QswSensor(QswSensorEntity, SensorEntity):
    entity_description: QswSensorEntityDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: QswDataCoordinator, description: QswSensorEntityDescription, entry: ConfigEntry) -> None: ...
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...
