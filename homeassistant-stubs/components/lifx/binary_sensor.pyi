from .const import HEV_CYCLE_STATE as HEV_CYCLE_STATE
from .coordinator import LIFXConfigEntry as LIFXConfigEntry, LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .entity import LIFXEntity as LIFXEntity
from .util import lifx_features as lifx_features
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

HEV_CYCLE_STATE_SENSOR: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LIFXConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LIFXHevCycleBinarySensorEntity(LIFXEntity, BinarySensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator, description: BinarySensorEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
