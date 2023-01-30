from .const import ATTR_DARK as ATTR_DARK, ATTR_ON as ATTR_ON
from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import DeconzGateway as DeconzGateway, get_gateway_from_config_entry as get_gateway_from_config_entry
from .util import serial_from_unique_id as serial_from_unique_id
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import DOMAIN as DOMAIN, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, ATTR_VOLTAGE as ATTR_VOLTAGE, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pydeconz.interfaces.sensors import SensorResources
from pydeconz.models.event import EventType as EventType
from pydeconz.models.sensor import SensorBase as PydeconzSensorBase
from pydeconz.models.sensor.air_quality import AirQuality
from pydeconz.models.sensor.consumption import Consumption
from pydeconz.models.sensor.daylight import Daylight
from pydeconz.models.sensor.generic_status import GenericStatus
from pydeconz.models.sensor.humidity import Humidity
from pydeconz.models.sensor.light_level import LightLevel
from pydeconz.models.sensor.power import Power
from pydeconz.models.sensor.pressure import Pressure
from pydeconz.models.sensor.temperature import Temperature
from pydeconz.models.sensor.time import Time
from typing import TypeVar

PROVIDES_EXTRA_ATTRIBUTES: Incomplete
ATTR_CURRENT: str
ATTR_POWER: str
ATTR_DAYLIGHT: str
ATTR_EVENT_ID: str
T = TypeVar('T', AirQuality, Consumption, Daylight, GenericStatus, Humidity, LightLevel, Power, Pressure, Temperature, Time, PydeconzSensorBase)

class DeconzSensorDescriptionMixin:
    supported_fn: Callable[[T], bool]
    update_key: str
    value_fn: Callable[[T], Union[datetime, StateType]]
    def __init__(self, supported_fn, update_key, value_fn) -> None: ...

class DeconzSensorDescription(SensorEntityDescription, DeconzSensorDescriptionMixin[T]):
    instance_check: Union[type[T], None]
    name_suffix: str
    old_unique_id_suffix: str
    def __init__(self, supported_fn, update_key, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement, instance_check, name_suffix, old_unique_id_suffix) -> None: ...

ENTITY_DESCRIPTIONS: tuple[DeconzSensorDescription, ...]

def async_update_unique_id(hass: HomeAssistant, unique_id: str, description: DeconzSensorDescription) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzSensor(DeconzDevice[SensorResources], SensorEntity):
    TYPE: Incomplete
    entity_description: DeconzSensorDescription
    unique_id_suffix: Incomplete
    _update_key: Incomplete
    _name_suffix: Incomplete
    def __init__(self, device: SensorResources, gateway: DeconzGateway, description: DeconzSensorDescription) -> None: ...
    @property
    def native_value(self) -> Union[StateType, datetime]: ...
    @property
    def extra_state_attributes(self) -> dict[str, Union[bool, float, int, str, None]]: ...

class DeconzBatteryTracker:
    sensor: Incomplete
    gateway: Incomplete
    description: Incomplete
    async_add_entities: Incomplete
    unsubscribe: Incomplete
    def __init__(self, sensor_id: str, gateway: DeconzGateway, description: DeconzSensorDescription, async_add_entities: AddEntitiesCallback) -> None: ...
    def async_update_callback(self) -> None: ...
