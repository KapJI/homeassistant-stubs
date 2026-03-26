from .coordinator import HuumConfigEntry as HuumConfigEntry, HuumDataUpdateCoordinator as HuumDataUpdateCoordinator
from .entity import HuumBaseEntity as HuumBaseEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: HuumConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HuumTemperatureSensor(HuumBaseEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: HuumDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> int | None: ...
