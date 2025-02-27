from .coordinator import DormakabaDkeyConfigEntry as DormakabaDkeyConfigEntry, DormakabaDkeyCoordinator as DormakabaDkeyCoordinator
from .entity import DormakabaDkeyEntity as DormakabaDkeyEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from py_dormakaba_dkey.commands import Notifications as Notifications

@dataclass(frozen=True, kw_only=True)
class DormakabaDkeyBinarySensorDescription(BinarySensorEntityDescription):
    is_on: Callable[[Notifications], bool]

BINARY_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: DormakabaDkeyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DormakabaDkeyBinarySensor(DormakabaDkeyEntity, BinarySensorEntity):
    _attr_has_entity_name: bool
    entity_description: DormakabaDkeyBinarySensorDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DormakabaDkeyCoordinator, description: DormakabaDkeyBinarySensorDescription) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
