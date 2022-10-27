from .const import DOMAIN as DOMAIN, HEV_CYCLE_STATE as HEV_CYCLE_STATE
from .coordinator import LIFXSensorUpdateCoordinator as LIFXSensorUpdateCoordinator, LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .entity import LIFXSensorEntity as LIFXSensorEntity
from .util import lifx_features as lifx_features
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

HEV_CYCLE_STATE_SENSOR: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LIFXHevCycleBinarySensorEntity(LIFXSensorEntity, BinarySensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LIFXSensorUpdateCoordinator, description: BinarySensorEntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
