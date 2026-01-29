from .coordinator import PowerfoxBaseCoordinator as PowerfoxBaseCoordinator, PowerfoxConfigEntry as PowerfoxConfigEntry, PowerfoxDataUpdateCoordinator as PowerfoxDataUpdateCoordinator, PowerfoxReportDataUpdateCoordinator as PowerfoxReportDataUpdateCoordinator
from .entity import PowerfoxEntity as PowerfoxEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CURRENCY_EURO as CURRENCY_EURO, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from powerfox import Device as Device, GasReport as GasReport, HeatMeter, PowerMeter, WaterMeter
from typing import Any

@dataclass(frozen=True, kw_only=True)
class PowerfoxSensorEntityDescription[T: (PowerMeter, WaterMeter, HeatMeter)](SensorEntityDescription):
    value_fn: Callable[[T], float | int | None]

@dataclass(frozen=True, kw_only=True)
class PowerfoxReportSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[GasReport], float | int | None]

SENSORS_POWER: tuple[PowerfoxSensorEntityDescription[PowerMeter], ...]
SENSORS_WATER: tuple[PowerfoxSensorEntityDescription[WaterMeter], ...]
SENSORS_HEAT: tuple[PowerfoxSensorEntityDescription[HeatMeter], ...]
SENSORS_GAS: tuple[PowerfoxReportSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PowerfoxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BasePowerfoxSensorEntity[CoordinatorT: PowerfoxBaseCoordinator[Any]](PowerfoxEntity[CoordinatorT], SensorEntity):
    entity_description: SensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: CoordinatorT, device: Device, description: SensorEntityDescription) -> None: ...

class PowerfoxSensorEntity(BasePowerfoxSensorEntity[PowerfoxDataUpdateCoordinator]):
    coordinator: PowerfoxDataUpdateCoordinator
    entity_description: PowerfoxSensorEntityDescription
    @property
    def native_value(self) -> float | int | None: ...

class PowerfoxGasSensorEntity(BasePowerfoxSensorEntity[PowerfoxReportDataUpdateCoordinator]):
    coordinator: PowerfoxReportDataUpdateCoordinator
    entity_description: PowerfoxReportSensorEntityDescription
    @property
    def native_value(self) -> float | int | None: ...
