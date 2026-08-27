from .coordinator import IntelliClimaConfigEntry as IntelliClimaConfigEntry, IntelliClimaFilterCoordinator as IntelliClimaFilterCoordinator
from .entity import eco_device_info as eco_device_info
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyintelliclima.intelliclima_types import IntelliClimaECO as IntelliClimaECO
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: IntelliClimaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IntelliClimaFilterCleaningBinarySensor(CoordinatorEntity[IntelliClimaFilterCoordinator], BinarySensorEntity):
    _attr_has_entity_name: bool
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_device_info: Incomplete
    _device_sn: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IntelliClimaFilterCoordinator, device: IntelliClimaECO) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
