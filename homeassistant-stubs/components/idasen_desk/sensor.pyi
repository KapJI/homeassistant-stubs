from . import IdasenDeskConfigEntry as IdasenDeskConfigEntry, IdasenDeskCoordinator as IdasenDeskCoordinator
from .entity import IdasenDeskEntity as IdasenDeskEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfLength as UnitOfLength
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class IdasenDeskSensorDescription(SensorEntityDescription):
    value_fn: Callable[[IdasenDeskCoordinator], float | None]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: IdasenDeskConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IdasenDeskSensor(IdasenDeskEntity, SensorEntity):
    entity_description: IdasenDeskSensorDescription
    def __init__(self, coordinator: IdasenDeskCoordinator, description: IdasenDeskSensorDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
