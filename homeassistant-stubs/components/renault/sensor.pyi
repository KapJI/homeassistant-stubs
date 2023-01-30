from .const import DOMAIN as DOMAIN
from .renault_coordinator import T as T
from .renault_entities import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from .renault_hub import RenaultHub as RenaultHub
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfEnergy as UnitOfEnergy, UnitOfLength as UnitOfLength, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import as_utc as as_utc, parse_datetime as parse_datetime
from typing import Any

class RenaultSensorRequiredKeysMixin:
    data_key: str
    entity_class: type[RenaultSensor[T]]
    def __init__(self, data_key, entity_class) -> None: ...

class RenaultSensorEntityDescription(SensorEntityDescription, RenaultDataEntityDescription, RenaultSensorRequiredKeysMixin[T]):
    icon_lambda: Union[Callable[[RenaultSensor[T]], str], None]
    condition_lambda: Union[Callable[[RenaultVehicleProxy], bool], None]
    requires_fuel: bool
    value_lambda: Union[Callable[[RenaultSensor[T]], Union[StateType, datetime]], None]
    def __init__(self, data_key, entity_class, coordinator, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement, icon_lambda, condition_lambda, requires_fuel, value_lambda) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultSensor(RenaultDataEntity[T], SensorEntity):
    entity_description: RenaultSensorEntityDescription[T]
    @property
    def data(self) -> StateType: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def native_value(self) -> Union[StateType, datetime]: ...

def _get_charging_power(entity: RenaultSensor[T]) -> StateType: ...
def _get_charge_state_formatted(entity: RenaultSensor[T]) -> Union[str, None]: ...
def _get_charge_state_icon(entity: RenaultSensor[T]) -> str: ...
def _get_plug_state_formatted(entity: RenaultSensor[T]) -> Union[str, None]: ...
def _get_plug_state_icon(entity: RenaultSensor[T]) -> str: ...
def _get_rounded_value(entity: RenaultSensor[T]) -> float: ...
def _get_utc_value(entity: RenaultSensor[T]) -> datetime: ...

SENSOR_TYPES: tuple[RenaultSensorEntityDescription[Any], ...]
