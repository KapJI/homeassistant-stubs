from .const import DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY
from .helpers import on_unload as on_unload
from homeassistant.components import mysensors as mysensors
from homeassistant.components.sensor import DOMAIN as DOMAIN, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONDUCTIVITY as CONDUCTIVITY, DEGREE as DEGREE, ELECTRICAL_CURRENT_AMPERE as ELECTRICAL_CURRENT_AMPERE, ELECTRICAL_VOLT_AMPERE as ELECTRICAL_VOLT_AMPERE, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, FREQUENCY_HERTZ as FREQUENCY_HERTZ, LENGTH_METERS as LENGTH_METERS, LIGHT_LUX as LIGHT_LUX, MASS_KILOGRAMS as MASS_KILOGRAMS, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, VOLT as VOLT, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SENSORS: dict[str, Union[list[Union[str, None]], dict[str, list[Union[str, None]]]]]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MySensorsSensor(mysensors.device.MySensorsEntity, SensorEntity):
    @property
    def force_update(self) -> bool: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    def _get_sensor_type(self) -> list[Union[str, None]]: ...
