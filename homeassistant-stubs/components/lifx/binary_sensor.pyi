from .const import HEV_CYCLE_STATE as HEV_CYCLE_STATE
from .coordinator import LIFXConfigEntry as LIFXConfigEntry, LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .entity import LIFXEntity as LIFXEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
HEV_CYCLE_STATE_SENSOR: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LIFXConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LIFXHevCycleBinarySensorEntity(LIFXEntity, BinarySensorEntity):
    def __init__(self, coordinator: LIFXUpdateCoordinator, description: BinarySensorEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    @callback
    @override
    def _async_update_attrs(self) -> None: ...
