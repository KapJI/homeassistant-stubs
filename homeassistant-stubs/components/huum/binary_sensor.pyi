from .coordinator import HuumConfigEntry as HuumConfigEntry, HuumDataUpdateCoordinator as HuumDataUpdateCoordinator
from .entity import HuumBaseEntity as HuumBaseEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: HuumConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HuumDoorSensor(HuumBaseEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: HuumDataUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
