from . import FytaConfigEntry as FytaConfigEntry
from .coordinator import FytaCoordinator as FytaCoordinator
from .entity import FytaPlantEntity as FytaPlantEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from fyta_cli.fyta_models import Plant as Plant
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfConductivity as UnitOfConductivity, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Final

@dataclass(frozen=True, kw_only=True)
class FytaSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Plant], StateType | datetime]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

PLANT_STATUS_LIST: list[str]
PLANT_MEASUREMENT_STATUS_LIST: list[str]
SENSORS: Final[list[FytaSensorEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: FytaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FytaPlantSensor(FytaPlantEntity, SensorEntity):
    entity_description: FytaSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime: ...
