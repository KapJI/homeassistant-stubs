from .coordinator import Tami4ConfigEntry as Tami4ConfigEntry, Tami4EdgeCoordinator as Tami4EdgeCoordinator
from .entity import Tami4EdgeBaseEntity as Tami4EdgeBaseEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete
ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: Tami4ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class Tami4EdgeSensorEntity(Tami4EdgeBaseEntity, CoordinatorEntity[Tami4EdgeCoordinator], SensorEntity):
    def __init__(self, coordinator: Tami4EdgeCoordinator, entity_description: SensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def _update_attr(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
