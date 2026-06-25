from . import VeluxConfigEntry as VeluxConfigEntry
from .coordinator import VeluxLimitationCoordinator as VeluxLimitationCoordinator
from .entity import velux_device_info as velux_device_info, velux_unique_id as velux_unique_id
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: VeluxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VeluxRainSensor(CoordinatorEntity[VeluxLimitationCoordinator], BinarySensorEntity):
    _attr_entity_registry_enabled_default: bool
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: VeluxLimitationCoordinator, config_entry_id: str) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
