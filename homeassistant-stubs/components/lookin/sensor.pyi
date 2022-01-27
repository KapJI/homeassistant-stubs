from .const import DOMAIN as DOMAIN
from .entity import LookinDeviceCoordinatorEntity as LookinDeviceCoordinatorEntity
from .models import LookinData as LookinData
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

LOGGER: Any
SENSOR_TYPES: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LookinSensorEntity(LookinDeviceCoordinatorEntity, SensorEntity):
    entity_description: Any
    _attr_name: Any
    _attr_native_value: Any
    _attr_unique_id: Any
    def __init__(self, description: SensorEntityDescription, lookin_data: LookinData) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
