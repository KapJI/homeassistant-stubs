from .const import DIMENSIONLESS_UNITS as DIMENSIONLESS_UNITS, READOUT_ICONS as READOUT_ICONS, SECONDS_PER_DAY as SECONDS_PER_DAY, TIME_OF_DAY_READOUTS as TIME_OF_DAY_READOUTS, UNIT_MAP as UNIT_MAP, WIND_DIRECTION_SUBJECT as WIND_DIRECTION_SUBJECT
from .coordinator import HortimaxConfigEntry as HortimaxConfigEntry, HortimaxCoordinator as HortimaxCoordinator
from .entity import HortimaxEntity as HortimaxEntity
from _typeshed import Incomplete
from aiohortos import Readout as Readout
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import DEGREE as DEGREE, EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, UnitOfConductivity as UnitOfConductivity, UnitOfEnergy as UnitOfEnergy, UnitOfIrradiance as UnitOfIrradiance, UnitOfMass as UnitOfMass, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfRatio as UnitOfRatio, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final, override

PARALLEL_UPDATES: int
UNIT_DESCRIPTIONS: Final[dict[str, SensorEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: HortimaxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def _describe(readout: Readout) -> SensorEntityDescription: ...

class HortimaxReadoutSensor(HortimaxEntity, SensorEntity):
    _attr_name: Incomplete
    _attr_icon: Incomplete
    _attr_entity_category: Incomplete
    entity_description: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, coordinator: HortimaxCoordinator, device_id: str, key: str) -> None: ...
    @property
    @override
    def native_value(self) -> float | str | datetime | None: ...
