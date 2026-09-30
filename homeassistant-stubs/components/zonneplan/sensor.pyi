from .const import ZONNEPLAN_TIMEZONE as ZONNEPLAN_TIMEZONE
from .coordinator import ZonneplanConfigEntry as ZonneplanConfigEntry, ZonneplanCoordinator as ZonneplanCoordinator, ZonneplanData as ZonneplanData
from .entity import ZonneplanEntity as ZonneplanEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass, StateType as StateType
from homeassistant.const import CURRENCY_EURO as CURRENCY_EURO, PERCENTAGE as PERCENTAGE, UnitOfEnergy as UnitOfEnergy, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyzonneplan import ElectricityChartGroup as ElectricityChartGroup, GasChartGroup as GasChartGroup
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ZonneplanPriceSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[ZonneplanCoordinator], float | str | datetime | None]
    supported_fn: Callable[[ZonneplanCoordinator], bool] | None = ...

ZONNEPLAN_SENSORS: tuple[ZonneplanPriceSensorEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class ZonneplanUsageSensorEntityDescription(SensorEntityDescription):
    group_fn: Callable[[ZonneplanData], ElectricityChartGroup | GasChartGroup | None]
    value_fn: Callable[[ZonneplanData], Decimal | None]

ZONNEPLAN_USAGE_SENSORS: tuple[ZonneplanUsageSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ZonneplanConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ZonneplanPriceSensor(ZonneplanEntity, SensorEntity):
    entity_description: ZonneplanPriceSensorEntityDescription
    @property
    @override
    def native_value(self) -> StateType | datetime: ...

class ZonneplanUsageSensor(ZonneplanEntity, SensorEntity):
    entity_description: ZonneplanUsageSensorEntityDescription
    @property
    @override
    def native_value(self) -> Decimal | None: ...
    @property
    @override
    def last_reset(self) -> datetime | None: ...
