from .const import DEVICE_CLASS_CHARGE_STATE as DEVICE_CLASS_CHARGE_STATE, DEVICE_CLASS_PLUG_STATE as DEVICE_CLASS_PLUG_STATE, DOMAIN as DOMAIN
from .renault_coordinator import T as T
from .renault_entities import RenaultDataEntity as RenaultDataEntity, RenaultEntityDescription as RenaultEntityDescription
from .renault_hub import RenaultHub as RenaultHub
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from collections.abc import Callable as Callable
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, STATE_CLASS_TOTAL_INCREASING as STATE_CLASS_TOTAL_INCREASING, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, LENGTH_KILOMETERS as LENGTH_KILOMETERS, PERCENTAGE as PERCENTAGE, POWER_KILO_WATT as POWER_KILO_WATT, TEMP_CELSIUS as TEMP_CELSIUS, TIME_MINUTES as TIME_MINUTES, VOLUME_LITERS as VOLUME_LITERS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import as_utc as as_utc, parse_datetime as parse_datetime

class RenaultSensorRequiredKeysMixin:
    data_key: str
    entity_class: type[RenaultSensor]

class RenaultSensorEntityDescription(SensorEntityDescription, RenaultEntityDescription, RenaultSensorRequiredKeysMixin):
    icon_lambda: Union[Callable[[RenaultSensor[T]], str], None]
    condition_lambda: Union[Callable[[RenaultVehicleProxy], bool], None]
    requires_fuel: bool
    value_lambda: Union[Callable[[RenaultSensor[T]], StateType], None]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultSensor(RenaultDataEntity[T], SensorEntity):
    entity_description: RenaultSensorEntityDescription
    @property
    def data(self) -> StateType: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def native_value(self) -> StateType: ...

def _get_charging_power(entity: RenaultSensor[T]) -> StateType: ...
def _get_charge_state_formatted(entity: RenaultSensor[T]) -> Union[str, None]: ...
def _get_charge_state_icon(entity: RenaultSensor[T]) -> str: ...
def _get_plug_state_formatted(entity: RenaultSensor[T]) -> Union[str, None]: ...
def _get_plug_state_icon(entity: RenaultSensor[T]) -> str: ...
def _get_rounded_value(entity: RenaultSensor[T]) -> float: ...
def _get_utc_value(entity: RenaultSensor[T]) -> str: ...

SENSOR_TYPES: tuple[RenaultSensorEntityDescription, ...]
