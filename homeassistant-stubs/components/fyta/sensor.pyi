from .const import CONF_MAX_ACCEPTABLE as CONF_MAX_ACCEPTABLE, CONF_MAX_GOOD as CONF_MAX_GOOD, CONF_MIN_ACCEPTABLE as CONF_MIN_ACCEPTABLE, CONF_MIN_GOOD as CONF_MIN_GOOD
from .coordinator import FytaConfigEntry as FytaConfigEntry, FytaCoordinator as FytaCoordinator
from .entity import FytaPlantEntity as FytaPlantEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from fyta_cli.fyta_models import Plant as Plant
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfConductivity as UnitOfConductivity, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Final

@dataclass(frozen=True, kw_only=True)
class FytaSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Plant], StateType | datetime]

@dataclass(frozen=True, kw_only=True)
class FytaMeasurementSensorEntityDescription(FytaSensorEntityDescription):
    attribute_fn: Callable[[Plant], dict[str, float | None]]

PLANT_STATUS_LIST: list[str]
PLANT_MEASUREMENT_STATUS_LIST: list[str]
SENSORS: Final[list[FytaSensorEntityDescription]]
MEASUREMENT_SENSORS: Final[list[FytaMeasurementSensorEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: FytaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FytaPlantSensor(FytaPlantEntity, SensorEntity):
    entity_description: FytaSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime: ...

class FytaPlantMeasurementSensor(FytaPlantSensor):
    entity_description: FytaMeasurementSensorEntityDescription
    @property
    def extra_state_attributes(self) -> dict[str, float | None]: ...
