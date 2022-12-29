from .. import mysensors as mysensors
from .const import DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY
from .helpers import on_unload as on_unload
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONDUCTIVITY as CONDUCTIVITY, DEGREE as DEGREE, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, Platform as Platform, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfPower as UnitOfPower, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfTemperature as UnitOfTemperature, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM
from typing import Any

SENSORS: dict[str, SensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MySensorsSensor(mysensors.device.MySensorsEntity, SensorEntity):
    _attr_force_update: bool
    entity_description: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def native_value(self) -> Union[str, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
    def _get_entity_description(self) -> Union[SensorEntityDescription, None]: ...
