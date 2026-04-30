from .coordinator import PecoConfigEntry as PecoConfigEntry, PecoSmartMeterCoordinator as PecoSmartMeterCoordinator
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Final

PARALLEL_UPDATES: Final[int]

async def async_setup_entry(hass: HomeAssistant, config_entry: PecoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PecoBinarySensor(CoordinatorEntity[PecoSmartMeterCoordinator], BinarySensorEntity):
    _attr_icon: str
    _attr_device_class: Incomplete
    _attr_name: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PecoSmartMeterCoordinator, phone_number: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
