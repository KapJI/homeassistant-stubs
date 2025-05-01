from .coordinator import OhmeConfigEntry as OhmeConfigEntry
from .entity import OhmeEntity as OhmeEntity, OhmeEntityDescription as OhmeEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from ohme import OhmeApiClient as OhmeApiClient

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OhmeSensorDescription(OhmeEntityDescription, SensorEntityDescription):
    value_fn: Callable[[OhmeApiClient], str | int | float | None]

SENSOR_CHARGE_SESSION: Incomplete
SENSOR_ADVANCED_SETTINGS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: OhmeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OhmeSensor(OhmeEntity, SensorEntity):
    entity_description: OhmeSensorDescription
    @property
    def native_value(self) -> str | int | float | None: ...
