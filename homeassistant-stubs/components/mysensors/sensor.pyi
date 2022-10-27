from .. import mysensors as mysensors
from .const import DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY
from .helpers import on_unload as on_unload
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONDUCTIVITY as CONDUCTIVITY, DEGREE as DEGREE, ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ELECTRIC_POTENTIAL_MILLIVOLT as ELECTRIC_POTENTIAL_MILLIVOLT, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, FREQUENCY_HERTZ as FREQUENCY_HERTZ, LENGTH_METERS as LENGTH_METERS, LIGHT_LUX as LIGHT_LUX, MASS_KILOGRAMS as MASS_KILOGRAMS, PERCENTAGE as PERCENTAGE, POWER_VOLT_AMPERE as POWER_VOLT_AMPERE, POWER_WATT as POWER_WATT, Platform as Platform, SOUND_PRESSURE_DB as SOUND_PRESSURE_DB, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS
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
