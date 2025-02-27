from .coordinator import LockData as LockData, SchlageConfigEntry as SchlageConfigEntry, SchlageDataUpdateCoordinator as SchlageDataUpdateCoordinator
from .entity import SchlageEntity as SchlageEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_SENSOR_DESCRIPTIONS: list[SensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: SchlageConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SchlageBatterySensor(SchlageEntity, SensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, coordinator: SchlageDataUpdateCoordinator, description: SensorEntityDescription, device_id: str) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
