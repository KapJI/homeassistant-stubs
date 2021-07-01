from .const import ATTR_ENABLED_BY_DEFAULT as ATTR_ENABLED_BY_DEFAULT, ATTR_ENTRY_TYPE as ATTR_ENTRY_TYPE, DOMAIN as DOMAIN, ENTRY_TYPE_SERVICE as ENTRY_TYPE_SERVICE, SENSORS as SENSORS, SERVICES as SERVICES
from .models import AmbeeSensor as AmbeeSensor
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ICON as ATTR_ICON, ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_NAME as ATTR_NAME, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AmbeeSensorEntity(CoordinatorEntity, SensorEntity):
    _sensor_key: Any
    _service_key: Any
    entity_id: Any
    _attr_device_class: Any
    _attr_entity_registry_enabled_default: Any
    _attr_icon: Any
    _attr_name: Any
    _attr_state_class: Any
    _attr_unique_id: Any
    _attr_unit_of_measurement: Any
    _attr_device_info: Any
    def __init__(self, coordinator: DataUpdateCoordinator, entry_id: str, sensor_key: str, sensor: AmbeeSensor, service_key: str, service: str) -> None: ...
    @property
    def state(self) -> StateType: ...
