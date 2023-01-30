from . import FritzBoxDeviceEntity as FritzBoxDeviceEntity
from .const import CONF_COORDINATOR as CONF_COORDINATOR
from .model import FritzEntityDescriptionMixinBase as FritzEntityDescriptionMixinBase
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.climate import PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp
from pyfritzhome.fritzhomedevice import FritzhomeDevice as FritzhomeDevice
from typing import Final

class FritzEntityDescriptionMixinSensor(FritzEntityDescriptionMixinBase):
    native_value: Callable[[FritzhomeDevice], Union[StateType, datetime]]
    def __init__(self, suitable, native_value) -> None: ...

class FritzSensorEntityDescription(SensorEntityDescription, FritzEntityDescriptionMixinSensor):
    def __init__(self, suitable, native_value, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement) -> None: ...

def suitable_eco_temperature(device: FritzhomeDevice) -> bool: ...
def suitable_comfort_temperature(device: FritzhomeDevice) -> bool: ...
def suitable_nextchange_temperature(device: FritzhomeDevice) -> bool: ...
def suitable_nextchange_time(device: FritzhomeDevice) -> bool: ...
def suitable_temperature(device: FritzhomeDevice) -> bool: ...
def value_electric_current(device: FritzhomeDevice) -> float: ...
def value_nextchange_preset(device: FritzhomeDevice) -> str: ...
def value_scheduled_preset(device: FritzhomeDevice) -> str: ...

SENSOR_TYPES: Final[tuple[FritzSensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxSensor(FritzBoxDeviceEntity, SensorEntity):
    entity_description: FritzSensorEntityDescription
    @property
    def native_value(self) -> Union[StateType, datetime]: ...
