from . import RenaultConfigEntry as RenaultConfigEntry
from .entity import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfEnergy as UnitOfEnergy, UnitOfLength as UnitOfLength, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import as_utc as as_utc, parse_datetime as parse_datetime
from renault_api.kamereon.models import KamereonVehicleBatteryStatusData, KamereonVehicleChargingSettingsData, KamereonVehicleDataAttributes as KamereonVehicleDataAttributes
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RenaultSensorEntityDescription[T: KamereonVehicleDataAttributes](SensorEntityDescription, RenaultDataEntityDescription):
    condition_lambda: Callable[[RenaultVehicleProxy], bool] | None = ...
    requires_fuel: bool = ...
    value_lambda: Callable[[RenaultSensor[T]], StateType | datetime]

async def async_setup_entry(hass: HomeAssistant, config_entry: RenaultConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RenaultSensor[T: KamereonVehicleDataAttributes](RenaultDataEntity[T], SensorEntity):
    entity_description: RenaultSensorEntityDescription[T]
    @property
    def native_value(self) -> StateType | datetime: ...

def _get_charge_state_formatted(entity: RenaultSensor[KamereonVehicleBatteryStatusData]) -> str | None: ...
def _get_plug_state_formatted(entity: RenaultSensor[KamereonVehicleBatteryStatusData]) -> str | None: ...
def _get_rounded_value(value: float | None) -> int | None: ...
def _get_utc_value(value: str | None) -> datetime | None: ...
def _get_charging_settings_mode_formatted(entity: RenaultSensor[KamereonVehicleChargingSettingsData]) -> str | None: ...

SENSOR_TYPES: tuple[RenaultSensorEntityDescription[Any], ...]
