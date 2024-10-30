from .coordinator import AsekoConfigEntry as AsekoConfigEntry
from .entity import AsekoEntity as AsekoEntity
from aioaseko import Unit as Unit
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfElectricPotential as UnitOfElectricPotential, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

@dataclass(frozen=True, kw_only=True)
class AsekoSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Unit], StateType]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

SENSORS: list[AsekoSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: AsekoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AsekoSensorEntity(AsekoEntity, SensorEntity):
    entity_description: AsekoSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
