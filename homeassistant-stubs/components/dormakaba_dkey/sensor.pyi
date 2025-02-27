from .coordinator import DormakabaDkeyConfigEntry as DormakabaDkeyConfigEntry, DormakabaDkeyCoordinator as DormakabaDkeyCoordinator
from .entity import DormakabaDkeyEntity as DormakabaDkeyEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

BINARY_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: DormakabaDkeyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DormakabaDkeySensor(DormakabaDkeyEntity, SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DormakabaDkeyCoordinator, description: SensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
