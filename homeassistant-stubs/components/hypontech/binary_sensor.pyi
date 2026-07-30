from .coordinator import HypontechConfigEntry as HypontechConfigEntry, HypontechDataCoordinator as HypontechDataCoordinator
from .entity import HypontechPlantEntity as HypontechPlantEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PLANT_STATUS_BINARY_SENSOR_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: HypontechConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HypontechPlantStatusBinarySensor(HypontechPlantEntity, BinarySensorEntity):
    entity_description: BinarySensorEntityDescription
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: HypontechDataCoordinator, plant_id: str) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
