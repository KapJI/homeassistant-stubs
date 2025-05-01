from .coordinator import APCUPSdConfigEntry as APCUPSdConfigEntry, APCUPSdCoordinator as APCUPSdCoordinator
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Final

PARALLEL_UPDATES: int
_DESCRIPTION: Incomplete
_VALUE_ONLINE_MASK: Final[int]

async def async_setup_entry(hass: HomeAssistant, config_entry: APCUPSdConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OnlineStatus(CoordinatorEntity[APCUPSdCoordinator], BinarySensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: APCUPSdCoordinator, description: BinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
